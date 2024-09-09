"""Recriating Space Invaders game using Python"""



import math
import random




import pygame #pylint:disable=import-error



from pygame import mixer #pylint:disable=import-error




# initialize the game
pygame.init()




# create screen



screen = pygame.display.set_mode((800, 600))




# load background



background = pygame.image.load('space_invader/img/background.png')


# Initialize sound settings
IS_SOUND_ON = True



# load sound



mixer.music.load('space_invader/audio/background.wav')



mixer.music.play(-1)


sound_on = pygame.image.load('space_invader/img/sound.png')

sound_off = pygame.image.load('space_invader/img/no-sound.png')


def toggle_audio():

    """toggle sound on and off"""

    global IS_SOUND_ON

    if IS_SOUND_ON:

        pygame.mixer.music.set_volume(0.0)  # Mute the sound
        IS_SOUND_ON = False

    else:

        pygame.mixer.music.set_volume(1.0)  # Unmute the sound
        IS_SOUND_ON = True


def draw_sound_button():

    """initialize the sound buttons"""

    if IS_SOUND_ON:

        screen.blit(sound_on, (730, 10))

    else:

        screen.blit(sound_off, (730, 10))

# caption and icon



pygame.display.set_caption("Space Invader")



icon = pygame.image.load('space_invader/img/ufo.png')

pygame.display.set_icon(icon)




# player image



playerImg = pygame.image.load('space_invader/img/player.png')



PLAYER_X = 370



PLAYER_Y = 480



PLAYER_X_CHANGE = 0




def player(x, y):



    """Initialize the player"""



    screen.blit(playerImg, (x, y))




# score

# Fire - The bullet is currently moving

bullet_Img = pygame.image.load('space_invader/img/bullet.png')
bullet_X = 0
bullet_Y = 480
bullet_X_change = 0
bullet_Y_change = 10
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Img, (x + 16, y + 10))

def isColission(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# enemies
enemy_img = []
enemy_X = []
enemy_Y= []
enemy_X_change = []
enemy_Y_change = []
NUM_OF_ENEMIES = 6

for i in range(NUM_OF_ENEMIES):
    enemy_img.append(pygame.image.load('space_invader/img/enemy.png'))
    enemy_X.append(random.randint(0, 736))
    enemy_Y.append(random.randint(50, 150))
    enemy_X_change.append(4)
    enemy_Y_change.append(40)

def enemy(x, y, i):
    """display enemies"""
    screen.blit(enemy_img[i], (x, y))

SCORE_VALUE = 0



font = pygame.font.Font('freesansbold.ttf', 32)


SCORE_X = 10


SCORE_Y = 10



def show_score(x,y):


    """render the score"""


    score = font.render("Score: " + str(SCORE_VALUE), True, (255, 255, 255))



    screen.blit(score, (x , y))



clock = pygame.time.Clock()



RUNNING = True





while RUNNING:




    # background-color



    screen.fill("black")




    #background-image



    screen.blit(background, (0,0))




    # pygame.QUIT event means the user clicked X to close your window




    for event in pygame.event.get():




        if event.type == pygame.QUIT:



            RUNNING = False


        # Handle mouse clicks to toggle sound

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            if 750 <= mouse_x <= 750 + sound_on.get_width() and 10 <= mouse_y <= 10 + sound_on.get_height():
                toggle_audio()


        # handle player input

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('space_invader/audio/laser.wav')
                    bullet_sound.play()
                    #get coordinates
                    bullet_X = PLAYER_X
                    fire_bullet(bullet_X, bullet_Y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    PLAYER_X_CHANGE = 0

              
    # RENDER YOUR GAME HERE
    PLAYER_X += PLAYER_X_CHANGE
    if PLAYER_X <= 0:
        PLAYER_X = 0
    elif PLAYER_X >= 736:
        PLAYER_X = 736

    #Enemy movement
    for i in range(NUM_OF_ENEMIES):
        enemy_X[i] += enemy_X_change[i]
        if enemy_X[i] <= 0:
            enemy_X_change[i] = 4
            enemy_Y[i] += enemy_Y_change[i]
        elif enemy_X[i] >= 736:
            enemy_X_change[i] = -4
            enemy_Y[i] += enemy_Y_change[i]
        enemy(enemy_X[i], enemy_Y[i], i)

        #collision

        collision = isColission(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if collision:
            explosionSound = mixer.Sound('space_invader/audio/explosion.wav')
            explosionSound.play()
            bullet_Y = 480
            bullet_state = "ready"
            SCORE_VALUE += 1
            enemy_X[i] = random.randint(0, 736)
            enemy_Y[i] = random.randint(50, 250)

    # Bullet movement
    if bullet_Y <= 0:
        bullet_Y = 400
        bullet_state = "ready"
    
    if bullet_state is "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Y_change

    # Draw the sound button

    draw_sound_button()


    # Draw Player

    player(PLAYER_X, PLAYER_Y)


    # Show Score

    show_score(SCORE_X, SCORE_Y)

    pygame.display.update()





    clock.tick(60)  # limits FPS to 60





pygame.quit()
