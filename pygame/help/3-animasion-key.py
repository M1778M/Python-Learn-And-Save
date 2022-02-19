import pygame as pg
import time

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pg.display.set_caption("MyGame")
gameDisplay = pg.display.set_mode((500, 500))
pg.display.update()
end = False

let_x = 200
let_y = 200
let_c_change = 0
clock = pg.time.Clock()

while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            let_c_change -= 10
        if event.key == pg.K_RIGHT:
            let_c_change += 10

    let_x += let_c_change
    gameDisplay.fill(white)

    pg.draw.rect(gameDisplay, black, [let_x, let_y, 100, 100])

    pg.display.update()
    clock.tick(10)
pg.quit()
exit()
