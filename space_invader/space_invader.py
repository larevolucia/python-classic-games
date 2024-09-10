"""space invader game"""
import math
import random
import pygame  # pylint: disable=import-error
from pygame import mixer  # pylint: disable=import-error

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_START_X = 380
PLAYER_START_Y = 480
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
NUM_OF_ENEMIES = 6
FONT_SIZE = 32
WHITE = (255, 255, 255)
INITIAL_NUM_ENEMIES = 6
ENEMY_INCREMENT_THRESHOLD = 5  # Add more enemies every 5 points

# Initialize the game
pygame.init() # pylint: disable=no-member
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('img/background.png')

# Sound settings
mixer.music.load('audio/background.wav')
mixer.music.play(-1)
music_on = pygame.image.load('img/music.png')
music_off = pygame.image.load('img/music-off.png')

def toggle_music(settings):
    """Toggle sound on and off."""
    if settings["is_music_on"]:
        pygame.mixer.music.set_volume(0.0)  # Mute the sound
    else:
        pygame.mixer.music.set_volume(1.0)  # Unmute the sound
    settings["is_music_on"] = not settings["is_music_on"]

def draw_music_button(settings):
    """Draw the sound toggle button."""
    if settings["is_music_on"]:
        screen.blit(music_on, (730, 10))
    else:
        screen.blit(music_off, (730, 10))

# Define sound effects
sound_on = pygame.image.load('img/sound.png')
sound_off = pygame.image.load('img/no-sound.png')
bullet_sound = mixer.Sound('audio/laser.wav')
explosion_sound = mixer.Sound('audio/explosion.wav')

music_settings = {
    "is_music_on": True
    }
sounds_settings = {
    "is_sound_on": True
}


# Toggle sound effects
def toggle_sound(settings):
    """Toggle sound on and off."""
    settings["is_sound_on"] = not settings["is_sound_on"]

def draw_sound_button(settings):
    """Draw the sound toggle button."""
    if settings["is_sound_on"]:
        screen.blit(sound_on, (670, 10))
    else:
        screen.blit(sound_off, (670, 10))

def play_bullet_sound(settings):
    """Play the bullet sound effect if sound is enabled."""
    if settings["is_sound_on"]:
        bullet_sound.play()

def play_collision_sound(settings):
    """Play the collision sound effect if sound is enabled."""
    if settings["is_sound_on"]:
        explosion_sound.play()

def is_collision(entity1_x, entity1_y, entity2_x, entity2_y, threshold=27):
    """Check if two entities have collided based on their positions."""
    distance = math.sqrt(math.pow(entity1_x - entity2_x, 2) + math.pow(entity1_y - entity2_y, 2))
    return distance < threshold

def show_score(score_value):
    """Display the current score on the screen."""
    score = font.render(f"Score: {score_value}", True, WHITE)
    screen.blit(score, (10, 10))

# Fonts
font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

# Classes
class Player:
    """creates player"""
    def __init__(self):
        self.image = pygame.image.load('img/player.png')
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.x_change = 0

    def move(self):
        """move player"""
        self.x += self.x_change
        self.x = max(0, min(self.x, SCREEN_WIDTH - 64))  # Ensure player stays on screen

    def draw(self):
        """draws the player"""
        screen.blit(self.image, (self.x, self.y))

class Bullet:
    """draws and defines fire event and movement"""
    def __init__(self):
        self.image = pygame.image.load('img/bullet.png')
        self.x = 0
        self.y = PLAYER_START_Y
        self.y_change = BULLET_SPEED
        self.state = "ready"

    def fire(self, x):
        """fire bullet"""
        if self.state == "ready":
            self.x = x
            self.state = "fire"

    def move(self):
        """bullet movement"""
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))
            self.y -= self.y_change
        if self.y <= 0:
            self.state = "ready"
            self.y = PLAYER_START_Y

