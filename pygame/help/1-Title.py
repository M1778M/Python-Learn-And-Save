import pygame as pg
import time
pg.init()


pg.display.set_caption("MyGame")
gameDisplay = pg.display.set_mode((500,500))
pg.display.update()
end = False

while not end:
    for event in pg.event.get():
        print(event)
        if event.type == pg.QUIT:
            end = True

pg.quit()
exit()