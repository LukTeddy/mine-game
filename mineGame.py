import pygame
from sys import exit
from text import Text
from audio import Audio
from button import Button
from database import Database
from flag import Flag
from level import Level
from grid_ui import Grid_UI
from bomb import Bomb
from enemy import Enemy
from player import Player

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Mine Game")
clock = pygame.time.Clock()

# Classes
text = Text(screen)
test_font = text.font("orbitron-bold.otf", 60)
test_font2 = text.font("orbitron-bold.otf", 30)
#bg_music = Audio("bg_music2.wav", 0.25)
#bg_music.play()

# Data
data = Database()
winning_animation, losing_animation, finish_animation = data.define()
grid_ui = Grid_UI(screen, data)
flag = Flag()
bomb = Bomb(screen)
enemy = Enemy()
level = Level(bomb, enemy)

# Variables
game_active = False
gamemode = ""
level_num = 0
gamesPlayed = 0
gamesWon = 0

grid_size = 16
sizeVar = 480/grid_size
player = Player(screen, sizeVar, grid_size, bomb, flag)

# Grid Setup
grid = {}
for i in range(1, grid_size+1):
    grid['r' + str(i)] = []
    for j in range(1, grid_size+1):
        grid['r' + str(i)].append('c' + str(j))

# Images
menu_surface = pygame.image.load("assets/sprites/mineGame.png").convert_alpha()
normal_button = Button(screen, "normalButton.png")
insane_button = Button(screen, "insaneButton.png")


def reset():
    global grid_ui, flag, bomb, level, enemy
    grid_ui.__init__(screen, data)
    flag.__init__()
    bomb.__init__(screen)
    enemy.__init__()
    level.__init__(bomb, enemy)
    player.__init__(screen, sizeVar, grid_size, bomb, flag)
    bomb.level_update(level_num)


# Loop
while True:
    mouse = pygame.mouse.get_pos()
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            player.key_input(event.type)
        else:
            level_num = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if normal_button.check_clicked():
                    gamemode = "Normal"
                    level_num = 1
                    game_active = True
                    reset()
                elif insane_button.check_clicked():
                    gamemode = "Insane"
                    level_num = 1
                    game_active = True
                    reset()
    if game_active:
        screen.fill("Black")
        bomb.update()
        level.check_for_enemies(grid_size)
        if not enemy.placed:
            enemy.place(grid_size, sizeVar, bomb.max_bombs)
        grid_ui.grid_squares(grid_size, sizeVar)
        grid_ui.enemy_squares(enemy, sizeVar)
        flag.display(screen, sizeVar)
        grid_ui.bomb_squares(bomb, sizeVar)
        player.draw()
        if bomb.explode_on:
            player.active = False
            bomb.explode_bombs(grid_size, sizeVar, enemy)
        if level.update_grid(grid_ui) == "Lose":
            if gamemode == "Insane":
                level_num = 1
            gamesPlayed += 1
            reset()
        elif level.update_grid(grid_ui) == "Win":
            if level_num == 25:
                #level.beat()
                print("Simga")
            else:
                level_num += 1
                gamesWon += 1
                gamesPlayed += 1
                reset()
        if level.update_grid(grid_ui) == "Finish":
            if gamemode == "Insane":
                level_num = 1
            gamesPlayed += 1
            reset()
        # SideBar UI
        text.draw((640, 80), (50, 150, 50), test_font, f'Level {level_num}')
        text.draw((640, 200), (50, 150, 50), test_font2, f'Bombs: {bomb.number_left}/{bomb.max_bombs}')
        text.draw((640, 300), (50, 150, 50), test_font2, f'Games: {gamesPlayed}')
        text.draw((640, 400), (50, 150, 50), test_font2, f'Wins: {gamesWon}')
    else:
        # Menu UI
        screen.fill("Black")
        screen.blit(menu_surface, (100, 0))
        normal_button.draw(253, 400)
        insane_button.draw(554, 400)
    pygame.display.update()
    clock.tick(60)
