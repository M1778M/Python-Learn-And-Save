import pygame as pg
import time
pg.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pg.display.set_caption("MyGame")
gameDisplay = pg.display.set_mode((500,500))
pg.display.update()
end = False

while not end:
    for event in pg.event.get():
        print(event)
        if event.type == pg.QUIT:
            end = True

    gameDisplay.fill(white)
    #1
    gameDisplay.fill(red,rect=[200,200,250,100])
    #2
    pg.draw.rect(gameDisplay,black,[10,10,100,100])

    pg.display.update()
pg.quit()
exit()
