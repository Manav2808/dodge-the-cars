import pygame
from random import choice

pygame.init()

screen = pygame.display.set_mode((900, 600))

Spawn_Enemies_Timer_1 = pygame.USEREVENT + 1
pygame.time.set_timer(Spawn_Enemies_Timer_1, 550)
Spawn_Enemies_Timer_2 = pygame.USEREVENT + 2
pygame.time.set_timer(Spawn_Enemies_Timer_2, 1000)
Spawn_Enemies_Timer_3 = pygame.USEREVENT + 3
pygame.time.set_timer(Spawn_Enemies_Timer_3, 1990)

Cars_List = []

class Player:
    def __init__(self, Player):
        self.player = Player
        self.pos = 3
        self.rect = pygame.Rect(16, 340, 64, 64)

    def draw(self):
        if self.pos == 1:
            self.rect.topleft = (16, 20)
            screen.blit(PLAYER, self.rect)
        elif self.pos == 2:
            self.rect.topleft = (16, 160)
            screen.blit(PLAYER, self.rect)
        elif self.pos == 3:
            self.rect.topleft = (16, 310)
            screen.blit(PLAYER, self.rect)
        elif self.pos == 4:
            self.rect.topleft = (16, 460)
            screen.blit(PLAYER, self.rect)

class ENEMY:
    def __init__(self, Enemy_Color, Enemy_Rect):
        self.enemy = Enemy_Color
        self.rect = pygame.Rect(Enemy_Rect[0], Enemy_Rect[1], 64, 64)

    def move(self):
        self.rect.x -= 12

#Fonts
TITLE_FONT = pygame.font.SysFont('consolas', 65)
TITLE = TITLE_FONT.render("DODGE THE CARS", True, (0, 100, 20))
TITLE_RECT = TITLE.get_rect(center = (450, 70))

INSTRUCT_FONT = pygame.font.SysFont('consolas', 50)
INSTRUCT = INSTRUCT_FONT.render("Press Space/Esc to Start/Exit", True, (0, 100, 20))
INSTRUCT_RECT = INSTRUCT.get_rect(center = (450, 520))

HOW_TO_PLAY_FONT = pygame.font.SysFont('calibri', 40)
HOW_TO_PLAY = HOW_TO_PLAY_FONT.render("Use Up/Down Arrow Keys to Move the Car", True, (0, 75, 10))
HOW_TO_PLAY_RECT = HOW_TO_PLAY.get_rect(center = (450, 240))

SCORE_FONT = pygame.font.SysFont('cambria', 40)

#Player
PLAYER = pygame.image.load("Assets\Player.png").convert_alpha()
player = Player(PLAYER)

#Enemy
Enemy_Brown = pygame.image.load("Assets\Enemy_Brown.png").convert_alpha()
Enemy_Cyan = pygame.image.load("Assets\Enemy_Cyan.png").convert_alpha()
Enemy_Green = pygame.image.load("Assets\Enemy_Green.png").convert_alpha()
Enemy_Violet = pygame.image.load("Assets\Enemy_Violet.png").convert_alpha()

Enemy_Pos_1 = (900, 20)
Enemy_Pos_2 = (900, 160)
Enemy_Pos_3 = (900, 310)
Enemy_Pos_4 = (900, 460)

def main_menu():
    screen.fill((169, 123, 0))

    screen.blit(TITLE, TITLE_RECT)
    screen.blit(HOW_TO_PLAY, HOW_TO_PLAY_RECT)

    #Player
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 308, 900, 130))
    #Road
    screen.blit(PLAYER, (16, 310))

    screen.blit(INSTRUCT, INSTRUCT_RECT)

def play_game(player_pos, Cars_List):
    global score

    screen.fill((169, 123, 0))

    #Roads
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 16, 900, 130))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 162, 900, 130))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 308, 900, 130))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 454, 900, 130))

    #Player
    player.draw()

    for Cars in Cars_List:
        screen.blit(Cars.enemy, Cars.rect)
        Cars.move()

    #Score
    score = int(pygame.time.get_ticks() / 1000)
    SCORE = SCORE_FONT.render(f"{score}", True, (255, 255, 255))
    SCORE_RECT = SCORE.get_rect(center = (450, 50))
    screen.blit(SCORE, SCORE_RECT)

def Game_Over(score):
    GAME_OVER = TITLE_FONT.render("GAME OVER", True, (255, 0, 0))
    GAME_OVER_RECT = GAME_OVER.get_rect(center = (450, 260))
    SCORE = SCORE_FONT.render(f"Your Score: {score}", True, (0, 255, 0))
    SCORE_RECT = SCORE.get_rect(center = (450, 330))

    screen.blit(GAME_OVER, GAME_OVER_RECT)
    screen.blit(SCORE, SCORE_RECT)

    pygame.display.update()

    pygame.time.delay(3000)

screen_counter = 1
player_pos = 3
game_over = 0
score = 0

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if screen_counter == 2:
            if event.type == Spawn_Enemies_Timer_1:
                Enemy = choice([Enemy_Brown, Enemy_Cyan, Enemy_Green, Enemy_Violet])
                Enemy_Pos = choice([Enemy_Pos_1, Enemy_Pos_2, Enemy_Pos_3, Enemy_Pos_4])
                enemy = ENEMY(Enemy, Enemy_Pos)
                Cars_List.append(enemy)
            if event.type == Spawn_Enemies_Timer_2:
                Enemy = choice([Enemy_Brown, Enemy_Cyan, Enemy_Green, Enemy_Violet])
                Enemy_Pos = choice([Enemy_Pos_1, Enemy_Pos_2, Enemy_Pos_3, Enemy_Pos_4])
                enemy_2 = ENEMY(Enemy, Enemy_Pos)
                Cars_List.append(enemy_2)
            if event.type == Spawn_Enemies_Timer_3:
                Enemy = choice([Enemy_Brown, Enemy_Cyan, Enemy_Green, Enemy_Violet])
                Enemy_Pos = choice([Enemy_Pos_1, Enemy_Pos_2, Enemy_Pos_3, Enemy_Pos_4])
                enemy_3 = ENEMY(Enemy, Enemy_Pos)
                Cars_List.append(enemy_3)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                screen_counter = 2

            if event.key == pygame.K_UP:
                if player.pos > 1:
                    player.pos -= 1
            if event.key == pygame.K_DOWN:
                if player.pos < 4:
                    player.pos += 1

    if screen_counter == 1:
        main_menu()
    elif screen_counter == 2:
        play_game(player_pos, Cars_List)

    for enemies in Cars_List:
        if player.rect.colliderect(enemies.rect):
            game_over = 1

    if game_over == 1:
        Game_Over(score)
        running = False

    for enemies in Cars_List:
        if enemies.rect.y < 0:
            del enemies

    pygame.display.update()

pygame.quit()
