
import pygame
pygame.init()
import keyboard

question = []
definition = []
next = False
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

def checkTheText(currentText, questionList, definitionList):
    
    #uses a for loop to see what text is there, and updates the text to the next text that needs to be displayed

    for i in range(0, len(questionList)):

        #checking to see if i is too large, in which case returning questionList[0]
        #so that the questions cycle through again
        if currentText == definitionList[(len(questionList) - 1)]:
            return(questionList[0])

        if questionList[i] == currentText:
            return definitionList[i]
        elif definitionList[i] == currentText:
            return questionList[(i + 1)]
        
#numberOfCards = input("How many cards do you want to input? (please input as a number) ")

inputting = True
"""
for i in range(0, int(numberOfCards)):
    print("\nNEW CARD")
    questionInput = input("What is the question for this card ")
    definitionInput = input("what is the answer for the question ")

    question.append(questionInput)
    definition.append(definitionInput)
    inputting = False
"""
textToDisplay = ""

w = pygame.display.set_mode((700, 700))
pygame.display.set_caption("FLASH CARDS")
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if the space key is pressed, it will trigger a boolean and when the next question/slide
            #is shown the boolean will be set back to false.
            
            if event.key == pygame.K_SPACE:
                if not inputting:
                    next = True
                else:
                    inputText += " "
            
            elif event.key == pygame.K_BACKSPACE:
                inputText = inputText[0:(len(inputText) - 1)]
            
            elif event.key == pygame.K_RETURN:
                enterPressed = True
            else:
                inputText += pygame.key.name(event.key)

                        
    w.fill((255, 255, 255))

    font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20) #roboto, taken from google fonts

    """
    checking which boolean is true ands based on that running that part of the program,
    in the start it collects the amount of cards the program wants to make,
    then alternates between getting the question and answer for each card,
    then the program will go into quizzing the user.
    """

    if start:
        
        text = font.render("How many cards do you want to input? (please input as a number) ", True, (0, 0, 0))
        w.blit(text, (250, 250))

        if enterPressed:

            makeCards = True
            cardCount = int(inputText)
            inputText = ""
            start = False
            enterPressed = False

    elif makeCards:

        if takingQuestion:

            if not enterPressed and not next:

                questionOutput = font.render("What is the question for this card? ", True, (0, 0, 0))
                w.blit(questionOutput, (250, 250))

            else:

                question.append(inputText)
                inputText = ""
                enterPressed = False
                takingQuestion = False
                
            
        else:

            if not enterPressed and not next:

                definitionOutput = font.render("What is the answer for this card? ", True, (0, 0, 0))
                w.blit(definitionOutput, (250, 250))

            else:

                definition.append(inputText)
                inputText = ""
                enterPressed = False
                takingQuestion = True
                
    enterPressed = False
    inputCounter += 1

    if len(definition) == cardCount:
        makeCards = False

    if not start and not makeCards:

        try:
            textToDisplay = question[0]
        except:
            None

        #changing the text if the space bar is clicked
        if next or enterPressed:
            textToDisplay = checkTheText(textToDisplay, question, definition)
            next = False


        text = font.render(textToDisplay, True, (0, 0, 0))
        w.blit(text, (250, 250))        
        
    pygame.display.flip()

    clock.tick(60)

