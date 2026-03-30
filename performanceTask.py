import pygame
import random
pygame.init()
pygame.key.set_repeat(300, 50) #line written by ChatGPT

question = []
definition = []
cardIDs = []
clock = pygame.time.Clock()
inputText = "Type here:"
inputCounter = 0
currentCard = 0
start = True
makeCards = True
doQuestions = True
enterPressed = False
cardCount = ""
takingQuestion = True
firstQuestionCycle = True
showUserInput = True
showFeedback = False
showWarning = False
mouseDown = False
finished = False
cardRect = pygame.Rect(100, 100, 500, 350)
homePage = True
shuffleMode = False

correct = 0
incorrect = 0
attempted = 0
feedback = ""
#ChatGPT

def cycleTheText(currentText, questionList, definitionList, goBack=False):
    
    for i in range(0, len(questionList)):

        if currentText == definitionList[(len(questionList) - 1)] or currentText == "":
            return(questionList[0])

        if questionList[i] == currentText:
            return definitionList[i]
        elif definitionList[i] == currentText:
            return questionList[(i + 1)]
        
def getXToCenter(surface):

    rect = surface.get_rect()
    temp = (350 - (rect.width/2))
    return temp

def getCollisionStatus(surface, x, y):

    global mouseDown

    mouseCoordinate = pygame.mouse.get_pos()
    rect = surface.get_rect(topleft = (x, y))

    if rect.collidepoint(mouseCoordinate) and mouseDown:
        return True
    else:
        return False

inputting = True
textToDisplay = ""

