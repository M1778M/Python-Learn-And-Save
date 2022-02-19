import pygame as pg
import time

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pg.display.set_caption("MyGame")
gameDisplay = pg.display.set_mode((800, 500))
pg.display.update()
end = False

let_x = 200
let_y = 200
let_c_change = 0
let_y_change = 0
clock = pg.time.Clock()

while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            let_c_change = -10
            let_y_change = 0
        elif event.key == pg.K_RIGHT:
            let_c_change = 10
            let_y_change = 0
        elif event.key == pg.K_UP:
            let_y_change = -10
            let_c_change = 0
        elif event.key == pg.K_DOWN:
            let_y_change = 10
            let_c_change = 0

    if let_x >= 800 or let_x < 0 or let_y >= 500 or let_y < 0:
        end = True

    let_x += let_c_change
    let_y += let_y_change
    gameDisplay.fill(white)

    pg.draw.rect(gameDisplay, black, [let_x, let_y, 10, 10])

    pg.display.update()
    clock.tick(10)
pg.quit()
exit()
