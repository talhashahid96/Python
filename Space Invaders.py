import pygame
import random
import math

# initialize the window
pygame.init()
# window open
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

# Background
bg_image = pygame.image.load("bg.jpg")
# Bullet
bullet_image = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 2.5
bullet_state = "ready"
# Player
playerimage = pygame.image.load("space-invaders (3).png")
playerx = 370
playery = 480
# Enemy
enemyimage = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 3
for i in range(num_of_enemies):
    enemyimage.append(pygame.image.load("game.png"))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(50, 100))
    enemyx_change.append(0.3)
    enemyy_change.append(0)
# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scorex = 10
scorey = 10
f_score = []
clock = pygame.time.Clock()

# Game Over
game_over_font = pygame.font.Font("freesansbold.ttf", 48)
game_over_font_x = 255
game_over_font_y = 260


def game_over(game_ver_front_x, game_over_font_y):
    over = game_over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over, (game_over_font_x, game_over_font_y))


def game_score(x, y):
    score = font.render("Score :" + "" + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))


# enemyimage2 = pygame.image.load("game.png")
# enemyx2 = random.randint(0, 736)
# enemyy2 = random.randint(50, 100)
# enemyx2_change = 0.3
# enemyy2_change = 0

# enemyimage3 = pygame.image.load("game.png")
# enemyx3 = random.randint(0, 736)
# enemyy3 = random.randint(50, 100)
# enemyx3_change = 0.3
# enemyy3_change = 0

# enemyimage4 = pygame.image.load("game.png")
# enemyx4 = random.randint(0, 736)
# enemyy4 = 50

player_change_x = 0
player_change_y = 0

score = 0
final_score = []


def player(x, y):
    screen.blit(playerimage, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x, y - 60))


def enemy(x, y, i):
    screen.blit(enemyimage[i], (x, y))


def enemy1(x, y):
    screen.blit(enemyimage2, (x, y))
    enemyx2 += enemyx2_change
    if enemyx2 <= 0:
        enemyx2_change = 0.3

        enemyy2_change = 0.06
    elif enemyx2 >= 736:
        enemyx2_change = -0.3
        enemyy2_change = 0.06


def enemy2(x, y):
    screen.blit(enemyimage3, (x, y))
    enemyx3 += enemyx3_change
    if enemyx3 <= 0:
        enemyx3_change = 0.3

        enemyy3_change = 0.06
    elif enemyx3 >= 736:
        enemyx3_change = -0.3
        enemyy3_change = 0.06


def iscollision(enemyx, enemyy, bullet_x, bullet_y, i):
    distance = math.sqrt(math.pow(enemyx[i] - bullet_x, 2) + (math.pow(enemyy[i] - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# def gameover(enemyy):
#    if enemyy >= 480:
#        return True
#    else:
#        return False


running = True
while running:
    clock.tick(1200)
    screen.fill((0, 0, 0))
    # Background
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = playerx  # Bullet starting x position matches player position
                    fire_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_LEFT:
                # print("Left key is pressed.")
                player_change_x = -0.3
            if event.key == pygame.K_RIGHT:
                # print("Right Key is pressed.")
                player_change_x = 0.3
            # if event.key == pygame.K_UP:
            #    player_change_y = -0.3
            # if event.key == pygame.K_DOWN:
            #    player_change_y = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # print("Key is released.")
                player_change_x = 0
                player_change_y = 0
    # The new value that is being increased by 0.1 as the key is pressed is being added to the original value.
    playerx += player_change_x
    playery += player_change_y
    # Boundaries
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    # bullet_x += bulletx_change
    # bullet_y += bullety_change
    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        enemyy[i] += enemyy_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.4
            enemyy_change[i] = 0.04
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.4
            enemyy_change[i] = 0.04

            # Collision
        collision = iscollision(enemyx, enemyy, bullet_x, bullet_y, i)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            # final_score.append(score)
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(50, 100)
        enemy(enemyx[i], enemyy[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullety_change
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    # game_over = gameover(enemyy)
    # if game_over:
    #    bullet_y = 480
    #    bullet_state = "ready"
    #    enemyy = 0
    #    enemyx_change = 0
    #    enemyy_change = 0
    #    enemyx[i] = 0
    #    playerx = 300
    #    playery = 480
    #    print("Game Over")
    for i in range(num_of_enemies):
        if enemyy[i] > 480:
            for j in range(num_of_enemies):
                enemyy[j] = 2000  # Move enemies off screen
            game_over(game_over_font_x, game_over_font_y)
            break
    player(playerx, playery)

    # bullet(bullet_x,bullet_y)
    game_score(scorex, scorey)
    # enemy3(enemyx4,enemyy4)
    # pygame.display.update has to be there. as it updates the game
    pygame.display.update()
