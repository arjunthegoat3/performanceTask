
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

    #putting the text onto the screen

    if start:
        
        text = font.render("How many cards do you want to input? (please input as a number) ", True, (0, 0, 0))
        w.blit(text, (250, 250))

        if enterPressed:

            cardCount = str(inputText)
            inputText = ""
            makeCards = True
            start = False

    elif makeCards:

        takingQuestion = True

        if takingQuestion:

            questionOutput = font.render("What is the question for this card? ", True, (0, 0, 0))
            w.blit(questionOutput, (250, 250))

            if enterPressed:

                question.append(inputText)
                inputText = ""
                takingQuestion = False
            

        else:

            definitionOutput = font.render("What is the answer for this card? ", True, (0, 0, 0))
            w.blit(definitionOutput, (250, 250))

            if enterPressed:


                definition.append(inputText)
                inputText = ""
                takingQuestion = True

        enterPressed = False
        inputCounter += 1

        if inputCounter == cardCount:
            makeCards = False

    else:

        textToDisplay = question[0]

        #changing the text if the space bar is clicked
        if next:
            textToDisplay = checkTheText(textToDisplay, question, definition)
            next = False


        text = font.render(textToDisplay, True, (0, 0, 0))
        w.blit(text, (250, 250))



        
    """
    if inputting:

        if setup:

            text = font.render("How many cards do you want to input? (please input as a number) ", True, (0, 0, 0))
            w.blit(text, (250, 250))

        #sees if the user inputted a number, if not the user will be prompted again

        try:
            numberOfCards = int(inputText)
            inputText = ""
            setup = False
        except:
            numberOfCards = 0
            font.render("How many cards do you want to input? - please input as a number (ex. 15) ", True, (0, 0, 0))
            
        if setup:
        #this part is written by chatgpt (beginning of chagpt programmed part)
        counter = font.render(("card " + str(currentCard)), True, (255, 0, 0))
        w.blit(counter, (20, 20))

        if typingQuestion:
            prompt = font.render("What is the question for this card ", True, (0, 0, 0))
        else:
            prompt = font.render("What is the answer for this question ", True, (0, 0, 0))

        w.blit(prompt, (250, 250))

        # show typed text
        typed = font.render(inputText, True, (0, 0, 255))
        w.blit(typed, (250, 300))

        #end of chatgpt programmed block

        try:
        
            textToDisplay = question[0]

            #changing the text if the space bar is clicked
            if next:
                textToDisplay = checkTheText(textToDisplay, question, definition)
                next = False

            text = font.render(textToDisplay, True, (0, 0, 0))
            input = font.render(textToDisplay, True, (0, 0, 0))

            w.blit(text, (250, 250))
            w.blit(input, (400, 250))
        
        except:
            None
        
        
    else:
    
    """
        
        

    

        
        
    pygame.display.flip()

    clock.tick(60)

