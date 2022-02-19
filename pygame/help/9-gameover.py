import pygame as pg
import random

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,155,0)


display_width = 800
display_height = 600

pg.display.set_caption("MyGame")


gameDisplay = pg.display.set_mode((display_width, display_height))

pg.display.update()


clock = pg.time.Clock()


block_size = 11

FPS = 20

smfont = pg.font.SysFont("consolas",25)
nmfont = pg.font.SysFont("consolas",50)
lgfont = pg.font.SysFont("consolas",80)

def snake(block_size,snakelist,let_x,let_y):
    for XnY in snakelist:
        pg.draw.rect(gameDisplay, green, [int(let_x), int(let_y), block_size, block_size])

def text_object(text,color,size):
    if size == "small":
        textS = smfont.render(text,True,color)
    elif size == "normal":
        textS = nmfont.render(text, True, color)
    elif size == "large":
        textS = lgfont.render(text, True, color)
    return textS,textS.get_rect()


def msg_error_screen(msg,color,y_dis =0,size = "small"):
    textS,textR = text_object(msg,color,size)
    textR.center = [int(display_width/2),int(display_height/2) + y_dis]
    gameDisplay.blit(textS,textR)




def gameloop():
    end = False
    gameover = False
    let_x = display_width / 2

    let_y = display_height / 2

    let_c_change = 0

    let_y_change = 0
    snakelist = []

    snakeleg = 1

    randPointX = round(random.randrange(0,display_width-block_size)/10.0*10)
    randPointY = round(random.randrange(0, display_height-block_size)/10.0*10)

    while not end:

        while gameover == True:
            gameDisplay.fill(white)
            msg_error_screen("Game Over",red,-50,size="normal")
            msg_error_screen("Press Space To Play Again Or Press Q For Exit",black)
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

        snakehead = []
        snakehead.append(let_x)
        snakehead.append(let_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakeleg:
            del snakelist[0]


        for i in snakelist[:-1]:
            if i == snakehead:
                gameover = True

        pg.draw.rect(gameDisplay,red,[randPointX,randPointY,block_size,block_size])
        snake(block_size,snakelist,let_x,let_y)


        pg.display.update()

        if let_x == randPointX or let_x == randPointX - 1 or let_x == randPointX - 2 or let_x == randPointX + 1 or let_x == randPointX + 2 and let_y == randPointY or let_y == randPointY - 1 or let_y == randPointY - 2 or let_y == randPointY + 1 or let_y == randPointY + 2:
            randPointX = round(random.randrange(0, display_width - block_size) / 10.0 * 10)
            randPointY = round(random.randrange(0, display_height - block_size) / 10.0 * 10)
            snakeleg += 1

        clock.tick(FPS)



    pg.quit()
    exit()

gameloop()