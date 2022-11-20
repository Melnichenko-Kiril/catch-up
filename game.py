from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("road.png"), (700, 500))

font.init()

game_over = False

x1 = 190
y1 = 400
 
x2 = 410
y2 = 400

x3 = 300
y3 = 10

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite_2.png'), (100, 100))
sprite3 = transform.scale(image.load('prize.png'), (100, 100))
speed = 3

clock = time.Clock()

while game_over == False:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(sprite3, (x3, y3))

    for e in event.get():
        if e.type == QUIT:
            game_over = True

    sprite1_pressed = key.get_pressed()
    sprite2_pressed = key.get_pressed()

    if sprite1_pressed[K_a] and x1 > 5:
        x1 -= speed
    if sprite1_pressed[K_d] and x1 < 595:
        x1 += speed
    if sprite1_pressed[K_w] and y1 > 5:
        y1 -= speed
    if sprite1_pressed[K_s] and y1 < 395:
        y1 += speed

    if sprite2_pressed[K_LEFT] and x2 > 5:
        x2 -= speed
    if sprite2_pressed[K_RIGHT] and x2 < 595:
        x2 += speed
    if sprite2_pressed[K_UP] and y2 > 5:
        y2 -= speed
    if sprite2_pressed[K_DOWN] and y2 < 395:
        y2 += speed

    f1 = font.Font(None, 50)

    if x1 > 255 and x1 < 350 and y1 < 100:
        text1 = f1.render('Победил зеленый', True,(0, 255, 0))
        window.blit(text1, (200, 300))
        display.update()
        clock.tick(1)
        game_over = True

    if x2 > 255 and x2 < 350 and y2 < 100:
        text2 = f1.render('Победил белый', True,(255, 255, 255))
        window.blit(text2, (200, 300))
        display.update()
        clock.tick(1)
        game_over = True

    display.update()
    clock.tick(60)