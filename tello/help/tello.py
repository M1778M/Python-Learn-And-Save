import easytello as tello
import keyboard as kb

tl = tello.Tello()

speed = 30

while True:
    input = kb.read_key()

    if input == 'enter':
        tl.takeoff()
    elif input == 'w':
        tl.forward(speed)
    elif input == 's':
        tl.back(speed)
    elif input == 'd':
        tl.cw(speed)
    elif input == 'a':
        tl.ccw(speed)
    elif input == 'space':
        tl.land()
    elif input == 'up':
        tl.up(speed)
    elif input == 'down':
        tl.down(speed)
    elif input == 'right':
        tl.right(speed)
    elif input == 'left':
        tl.left(speed)
    elif input == 'q':
        tl.land()
        break
    else:
        print('\a')
