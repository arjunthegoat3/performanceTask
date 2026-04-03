import pygame
import random
pygame.init()
pygame.key.set_repeat(300, 50) #line written by ChatGPT

#--DEFINING VARIABLES--#

question = []
definition = []
cardIDs = []
originalQuestion = []
originalDefinition = []
originalCardIDs = []
clock = pygame.time.Clock()
inputText = "Type here:"
currentCard = 0
start = True
makeCards = True
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
inputBox = pygame.Rect(100, 580, 500, 40)
homePage = True
shuffleMode = False
blitAnswerWarning = False
textToDisplay = ""
overflow = False
cardInputNumber = 1
feedbackColor = (255, 255, 255)

correct = 0
incorrect = 0
attempted = 0
feedback = ""
#ChatGPT

#--CYCLETHETEXT FUNCTION DEFINITION--#

def cycleTheText(currentText, questionList, definitionList, goBack=False):
    
    for i in range(0, len(questionList)):

        #uses a for loop to see what text is there, and updates the 
        #text to the next text that needs to be displayed, returns a string

        
        if currentText == definitionList[(len(questionList) - 1)] or currentText == "":

            #checking to see if i is too large, in which case returning questionList[0]
            #so that the questions cycle through again

            return(questionList[0])

        if questionList[i] == currentText:

            return definitionList[i]
        
        elif definitionList[i] == currentText:

            return questionList[(i + 1)]
        
#--GETXTOCENTER DEFINITION--#
        
def getXToCenter(surface):

    #gets the x value with which the text will be centered,
    #returns an int

    rect = surface.get_rect()
    temp = (350 - (rect.width/2))
    return temp

#--GETCOLLISIONSTATUS DEFINITION--#

def getCollisionStatus(surface, x, y):

    #finds the coordinate of the mouse and checks if it collides with the
    #provided surface, returns a boolean

    global mouseDown

    mouseCoordinate = pygame.mouse.get_pos()
    rect = surface.get_rect(topleft = (x, y))

    if rect.collidepoint(mouseCoordinate) and mouseDown:
        return True
    else:
        return False

#--PYGAME OBJECT DEFINITIONS--#

#creating and configuring all pygame objects
w = pygame.display.set_mode((700, 700))
icon = pygame.image.load("icon.png") #notebook picture, from dreamstime website
finishButton = pygame.image.load("finishButton.png") #made in canva
nextButton = pygame.image.load("next.png") #made in canva
shuffleModeButton = pygame.image.load("shuffleModeButton.png") #made in canva
pygame.display.set_icon(icon)
pygame.display.set_caption("FLASH CARDS")
font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20) #roboto, taken from google fonts
largeFont = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 40) #roboto, taken from google fonts
clickSound = pygame.mixer.Sound("universfield-computer-mouse-click-352734.mp3") #taken from pixabay
clickSound.set_volume(0.7)
largeFont.set_bold(True)

#--PYGAME FOR LOOP--#

