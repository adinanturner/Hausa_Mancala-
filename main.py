import pygame
from GUI import Drawer
from Play import Play
from Game import Game
import time
import random

def show_story_screen(screen):
    story_1 = (
        "Zomo da kura sun yi abota. Duk lokacin da suka je farauta, zomo yana ta tsere, "
        "yana barin kura da komai. Ranar nan kura ta ce, 'Ina jin haushi, ka daina gudu.' "
        "Sai zomo ya ce, 'To, mu raba abinci daidai.' Kura ta amince. Suna kamawa, zomo ya ce, "
        "'Rabinka tsoka, rabina kashi.' Kura ta daina abota da zomo. "
        "Darasi: Idan wani ya fi ka wayo, ka dinga lura da yanda kake yarda da shi."
    )

    story_2 = (
        "Wata mata tana da kwarya tana ajiyewa 'ya'yanta ruwa. Rana guda tsuntsu ya zo ya fasa kwaryar. "
        "Yara suka rasa ruwa. Da aka kama tsuntsun, ya ce, 'Ba da gangan ba ne.' "
        "Amma kwarya ta riga ta karye. "
        "Darasi: Ka lura da abin da kake yi, domin sakamakon wasu kuskure baya gyaruwa."
    )

    stories = [story_1, story_2]
    selected_story = random.choice(stories)

    font = pygame.font.SysFont("Arial", 28)
    text_color = (0, 0, 0)
    bg_color = (255, 255, 200)

    screen.fill(bg_color)

    # Word wrap for long story
    words = selected_story.split()
    lines = []
    line = ""
    for word in words:
        if font.size(line + word)[0] < 700:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y = 100
    for line in lines:
        rendered = font.render(line.strip(), True, text_color)
        rect = rendered.get_rect(center=(screen.get_width()//2, y))
        screen.blit(rendered, rect)
        y += 35

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False
# game loop

draw = Drawer()
running = True
test = Play()
game = Game(1)
player = 1

while (not game.gameOver()):
    if (player == 1):
        draw.DisplayPossibleMoves(game.state.possibleMoves(1))
        player = test.humanTurn(game)
        draw.RemovePossibleMoves(game.state.possibleMoves(1))
        draw.Update1(game.state.board)
        draw.DisplayTurn(player)
    else:
        player, game = test.computerTurn(game, test)
        draw.Update2(game.state.board)
        draw.DisplayTurn(player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

player, score = game.findWinner()
draw.DisplayTheWinner(player, score)

# 🔥 Show Hausa story after the winner
show_story_screen(pygame.display.get_surface())

time.sleep(2)
pygame.quit()
