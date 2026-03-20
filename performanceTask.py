
import pygame
pygame.init()

question = []
definition = []
next = False
clock = pygame.time.Clock()

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
        
numberOfCards = input("How many cards do you want to input? (please input as a number) ")

for i in range(0, int(numberOfCards)):
    print("\nNEW CARD")
    questionInput = input("What is the question for this card ")
    definitionInput = input("what is the answer for the question ")

    question.append(questionInput)
    definition.append(definitionInput)

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
            if event.key == pygame.K_SPACE:
                next = True
    
    w.fill((255, 255, 255))

    font = pygame.font.Font("Roboto/Roboto-VariableFont_wdth,wght.ttf", 20) #roboto, taken from google fonts

    #changing the text if the space bar is clicked
    if next:
        textToDisplay = checkTheText(textToDisplay, question, definition)
        next = False

    #putting the text onto the screen
    text = font.render(textToDisplay, True, (0, 0, 0))
    w.blit(text, (250, 250))

    pygame.display.flip()

    clock.tick(60)

