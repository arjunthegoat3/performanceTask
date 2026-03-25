import pygame
pygame.init()

question = []
definition = []
next = False
clock = pygame.time.Clock()
inputText = ""

correct = 0
incorrect = 0
attempted = 0
feedback = ""

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

inputting = True

for i in range(0, int(numberOfCards)):
    print("\nNEW CARD")
    questionInput = input("What is the question for this card ")
    definitionInput = input("what is the answer for the question ")

    question.append(questionInput)
    definition.append(definitionInput)
    inputting = False

textToDisplay = question[0]

w = pygame.display.set_mode((700, 700))
pygame.display.set_caption("FLASH CARDS")
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                inputText = inputText[:-1]

            elif event.key == pygame.K_RETURN:
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
                next = True

            elif event.key == pygame.K_SPACE and not inputting:
                next = True

            else:
                inputText += event.unicode

                        
    w.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 40)

    #changing the text if the space bar is clicked
    if next:
        textToDisplay = checkTheText(textToDisplay, question, definition)
        next = False

    #putting the text onto the screen
    text = font.render(textToDisplay, True, (0, 0, 0))
    textRect = text.get_rect(center=(350, 250))
    w.blit(text, textRect)

    inputSurface = font.render("Your Answer: " + inputText, True, (0,0,255))
    inputRect = inputSurface.get_rect(center=(350, 500))
    w.blit(inputSurface, inputRect)

    scoreText = font.render(f"Score: {correct}/{attempted}", True, (0,0,0))
    w.blit(scoreText, (20, 20))

    wrongText = font.render(f"Incorrect: {incorrect}", True, (255,0,0))
    w.blit(wrongText, (20, 60))

    feedbackText = font.render(feedback, True, (0,150,0))
    feedbackRect = feedbackText.get_rect(center=(350, 350))
    w.blit(feedbackText, feedbackRect)

    pygame.display.flip()

    clock.tick(60)