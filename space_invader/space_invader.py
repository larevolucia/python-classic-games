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


SCORE_VALUE = 0



font = pygame.font.Font('freesansbold.ttf', 28)


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



    # RENDER YOUR GAME HERE


    # Draw the sound button

    draw_sound_button()


    # Draw Player

    player(PLAYER_X, PLAYER_Y)


    # Show Score

    show_score(SCORE_X, SCORE_Y)

    pygame.display.update()





    clock.tick(60)  # limits FPS to 60





pygame.quit()
