import pygame
import os 
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1500, 900 
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #making the window for the game 
pygame.display.set_caption("Space Game")

white = (255, 255, 255)
black = (0, 0, 0)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)

border = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

health_font = pygame.font.SysFont("comicsans", 40)
winner_font = pygame.font.SysFont("comicsans", 150)


vel = 4
bullet_vel = 6
spaceship_width, spaceship_height = 90,70

blue_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

blue_spaceship_image = pygame.image.load("Assets/blue.png")  #loads the image from the appropriate path 
blue_spaceship = pygame.transform.rotate(pygame.transform.scale(blue_spaceship_image, (spaceship_width, spaceship_height)), 270) # rotates and scales the image 

red_spaceship_image = pygame.image.load("Assets/red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 90)

space = pygame.transform.scale(pygame.image.load("Assets/spacemove.png"), (WIDTH, HEIGHT))

def draw_window(blue, red, blue_bullets, red_bullets, blue_health, red_health):
    WIN.blit(space, (0,0))
    pygame.draw.rect(WIN, white, border) #draws an item in the window that is black and is the border

    blue_health_text = health_font.render("Blue Health: " + str(blue_health), 1, white)
    red_health_text = health_font.render("Red Health: " + str(red_health), 1, white)
    WIN.blit(blue_health_text, (250, 10))
    WIN.blit(red_health_text, (1000,10))

    WIN.blit(blue_spaceship, (blue.x, blue.y)) #blit puts items onto the screen. This is blitting the spaceship on screen
    WIN.blit(red_spaceship, (red.x,red.y))



    for bullet in blue_bullets:
        pygame.draw.rect(WIN, blue_color, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(WIN, red_color, bullet)

    pygame.display.update() #updates the display 

def blue_movement(keys_pressed, color):
    if keys_pressed[pygame.K_a] and color.x - vel > 0: #blue ship moving Left
        color.x -= vel
    if keys_pressed[pygame.K_d] and color.x + vel + color.width < border.x: #blue ship moving Right
        color.x += vel
    if keys_pressed[pygame.K_w] and color.y - vel > 0: #blue ship moving up
        color.y -= vel
    if keys_pressed[pygame.K_s] and color.y + vel + color.height < border.height - 15: #blue ship moving down
        color.y += vel

def red_movement(keys_pressed, color):
    if keys_pressed[pygame.K_LEFT] and color.x - vel > border.x + border.width: #red ship moving Left
        color.x -= vel
    if keys_pressed[pygame.K_RIGHT] and color.x + vel + color.width < WIDTH + 20: #red ship moving Right
        color.x += vel
    if keys_pressed[pygame.K_UP] and color.y - vel > 0: #red ship moving up
        color.y -= vel
    if keys_pressed[pygame.K_DOWN] and color.y + vel + color.height < border.height - 15: #red ship moving down
        color.y += vel

def handle_bullets(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            blue_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)


    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(blue_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet) 

def draw_winner(text):
    draw_text = winner_font.render(text, 1, white)
    WIN.blit(draw_text, (400, 100))
    pygame.display.update()
    pygame.time.delay(5000)
