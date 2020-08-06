import pygame
import random

HEIGHT = 500
WIDTH = 800
FPS = 60
BACKGROUND_COLOR = (255, 228, 196)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BROWN = (165, 42, 42)


class dice(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


def win_check(win_condition):
    dice_one_point = random.randint(1, 6)
    dice_two_point = random.randint(1, 6)
    sum = dice_one_point + dice_two_point
    if win_condition == 1:
        if sum <= 7:
            return dice_one_point, dice_two_point, sum, 1
        else:
            return dice_one_point, dice_two_point, sum, 0
    if win_condition == 2:
        if sum == 7:
            return dice_one_point, dice_two_point, sum, 1
        else:
            return dice_one_point, dice_two_point, sum, 0
    if win_condition == 3:
        if sum >= 7:
            return dice_one_point, dice_two_point, sum, 1
        else:
            return dice_one_point, dice_two_point, sum, 0


random.seed()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 26)

dices = [dice(30, 30, 'data/images/one.png'),
         dice(30, 30, 'data/images/two.png'),
         dice(30, 30, 'data/images/three.png'),
         dice(30, 30, 'data/images/four.png'),
         dice(30, 30, 'data/images/five.png'),
         dice(30, 30, 'data/images/six.png')]

dice_one = pygame.Surface((60, 60))
dice_one.fill(BACKGROUND_COLOR)
dice_two = pygame.Surface((60, 60))
dice_two.fill(BACKGROUND_COLOR)

button_more_than_7 = pygame.Surface((100, 50))
button_more_than_7.fill(BACKGROUND_COLOR)
button_more_than_7_image = pygame.image.load('data/images/more_than_seven.png')

button_less_than_7 = pygame.Surface((100, 50))
button_less_than_7.fill(BACKGROUND_COLOR)
button_less_than_7_image = pygame.image.load('data/images/less_than_seven.png')

button_equals_7 = pygame.Surface((100, 50))
button_equals_7.fill(BACKGROUND_COLOR)
button_equals_7_image = pygame.image.load('data/images/equals_seven.png')

button_roll = pygame.Surface((100, 50))
button_roll.fill(BACKGROUND_COLOR)
button_roll_image = pygame.image.load('data/images/roll.png')

button_restart = pygame.Surface((100, 50))
button_restart.fill(BACKGROUND_COLOR)
button_restart_image = pygame.image.load('data/images/restart.png')

play = True
win_condition_is = 0  # 1 - <7, 2 - =7, 3 - >7
roll_has_been_pressed = 0

while play:

    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = event.pos
                if 300 <= click_pos[1] <= 350:
                    if 200 <= click_pos[0] <= 300:
                        win_condition_is = 1
                    if 350 <= click_pos[0] <= 450:
                        win_condition_is = 2
                    if 500 <= click_pos[0] <= 600:
                        win_condition_is = 3
                if 400 <= click_pos[1] <= 450:
                    if 350 <= click_pos[0] <= 450:
                        roll_has_been_pressed = 1

    pos = pygame.mouse.get_pos()
    if 300 <= pos[1] <= 350:
        if 200 <= pos[0] <= 300:
            button_less_than_7.fill(RED)
        else:
            button_less_than_7.fill(BACKGROUND_COLOR)
        if 350 <= pos[0] <= 450:
            button_equals_7.fill(RED)
        else:
            button_equals_7.fill(BACKGROUND_COLOR)
        if 500 <= pos[0] <= 600:
            button_more_than_7.fill(RED)
        else:
            button_more_than_7.fill(BACKGROUND_COLOR)

    if win_condition_is == 1:
        button_less_than_7.fill(GREEN)
    elif win_condition_is == 2:
        button_equals_7.fill(GREEN)
    elif win_condition_is == 3:
        button_more_than_7.fill(GREEN)

    dice_one.blit(dices[0].image, dices[0].rect)
    dice_two.blit(dices[0].image, dices[0].rect)

    if roll_has_been_pressed == 1:
        if win_condition_is == 0:
            textbox = font.render('please, choose the win condition', 1, BROWN)
            screen.blit(textbox, (220, 50))
        if win_condition_is == 1 or win_condition_is == 2 or win_condition_is == 3:
            pause = True
            dice_one_point, dice_two_point, sum, win = win_check(win_condition_is)
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pause = False
                        play = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if 300 <= event.pos[1] <= 350:
                                if 350 <= event.pos[0] <= 450:
                                    win_condition_is = 0
                                    roll_has_been_pressed = 0
                                    pause = False

                screen.fill(BACKGROUND_COLOR)
                dice_one.blit(dices[dice_one_point - 1].image, dices[dice_one_point - 1].rect)
                dice_two.blit(dices[dice_two_point - 1].image, dices[dice_two_point - 1].rect)
                if win:
                    string = "congratulation! your score is - " + str(sum)
                    textbox = font2.render(string, 1, GREEN)
                    screen.blit(textbox, (220, 50))

                else:
                    string = "sorry, your score is - " + str(sum)
                    textbox = font2.render(string, 1, BROWN)
                    screen.blit(textbox, (220, 50))
                screen.blit(dice_one, (300, int(HEIGHT / 2) - 90))
                screen.blit(dice_two, (450, int(HEIGHT / 2) - 90))
                button_restart.blit(button_restart_image, (0, 0))
                screen.blit(button_restart, (350, 300))
                pygame.display.update()

    screen.blit(dice_one, (300, int(HEIGHT / 2) - 90))
    screen.blit(dice_two, (450, int(HEIGHT / 2) - 90))
    button_more_than_7.blit(button_more_than_7_image, (0, 0))
    button_less_than_7.blit(button_less_than_7_image, (0, 0))
    button_equals_7.blit(button_equals_7_image, (0, 0))
    button_roll.blit(button_roll_image, (0, 0))
    screen.blit(button_less_than_7, (200, 300))
    screen.blit(button_equals_7, (350, 300))
    screen.blit(button_more_than_7, (500, 300))
    screen.blit(button_roll, (350, 400))

    clock.tick(FPS)

    pygame.display.update()
