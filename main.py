import package_installer
import pygame
from pygame import gfxdraw
print('hello world')

def put_text(txt, x, y):

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(txt, True, [0, 0, 0])
    screen.blit(text, [x, y])  # shows an error. This should will not be an error at runtime


def put_pixel(color, x, y, screen):
    gfxdraw.pixel(screen, x, y, color)


def paint():  # Keep this the last function above main
    # gamestate  variables here
    done: bool = False

    # pygame init stuff here
    pygame.init()
    size = (400, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyPaint")
    clock = pygame.time.Clock()

    while not done:

        for event in pygame.event.get():

            # clears the screen with white
            screen.fill([255, 255, 255])

            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    # print("Left Mouse button was clicked")
                    pass
                if mouse_presses[1]:
                    # print("middle scroll wheel was pressed down")
                    pass
                if mouse_presses[2]:
                    # print("Right Mouse button was clicked"")
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    # print("Left Mouse button was released")
                    pass
                if mouse_presses[1]:
                    # print("middle scroll wheel was released")
                    pass
                if mouse_presses[2]:
                    # print("Right Mouse button was released"")
                    pass

            # add code to update screen here
            pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    paint()
    print("exiting")
    quit(0)

