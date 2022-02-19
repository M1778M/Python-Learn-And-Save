import pygame as pg
import time

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)



display_width = 800
display_height = 600

pg.display.set_caption("MyGame")


gameDisplay = pg.display.set_mode((display_width, display_height))

pg.display.update()

end = False


let_x = display_width/2

let_y = display_height/2

let_c_change = 0

let_y_change = 0

clock = pg.time.Clock()


block_size = 10

FPS = 30

font = pg.font.SysFont(None,25)

def msg_error_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[int(display_width/2),int(display_height/2)])

while not end:
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
        end = True

    let_x += let_c_change
    let_y += let_y_change
    gameDisplay.fill(white)

    pg.draw.rect(gameDisplay, black, [int(let_x), int(let_y), block_size, block_size])

    pg.display.update()
    clock.tick(FPS)

msg_error_screen("You lose!",red)
pg.display.update()
time.sleep(3)
pg.quit()
exit()
