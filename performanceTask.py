import pygame
pygame.init()
import keyboard

question = []
definition = []
clock = pygame.time.Clock()
inputText = ""
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


correct = 0
incorrect = 0
attempted = 0
feedback = ""
#ChatGPT

def checkTheText(currentText, questionList, definitionList):
    
    #uses a for loop to see what text is there, and updates the text to the next text that needs to be displayed

    for i in range(0, len(questionList)):

        #checking to see if i is too large, in which case returning questionList[0]
        #so that the questions cycle through again
        if currentText == definitionList[(len(questionList) - 1)] or currentText == "":
            return(questionList[0])

        if questionList[i] == currentText:
            return definitionList[i]
        elif definitionList[i] == currentText:
            return questionList[(i + 1)]
        
def getXToCenter(surfaceToCenter):

    #gets the x value with which the text will be centered

    rect = surfaceToCenter.get_rect()
    temp = (350 - (rect.width/2))
    return temp
        
#numberOfCards = input("How many cards do you want to input? (please input as a number) ")

inputting = True
textToDisplay = ""

w = pygame.display.set_mode((700, 700))
icon = pygame.image.load("icon.png") #notebook picture, from dreamstime website
pygame.display.set_icon(icon)
pygame.display.set_caption("FLASH CARDS")
font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20) #roboto, taken from google fonts
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if the space key is pressed, it will trigger a boolean and when the next question/slide
            #is shown the boolean will be set back to false.
            
            if event.key == pygame.K_SPACE:
                inputText += " "
            
            elif event.key == pygame.K_BACKSPACE:
                inputText = inputText[0:(len(inputText) - 1)]
            
            elif event.key == pygame.K_RETURN:
                enterPressed = True
            else:
                if len(pygame.key.name(event.key)) == 1:
                    inputText += pygame.key.name(event.key)

                        
    w.fill((255, 255, 255))

    #having text be displayed when the boolean is true
    if showUserInput:
        
        userInput = font.render(inputText, True, (0, 0, 255))
        w.blit(userInput, (getXToCenter(userInput), 600))

    """
    checking which boolean is true ands based on that running that part of the program,
    in the start it collects the amount of cards the program wants to make,
    then alternates between getting the question and answer for each card,
    then the program will go into quizzing the user.
    """

    if start:
        
        numberInputText = font.render("How many cards do you want to input? (please input as a number) ", True, (0, 0, 0))
        nutX = getXToCenter(numberInputText)
        w.blit(numberInputText, (nutX, 250))

        if enterPressed:

            makeCards = True
            cardCount = int(inputText)
            inputText = ""
            start = False
            enterPressed = False

    elif makeCards:

        if takingQuestion:

            if not enterPressed:
                
                questionOutput = font.render("What is the question for this card? ", True, (0, 0, 0))
                qoX = getXToCenter(questionOutput)
                w.blit(questionOutput, (qoX, 250))

            else:

                question.append(inputText)
                inputText = ""
                enterPressed = False
                takingQuestion = False
                
            
        else:

            if not enterPressed:

                definitionOutput = font.render("What is the answer for this card? ", True, (0, 0, 0))
                doX = getXToCenter(definitionOutput)
                w.blit(definitionOutput, (doX, 250))

            else:

                definition.append(inputText)
                inputText = ""
                enterPressed = False
                takingQuestion = True
                

                
        inputCounter += 1

        if len(definition) == cardCount:
            firstQuestionCycle = True
            makeCards = False
            
            

    if not start and not makeCards:

        showUserInput = True

        if firstQuestionCycle:
            textToDisplay = checkTheText(textToDisplay, question, definition)
            firstQuestionCycle = False

        if enterPressed:
            attempted += 1
            for i in range(len(question)):
                if textToDisplay == question[i]:
                    if inputText.lower() == definition[i].lower():
                        correct += 1
                        feedback = "Correct!"
                    else:
                        incorrect += 1
                        feedback = "Incorrect!"
            inputText = ""
            textToDisplay = checkTheText(textToDisplay, question, definition)
            enterPressed = False

        questionCycleText = font.render(textToDisplay, True, (0, 0, 0))
        qctX = getXToCenter(questionCycleText)
        w.blit(questionCycleText, (qctX, 250))

        attemptedNumber = font.render("Attempted: " + str(attempted), True, (0, 0, 0))
        w.blit(attemptedNumber, (20, 40))

        correctText = font.render("Correct: " + str(correct), True, (0,255,0))
        w.blit(correctText, (20,20))

        wrongText = font.render(f"Incorrect: {incorrect}", True, (255, 0, 0))
        w.blit(wrongText, (20, 60))

        feedbackText = font.render(feedback, True, (0, 150, 0))
        w.blit(feedbackText, (getXToCenter(feedbackText), 350))
# ChatGPT, used for Debugging  
# 
    pygame.display.flip()

    clock.tick(60)