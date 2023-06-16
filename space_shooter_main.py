import pygame
import os 
pygame.font.init()
pygame.mixer.init()

from space_shooter_func import draw_window, blue_movement, red_movement, handle_bullets, draw_winner, blue_hit, red_hit, spaceship_height, spaceship_width

max_bullets = 10

fps = 60

bullet_sound = pygame.mixer.Sound("Assets/shot.mp3")
explosion_sound = pygame.mixer.Sound("Assets/explosion.mp3")

def main():
    blue = pygame.Rect(100, 375, spaceship_width, spaceship_height)
    red = pygame.Rect(1300, 375, spaceship_width, spaceship_height)

    blue_bullets = []
    red_bullets = []
    blue_health = 10
    red_health = 10

    clock = pygame.time.Clock() 
    run = True 
    while run:
        clock.tick(fps) #locks the fps so it isn't open ended
        for event in pygame.event.get():   #loops through all events in the game 
            if event.type == pygame.QUIT:  #if user exits the window 
                run = False #ends the while loop which quits the game 
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < max_bullets:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height//2 +5, 10, 5)
                    blue_bullets.append(bullet)
                    bullet_sound.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 +5, 10, 5)
                    red_bullets.append(bullet)
                    bullet_sound.play()

            if event.type == red_hit:
                red_health -= 1
                explosion_sound.play()
            
            if event.type == blue_hit:
                blue_health -= 1
                explosion_sound.play()
                
        winner = ""        
        if blue_health <=0:
            winner = "Red Wins!"
        
        if red_health <= 0:
            winner = "Blue Wins!"
        
        if winner != "":
            draw_winner(winner)
            break
       
        keys_pressed = pygame.key.get_pressed()
        blue_movement(keys_pressed, blue)
        red_movement(keys_pressed, red)
        handle_bullets(blue_bullets, red_bullets, blue, red)
        draw_window(blue, red, blue_bullets, red_bullets, blue_health, red_health)

    main()


if __name__ == "__main__":
    main()
