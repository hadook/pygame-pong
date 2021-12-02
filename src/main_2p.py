import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_speed_x *= -1


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


def p1_animation():
    p1.y += p1_speed
    if p1.top <= 0:
        p1.top = 0
    if p1.bottom >= screen_height:
        p1.bottom = screen_height


def p2_animation():
    p2.y += p2_speed
    if p2.top <= 0:
        p2.top = 0
    if p2.bottom >= screen_height:
        p2.bottom = screen_height


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
p1 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
p2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
p1_color = pygame.Color('INDIANRED')
p2_color = pygame.Color('CORNFLOWERBLUE')
light_grey = (200, 200, 200)

ball_speed_x = 10 * random.choice((-1, 1))
ball_speed_y = 10 * random.choice((-1, 1))
p1_speed = 0
p2_speed = 0

while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p2_speed += 7
            if event.key == pygame.K_UP:
                p2_speed -= 7
            if event.key == pygame.K_a:
                p1_speed -= 7
            if event.key == pygame.K_z:
                p1_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                p2_speed = 0
            if event.key == pygame.K_a or event.key == pygame.K_z:
                p1_speed = 0

    ball_animation()
    p1_animation()
    p2_animation()

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, p1_color, p1)
    pygame.draw.rect(screen, p2_color, p2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # updating the window
    pygame.display.flip()
    clock.tick(60)
