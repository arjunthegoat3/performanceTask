5
import pygame
pygame.init()

question = []
definition = []

numberOfCards = input("How many cards do you want to input? (please input as a number)")

for i in range(0, int(numberOfCards)):
    print("\nNEW CARD")
    questionInput = input("What is the question for this card")
    definitionInput = input("what is the answer for the question")

    question.append(questionInput)
    definition.append(definitionInput)

w = pygame.display.set_mode((700, 700))
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
