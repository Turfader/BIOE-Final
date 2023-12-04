import package_installer
import pygame
from pygame import gfxdraw


def put_pixel(color, x, y, screen) -> None:
    gfxdraw.pixel(screen, x, y, color)


def paint() -> None:  # Keep this the last function above main
    # gamestate variables here
    done: bool = False
    pixel_locations: set = set()  # You should append tuples of (x_pos, y_pos, (r, g, b), radius)
    mouse_down: bool = False
    radius: int = 0  # set default to one pixel
    color: tuple[int, int, int] = (0, 0, 0)  # set default to black

    # pygame init stuff here
    pygame.init()
    size = (400, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyPaint")
    clock = pygame.time.Clock()

    # paints the screen white at the start
    screen.fill([255, 255, 255])

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                # screen clear
                if event.key == pygame.K_c:
                    screen.fill([255, 255, 255])  # when c is pressed, fill the screen with white
                    pixel_locations = set()  # clear existing pixel locations

                # screenshot
                if event.key == pygame.K_s and pygame.K_LSHIFT:
                    pygame.image.save(screen, "./screenshot.png")

                # color
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # sets color to red
                if event.key == pygame.K_g:
                    color = (0, 255, 0)  # sets color to green
                if event.key == pygame.K_u:  # uses u for blue and b for black
                    color = (0, 0, 255)  # sets color to blue
                if event.key == pygame.K_b:
                    color = (0, 0, 0)  # sets color to black
                if event.key == pygame.K_w:
                    color = (255, 255, 255)  # sets color to white

                # size
                if event.key == pygame.K_1:
                    radius = 1
                if event.key == pygame.K_2:
                    radius = 2
                if event.key == pygame.K_3:
                    radius = 3
                if event.key == pygame.K_4:
                    radius = 4
                if event.key == pygame.K_5:
                    radius = 5
                if event.key == pygame.K_6:
                    radius = 6
                if event.key == pygame.K_7:
                    radius = 7
                if event.key == pygame.K_8:
                    radius = 8
                if event.key == pygame.K_9:
                    radius = 9
                if event.key == pygame.K_0:
                    radius = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    # print("Left Mouse button was clicked")
                    mouse_down = True
                if mouse_presses[1]:
                    # print("middle scroll wheel was pressed down")
                    pass
                if mouse_presses[2]:
                    # print("Right Mouse button was clicked"")
                    pass

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            if mouse_down:
                x, y = pygame.mouse.get_pos()
                pixel_locations.add((x, y, color, radius))
                # TODO add code to add to pixel locations as shown in discord


                # TODO remove this code as shown in discord (until line 142)

            # TODO add code as shown in the discord
            for location in pixel_locations:
                if location[3] == 0:
                    put_pixel(location[2], location[0], location[1], screen)

                else:
                    pygame.draw.circle(screen, location[2], (location[0], location[1]), location[3])
            pygame.display.flip()
            clock.tick(30)  # limits frames to 30 fps
    pygame.quit()


if __name__ == "__main__":
    paint()
    print("exiting")
    quit(0)