w = pygame.display.set_mode((700, 700))
icon = pygame.image.load("icon.png")
finishButton = pygame.image.load("finishButton.png")
nextButton = pygame.image.load("next.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("FLASH CARDS")
font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20)
largeFont = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 40)
largeFont.set_bold(True)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s:
                  shuffleMode = not shuffleMode
                  if shuffleMode:
                      combined = list(zip(question, definition, cardIDs)) 
                      random.shuffle(combined)
                      question, definition, cardIDs = zip(*combined)
                      question = list(question)
                      definition = list(definition)
                      cardIDs = list(cardIDs)

            if homePage:
                continue
            
            if event.key == pygame.K_SPACE:
                if inputText != "Type here:":
                    inputText += " "
                else:
                    inputText = ""
                    inputText += " "
            
            elif event.key == pygame.K_BACKSPACE:

                if inputText != "Type here:":
                    inputText = inputText[0:(len(inputText) - 1)]
                else:
                    inputText = ""
                    inputText = inputText[0:(len(inputText) - 1)]
                    
            elif event.key == pygame.K_RETURN:

                if inputText != "Type here:":
                    enterPressed = True
                else:
                    inputText = ""
                    enterPressed = True
            

            else:

                if inputText != "Type here:":
                    if event.unicode.isprintable:
                        inputText += event.unicode

                else:
                    inputText = ""
                    if event.unicode.isprintable:
                        inputText += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True

    w.fill((255, 255, 255))

    if showUserInput:
        
        inputBox = pygame.Rect(100, 580, 500, 40)
        pygame.draw.rect(w, (240, 240, 240), inputBox, border_radius=10)
        pygame.draw.rect(w, (0, 0, 0), inputBox, 2, border_radius=10)

        userInput = font.render(inputText, True, (0, 0, 255))
        w.blit(userInput, (inputBox.x + 10, inputBox.y + 8))

    if homePage:

        showUserInput = False
        titleText = largeFont.render("FLASHCARD MAKER", True, (0, 0, 0))
        w.blit(titleText, (getXToCenter(titleText), 250))

        w.blit(nextButton, (getXToCenter(nextButton), 500))

        if getCollisionStatus(nextButton, getXToCenter(nextButton), 500):

            showUserInput = True
            homePage = False

    elif start:
        
        numberInputText = font.render("How many questions do you want to create? (please input as a number) ", True, (0, 0, 0))
        nutX = getXToCenter(numberInputText)
        w.blit(numberInputText, (nutX, 250))

        if showWarning:

            warning = font.render("Please enter your answer as a number (ex. 10)", True, (255, 0, 0))
            w.blit(warning, (getXToCenter(warning), 400))

        if enterPressed:

            try:
                cardCount = int(inputText)
                makeCards = True
                inputText = "Type here:"
                start = False
                showWarning = False
                enterPressed = False
            except:
                showWarning = True
                enterPressed = False

    elif makeCards:

        if takingQuestion:

            if not enterPressed:
                
                questionOutput = font.render("What is the question for this card? ", True, (0, 0, 0))
                qoX = getXToCenter(questionOutput)
                w.blit(questionOutput, (qoX, 250))

            else:

                question.append(inputText)
                inputText = "Type here:"
                enterPressed = False
                takingQuestion = False
                
        else:

            if not enterPressed:

                definitionOutput = font.render("What is the answer for this card? ", True, (0, 0, 0))
                doX = getXToCenter(definitionOutput)
                w.blit(definitionOutput, (doX, 250))

            else:

                definition.append(inputText)
                cardIDs.append(len(definition)) #assigning unique number to each card
                inputText = "Type here:"
                enterPressed = False
                takingQuestion = True

        inputCounter += 1

        if len(definition) == cardCount:
            firstQuestionCycle = True
            makeCards = False

    if finished:

        showUserInput = False
        scoreText = largeFont.render("Your score " + str(correct) + "/" + str(attempted), True, (200, 200, 0))
        try:
            scorePercent = 100*(correct/attempted)
        except:
            scorePercent = 0

        #typecasting to int to avoid weird numbers
        scorePercent = int(scorePercent)

        w.blit(finishButton, (getXToCenter(finishButton), 500))

        if getCollisionStatus(finishButton, getXToCenter(finishButton), 500):

            running = False
        
        scoreTextPercent = largeFont.render(str(scorePercent) + "%", True, (255, 0, 0))
        w.blit(scoreText, (getXToCenter(scoreText), 100))
        w.blit(scoreTextPercent, (getXToCenter(scoreTextPercent), 145))

    elif not start and not makeCards:
        titleText = largeFont.render("FLASHCARD MAKER", True, (0, 0, 0))
        w.blit(titleText, (getXToCenter(titleText), 20))
        showUserInput = True

        cardNumberText = font.render(
             f"Card # {cardIDs[currentCard]} out of {len(question)}", #display card # out of total
             True, 
              (0, 0, 0)
            )
        w.blit(cardNumberText, (500, 20))

        w.blit(finishButton, (150, 500))
        w.blit(nextButton, (450, 500))

        if firstQuestionCycle:
            textToDisplay = cycleTheText(textToDisplay, question, definition)
            firstQuestionCycle = False

        if enterPressed or getCollisionStatus(nextButton, 450, 500):
            for i in range(len(question)):
                if textToDisplay == question[i]:
                    currentCard = (currentCard + 1) % len(question)
                    if inputText.lower() == definition[i].lower():
                        correct += 1
                        feedback = "Correct!"
                    else:
                        incorrect += 1
                        feedback = "Incorrect!"

                    attempted += 1

            if showFeedback:
                showFeedback = False
            else:
                showFeedback = True
            inputText = "Type here:"
            textToDisplay = cycleTheText(textToDisplay, question, definition)
            enterPressed = False

        elif getCollisionStatus(finishButton, 150, 500):

            finished = True

        pygame.draw.rect(w, (230, 230, 230), cardRect, border_radius=15)
        pygame.draw.rect(w, (0, 0, 0), cardRect, 3, border_radius=15)

        questionCycleText = font.render("Question: " + textToDisplay, True, (0, 0, 0))
        qctX = getXToCenter(questionCycleText)
        w.blit(questionCycleText, (qctX, 250))

        attemptedNumber = font.render("Attempted: " + str(attempted), True, (0, 0, 0))
        w.blit(attemptedNumber, (20, 40))

        correctText = font.render("Correct: " + str(correct), True, (0, 255, 0))
        w.blit(correctText, (20,20))

        wrongText = font.render(f"Incorrect: {incorrect}", True, (255, 0, 0))
        w.blit(wrongText, (20, 60))

        shuffleText = font.render(f"Shuffle: {'ON' if shuffleMode else 'OFF'}", True, (0,0,0))
        w.blit(shuffleText, (20, 80))

        if showFeedback:

            if feedback == "Incorrect!":
                answerText = font.render("Answer:", True, (255, 0, 0))
                w.blit(answerText, (getXToCenter(answerText), 230))
                feedbackColor = (255, 0, 0)
            elif feedback == "Correct!":
                answerText = font.render("Answer:", True, (0, 200, 0))
                w.blit(answerText, (getXToCenter(answerText), 230))
                feedbackColor = (0, 200, 0)

            feedbackText = largeFont.render(feedback, True, feedbackColor)
            w.blit(feedbackText, (getXToCenter(feedbackText), 350))

            
    pygame.display.flip()
    mouseDown = False
    clock.tick(60)