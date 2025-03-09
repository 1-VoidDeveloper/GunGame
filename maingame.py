import pygame
import random
import math
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Shooter Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_x, player_y = WIDTH // 2, HEIGHT - 50
player_speed = 5
bullets = []
bullet_speed = 7
enemies = []
enemy_speed = 2
spawn_rate = 30
frame_count = 0
score = 0
errors = 0  # Numărul de greșeli
font = pygame.font.Font(None, 36)

def draw_3d_rect(x, y, size, depth, color):
    offset = depth * 2
    pygame.draw.polygon(screen, color, [(x, y), (x + size, y), (x + size - offset, y + size), (x - offset, y + size)])

def draw_player(x, y):
    draw_3d_rect(x, y, 50, 10, BLUE)

def draw_enemy(x, y):
    draw_3d_rect(x, y, 50, 10, RED)

def draw_bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, 5, 10))

def draw_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def draw_errors():
    error_text = font.render(f"Errors: {errors}", True, (0, 0, 0))
    screen.blit(error_text, (WIDTH - 150, 10))

def draw_winner():
    winner_text = font.render("You Win!", True, (0, 255, 0))
    screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2))

def draw_game_over():
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[K_SPACE]:
        bullets.append([player_x + 25, player_y])

    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    frame_count += 1
    if frame_count % spawn_rate == 0:
        enemies.append([random.randint(0, WIDTH - 50), 0])

    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            errors += 1  # Crește numărul de greșeli când un inamic ajunge la fund

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if enemy[0] < bullet[0] < enemy[0] + 50 and enemy[1] < bullet[1] < enemy[1] + 50:
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    if score >= 1000:  # Condiția de câștig
        draw_winner()
        pygame.display.flip()
        pygame.time.delay(2000)  # Afișează "You Win!" 2 secunde
        break  # Oprește jocul

    if errors >= 15:  # Condiția de Game Over
        draw_game_over()
        pygame.display.flip()
        pygame.time.delay(2000)  # Afișează "Game Over!" 2 secunde
        break  # Oprește jocul

    draw_player(player_x, player_y)

    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    draw_score()
    draw_errors()

    pygame.display.flip()

pygame.quit()