running = True
while running:

    #--EVENT LOOP--#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            #if the space key is pressed, it will trigger a boolean and when the next question/slide
            #is shown the boolean will be set back to false.
            
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

                userInput = font.render(inputText, True, (0, 0, 255))
                userInputRect = userInput.get_rect()

                if not overflow:

                    if inputText != "Type here:":
                        if event.unicode.isprintable():
                            inputText += event.unicode

                    else:
                        inputText = ""
                        if event.unicode.isprintable():
                            inputText += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickSound.play()
            mouseDown = True

    w.fill((255, 255, 255))

    #--BLITTING USER INPUT IF TO BE SHOWN--#

    if showUserInput:

        userInput = font.render(inputText, True, (0, 0, 255))
        userInputRect = userInput.get_rect()

        #checking for overflow

        if (userInputRect.width + 20) >= inputBox.width:

            inputWarning = font.render("Input is too long", True, (255, 0, 0))
            w.blit(inputWarning, (getXToCenter(inputWarning), 400))
            overflow = True

        else:

            overflow = False



        #having text be displayed when the boolean is true
        userInput = font.render(inputText, True, (0, 0, 255))
        pygame.draw.rect(w, (240, 240, 240), inputBox, border_radius=10)
        pygame.draw.rect(w, (0, 0, 0), inputBox, 2, border_radius=10)

        w.blit(userInput, (inputBox.x + 10, inputBox.y + 8))

    """
    checking which boolean is true ands based on that running that part of the program,
    in the start it collects the amount of cards the program wants to make,
    then alternates between getting the question and answer for each card,
    then the program will go into quizzing the user.
    """

    #--BLITTING ELEMENTS IF USER IS ON HOMEPAGE--#

    if homePage:

        showUserInput = False
        titleText = largeFont.render("FLASHCARD MAKER", True, (0, 0, 0))
        w.blit(titleText, (getXToCenter(titleText), 250))

        w.blit(nextButton, (getXToCenter(nextButton), 500))

        summaryText1 = font.render(
         "Create your own digital flashcards,",
         True,
          (0, 0, 0)
        )
        summaryText2 = font.render(
         "and quiz yourself",
         True,
        (0, 0, 0)
        )

        w.blit(summaryText1, (getXToCenter(summaryText1), 320))
        w.blit(summaryText2, (getXToCenter(summaryText2), 350))

        if getCollisionStatus(nextButton, getXToCenter(nextButton), 500):

            showUserInput = True
            homePage = False

    #--AMOUNT OF CARDS INPUTTING--#

    elif start:
        
        #adding next button
        w.blit(nextButton, (getXToCenter(nextButton), 500))

        numberInputText = font.render("How many questions do you want to create? (please input as a number) ", True, (0, 0, 0))
        w.blit(numberInputText, (getXToCenter(numberInputText), 250))

        if showWarning:

            warning = font.render("Please enter your answer as a number (ex. 10)", True, (255, 0, 0))
            w.blit(warning, (getXToCenter(warning), 400))

        if enterPressed or getCollisionStatus(nextButton, getXToCenter(nextButton), 500):

            #tries to typecast the input to an int, if not possible adds a warning to the front end,
            #if possible moves to the question creation cycle

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

    #--QUESTION INPUT CYCLE--#

                

    elif makeCards:


        cardInputNumberText = font.render("Card # " + str(cardInputNumber), True, (0, 0, 0))
        w.blit(cardInputNumberText, (10, 10))
        w.blit(nextButton, (getXToCenter(nextButton), 500))

        

        if takingQuestion:

            if not (enterPressed or getCollisionStatus(nextButton, getXToCenter(nextButton), 500)):


                questionOutput = font.render("What is the question for this card? ", True, (0, 0, 0))
                qoX = getXToCenter(questionOutput)
                w.blit(questionOutput, (qoX, 250))

            elif enterPressed or getCollisionStatus(nextButton, getXToCenter(nextButton), 500):

                question.append(inputText)
                inputText = "Type here:"
                enterPressed = False
                takingQuestion = False
                
        else:

            if not (enterPressed or getCollisionStatus(nextButton, getXToCenter(nextButton), 500)):

                definitionOutput = font.render("What is the answer for this card? ", True, (0, 0, 0))
                doX = getXToCenter(definitionOutput)
                w.blit(definitionOutput, (doX, 250))

                if blitAnswerWarning:

                    warning = font.render("Answer cannot be the same as the question", True, (255, 0, 0))
                    w.blit(warning, (getXToCenter(warning), 400))

            elif enterPressed or getCollisionStatus(nextButton, getXToCenter(nextButton), 500):

                cardInputNumber += 1

                #answer cannot be same as question to prevent logic errors with the cycleTheText function

                if inputText != question[len(question) - 1]:

                    definition.append(inputText)
                    cardIDs.append(len(definition)) #assigning unique number to each card

                    #resetting everything
                    blitAnswerWarning = False
                    inputText = "Type here:"
                    enterPressed = False
                    takingQuestion = True

                else:

                    blitAnswerWarning = True
                    enterPressed = False



        if len(definition) == cardCount:
            originalQuestion = question.copy()
            originalDefinition = definition.copy()
            originalCardIDs = cardIDs.copy()
            firstQuestionCycle = True
            makeCards = False
    #section for if the program is finished

    #--FINSIHED ANSWERING OUTPUT--#

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

    #--QUESTION AND ANSWER CYCLE--#

    elif not start and not makeCards:

        showUserInput = True

        cardNumberText = font.render(
             f"Card # {cardIDs[currentCard]} out of {len(question)}", #display card # out of total
             True, 
              (0, 0, 0)
            )
        
        #--SHOWING LIVE PERCENTAGES--#

        try:
            currentScorePercent = 100*(correct/attempted)

            if currentScorePercent > 60:

                color = (0, 255, 0)

            else:

                color = (255, 0, 0)

        except:
            currentScorePercent = 0

            color = (255, 0, 0)

        #typecasting to avoid weird numbers
        currentScorePercent = int(currentScorePercent)

        currentScorePercentText = largeFont.render(str(currentScorePercent) + "%", True, color)
        w.blit(currentScorePercentText, (600, 24))

        w.blit(cardNumberText, (530, 7))
        w.blit(shuffleModeButton, (getXToCenter(shuffleModeButton), 475))
        w.blit(finishButton, (150, 500))
        w.blit(nextButton, (450, 500))

        if getCollisionStatus(shuffleModeButton, getXToCenter(shuffleModeButton), 475):

            shuffleMode = not shuffleMode

            if shuffleMode:
                 combined = list(zip(question, definition, cardIDs)) 
                 random.shuffle(combined)
                 question, definition, cardIDs = zip(*combined)
                 question = list(question)
                 definition = list(definition)
                 cardIDs = list(cardIDs)

                 currentCard = 0
                 textToDisplay = ""
                 firstQuestionCycle = True

            else:
                  question = originalQuestion.copy()
                  definition = originalDefinition.copy()
                  cardIDs = originalCardIDs.copy()
        
                  currentCard = 0
                  textToDisplay = ""
                  firstQuestionCycle = True

            #When the shuffle mode is on the cards

        if firstQuestionCycle:
            textToDisplay = cycleTheText(textToDisplay, question, definition)
            firstQuestionCycle = False


        if enterPressed or getCollisionStatus(nextButton, 450, 500):
            

            for i in range(len(question)):
                if textToDisplay == question[i]:
                    
                    if inputText.lower() == definition[i].lower():
                        correct += 1
                        feedback = "Correct!"
                    else:
                        incorrect += 1
                        feedback = "Incorrect!"

                    attempted += 1

                elif textToDisplay == definition[i]:

                    currentCard = (currentCard + 1) % len(question)

            #if showfeedback is already true, it becomes false otherwise it becomes true
            if showFeedback:
                showFeedback = False
            else:
                showFeedback = True
            
            inputText = "Type here:"
            textToDisplay = cycleTheText(textToDisplay, question, definition)
            enterPressed = False

        elif getCollisionStatus(finishButton, 150, 500):

            finished = True

        #--DRAWING CONSISTANT ELEMENTS--#
        pygame.draw.rect(w, (230, 230, 230), cardRect, border_radius=15)
        pygame.draw.rect(w, (0, 0, 0), cardRect, 3, border_radius=15)

        questionCycleText = font.render(textToDisplay, True, (0, 0, 0))
        qctX = getXToCenter(questionCycleText)
        w.blit(questionCycleText, (qctX, 250))

        attemptedNumber = font.render("Attempted: " + str(attempted), True, (0, 0, 0))
        w.blit(attemptedNumber, (20, 35))

        correctText = font.render("Correct: " + str(correct), True, (0, 255, 0))
        w.blit(correctText, (20,15))

        wrongText = font.render(f"Incorrect: {incorrect}", True, (255, 0, 0))
        w.blit(wrongText, (20, 55))

        shuffleText = font.render(f"Shuffle: {'ON' if shuffleMode else 'OFF'}", True, (0,0,0))
        w.blit(shuffleText, (20,75))
        #displays wheter the shuffle mode is on or off

        #--SHOWING FEEDBACK IF SHOWING ANSWER--#

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
            
# ChatGPT, used for Debugging  

    #--PER FRAME CONFIGURATIONS--#
            
    pygame.display.flip()
    mouseDown = False
    clock.tick(60)
