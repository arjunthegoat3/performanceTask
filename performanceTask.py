
import pygame
pygame.init()
import keyboard

question = [""]
definition = []
next = False
clock = pygame.time.Clock()
inputText = ""
inputCounter = 0

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

textToDisplay = question[0]

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
            print(inputText)
            if event.key == pygame.K_SPACE and not inputting:
                next = True
            elif event.key == pygame.K_BACKSPACE:
                inputText = inputText[0:(len(inputText) - 1)]
            else:
                inputText += pygame.key.name(event.key)

                        
    w.fill((255, 255, 255))

    font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20) #roboto, taken from google fonts

    #changing the text if the space bar is clicked
    if next:
        textToDisplay = checkTheText(textToDisplay, question, definition)
        next = False

    #putting the text onto the screen
    
    if inputting:
        
        numberOfCards = 0
        font.render("How many cards do you want to input? (please input as a number) ", True, (0, 0, 0))

        try:
            numberOfCards = int(inputText)
            inputText = ""
        except:
            numberOfCards = 0
            font.render("How many cards do you want to input? - please input as a number (ex. 15) ", True, (0, 0, 0))
            
        for i in range(0, int(numberOfCards)):
            temp = ""
            temp += "\nNEW CARD"
            temp += "What is the question for this card "
            temp += "what is the answer for the question "

            question.append(questionInput)
            definition.append(definitionInput)
            inputting = False

        text = font.render(textToDisplay, True, (0, 0, 0))
        input = font.render(textToDisplay, True, (0, 0, 0))

        w.blit(text, (250, 250))
        w.blit(input, (400, 250))
    else:
        text = font.render(textToDisplay, True, (0, 0, 0))
        w.blit(text, (250, 250))

    pygame.display.flip()

    clock.tick(60)

