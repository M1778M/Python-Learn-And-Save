import pygame as pg
import random

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)



display_width = 800
display_height = 600

pg.display.set_caption("MyGame")


gameDisplay = pg.display.set_mode((display_width, display_height))

pg.display.update()


clock = pg.time.Clock()


block_size = 10

FPS = 30

font = pg.font.SysFont(None,25)

def msg_error_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[int(display_width/4),int(display_height/4)])


def gameloop():
    end = False
    gameover = False
    let_x = display_width / 2

    let_y = display_height / 2

    let_c_change = 0

    let_y_change = 0

    randPointX = random.randrange(0,display_width-block_size)
    randPointY = random.randrange(0, display_height-block_size)

    while not end:

        while gameover == True:
            gameDisplay.fill(white)
            msg_error_screen("Game Over, press space to play again or press Q for Exit.",red)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        gameloop()
                    if event.key == pg.K_q:
                        end = True
                        gameover = False


        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                let_c_change = -block_size
                let_y_change = 0
            elif event.key == pg.K_RIGHT:
                let_c_change = block_size
                let_y_change = 0
            elif event.key == pg.K_UP:
                let_y_change = -block_size
                let_c_change = 0
            elif event.key == pg.K_DOWN:
                let_y_change = block_size
                let_c_change = 0

        if let_x >= display_width or let_x < 0 or let_y >= display_height or let_y < 0:
            gameover = True

        let_x += let_c_change
        let_y += let_y_change
        gameDisplay.fill(white)

        pg.draw.rect(gameDisplay,red,[randPointX,randPointY,block_size,block_size])
        pg.draw.rect(gameDisplay, black, [int(let_x), int(let_y), block_size, block_size])

        pg.display.update()
        clock.tick(FPS)



    pg.quit()
    exit()

gameloop()