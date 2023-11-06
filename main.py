import pygame
import time
import random
 
pygame.init()
 
white = (240, 240, 240)
black = (0, 0, 0)
red = (213, 0, 0)
green = (0, 200, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snakerect = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)
 
 
def my_score(score, snake_speed):
    value = score_font.render("Ваш счёт и скорость: " + str(score) + ' ' + str(snake_speed), True, black)
    dis.blit(value, [0, 0])
 
 
 
def my_snake(snakerect, snakesss):
    for i in snakesss:
        pygame.draw.rect(dis, green, [i[0], i[1], snakerect, snakerect])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_end = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    xspeed = 0
    yspeed = 0
 
    snakesss = []
    snake_speed = 10
    snakesize = 1
    dif = 1
 
    eatw = round(random.randrange(0, dis_width - snakerect) / 10.0) * 10.0
    eath = round(random.randrange(0, dis_height - snakerect) / 10.0) * 10.0
 
    while not game_over:
 
        while game_end == True:
            dis.fill(white)
            message("R- сыграть заново, Q-выйти", red)
            my_score(snakesize - 1, snake_speed)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_r:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and xspeed != snakerect:
                    xspeed = -snakerect
                    yspeed = 0
                elif event.key == pygame.K_RIGHT and xspeed != -snakerect:
                    xspeed = snakerect
                    yspeed = 0
                elif event.key == pygame.K_UP and yspeed != snakerect:
                    yspeed = -snakerect
                    xspeed = 0
                elif event.key == pygame.K_DOWN and yspeed != -snakerect:
                    yspeed = snakerect
                    xspeed = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_end = True
        x1 += xspeed
        y1 += yspeed
        dis.fill(white)
        pygame.draw.rect(dis, red, [eatw, eath, snakerect, snakerect])
        ebalo = []
        ebalo.append(x1)
        ebalo.append(y1)
        snakesss.append(ebalo)
        if len(snakesss) > snakesize:
            del snakesss[0]
 
        for x in snakesss[:-1]:
            if x == ebalo:
                game_end = True
 
        my_snake(snakerect, snakesss)
        my_score(snakesize - 1, snake_speed)
 
        pygame.display.update()
 
        if x1 == eatw and y1 == eath:
            eatw = round(random.randrange(0, dis_width - snakerect) / 10.0) * 10.0
            eath = round(random.randrange(0, dis_height - snakerect) / 10.0) * 10.0
            snakesize += 1
            if snakesize - (dif * 5) == 0:
                dif += 1
                snake_speed += 5
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()