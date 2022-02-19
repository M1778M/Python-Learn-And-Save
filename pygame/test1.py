import pygame as pg
i = True

display = pg.display.init()

pg.display.set_mode((500,500))

pg.display.set_caption('Help')



while i:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                i = False
                pg.quit()
        if event.type == pg.QUIT:
            i = False
            pg.quit()