class Enemy:
    """creates enemies"""
    def __init__(self):
        self.image = pygame.image.load('img/enemy.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = ENEMY_SPEED_X
        self.y_change = ENEMY_SPEED_Y

    def move(self):
        """enemy movement"""
        self.x += self.x_change
        if self.x <= 0:
            self.x_change = ENEMY_SPEED_X
            self.y += self.y_change
        elif self.x >= 736:
            self.x_change = -ENEMY_SPEED_X
            self.y += self.y_change

    def draw(self):
        """draw enemy"""
        screen.blit(self.image, (self.x, self.y))

def increase_difficulty(score, enemies, last_enemy_increase_score):
    """Add more enemies based on the score."""
    # Increase enemies only if the score crosses a threshold and enemies haven't been added yet
    if score % ENEMY_INCREMENT_THRESHOLD == 0 and score > last_enemy_increase_score:
        for _ in range(2):  # Increase by 2 enemies for each threshold reached
            enemies.append(Enemy())
        last_enemy_increase_score = score  # Update the last score at which enemies were added
    return last_enemy_increase_score  # Return the updated value



# Game Over
game_state = {
    "is_game_over": False
}

def show_game_over(score):
    """Display Game Over message."""
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    final_score_font = pygame.font.Font('freesansbold.ttf', 42)
    final_score_text = final_score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (200, 250))
    screen.blit(final_score_text, (300, 350))

# Main Game Loop
def game_loop():
    """create game loop"""
    clock = pygame.time.Clock()
    running = True
    player = Player()
    bullet = Bullet()
    enemies = [Enemy() for _ in range(INITIAL_NUM_ENEMIES)]
    score_value = 0
    last_enemy_increase_score = 0


    while running:
        screen.fill("black")
        screen.blit(background, (0, 0))
        # Check if the game is over


        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                mouse_x, mouse_y = event.pos
                if 730 <= mouse_x <= 730 + sound_on.get_width() and 10 <= mouse_y <= 10 + sound_on.get_height(): # pylint: disable=line-too-long
                    toggle_music(music_settings)
            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                mouse_x, mouse_y = event.pos
                if 670 <= mouse_x <= 670 + sound_on.get_width() and 10 <= mouse_y <= 10 + sound_on.get_height(): # pylint: disable=line-too-long
                    toggle_sound(sounds_settings)

            # Player movement
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if event.key == pygame.K_LEFT: # pylint: disable=no-member
                    player.x_change = -PLAYER_SPEED
                if event.key == pygame.K_RIGHT: # pylint: disable=no-member
                    player.x_change = PLAYER_SPEED
                if event.key == pygame.K_SPACE: # pylint: disable=no-member
                    if bullet.state == "ready":
                        bullet.fire(player.x)
                        play_bullet_sound(sounds_settings)

            if event.type == pygame.KEYUP: # pylint: disable=no-member
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # pylint: disable=no-member
                    player.x_change = 0
        # Check for Game Over
        if game_state["is_game_over"]:
            show_game_over(score_value)  # Display Game Over message
            pygame.display.update()  # Update the screen with the message
            continue  # Skip the rest of the game logic when the game is over

        # Increase difficulty by adding more enemies when the player reaches a new threshold
        last_enemy_increase_score = increase_difficulty(score_value, enemies, last_enemy_increase_score) # pylint: disable=line-too-long
        player.move()
        bullet.move()
        # Check for bullet and enemy collision
        for enemy in enemies:
            enemy.move()
            if is_collision(enemy.x, enemy.y, bullet.x, bullet.y):
                play_collision_sound(sounds_settings)
                bullet.state = "ready"
                bullet.y = PLAYER_START_Y
                score_value += 1
                enemy.x = random.randint(0, 736)
                enemy.y = random.randint(50, 150)
            enemy.draw()
            # Check if enemy hits the player
            if is_collision(player.x, player.y, enemy.x, enemy.y, threshold=40):
                play_collision_sound(sounds_settings)
                game_state["is_game_over"] = True
                break  # End the loop early since we only need one collision to end the game

        player.draw()
        show_score(score_value)
        draw_music_button(music_settings)
        draw_sound_button(sounds_settings)

        pygame.display.update()
        clock.tick(60)

    pygame.quit() # pylint: disable=no-member

# Start the game
game_loop()
