import package_installer
import pygame
from pygame import gfxdraw


def put_pixel(color, x, y, screen) -> None:
    gfxdraw.pixel(screen, x, y, color)


def paint() -> None:  # Keep this the last function above main
    # gamestate variables here
    done: bool = False
    pixel_locations: set = set()  # You should append tuples of (x_pos, y_pos, (r, g, b))
    mouse_down: bool = False

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
                if event.key == pygame.K_c:
                    screen.fill([255, 255, 255])  # when c is pressed, fill the screen with white
                    pixel_locations = set()  # clear existing pixel locations
                if event.key == pygame.K_c and pygame.K_LSHIFT:
                    pygame.image.save(screen, "./screenshot.png")

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
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    # print("Left Mouse button was released")
                    mouse_down = False
                if mouse_presses[1]:
                    # print("middle scroll wheel was released")
                    pass
                if mouse_presses[2]:
                    # print("Right Mouse button was released"")
                    pass

            if mouse_down:
                x, y = pygame.mouse.get_pos()

                draw_on = False
                last_pos = (0, 0)

                radius = 5
                # todo: refactor the below code to follow existing conventions
                # make sure that it saves each location to the set pixel_locations and then
                # draws them at the location dictated by the todo
                def line(canvas, color, start, end, radius=1):
                    Xaxis = end[0] - start[0]
                    Yaxis = end[1] - start[1]
                    dist = max(abs(Xaxis), abs(Yaxis))
                    for i in range(dist):
                        x = int(start[0] + float(i) / dist * Xaxis)
                        y = int(start[1] + float(i) / dist * Yaxis)
                        pygame.draw.circle(canvas, color, (x, y), radius)

                try:
                    while True:
                        event = pygame.event.wait()

                        if event.type == pygame.QUIT:
                            raise StopIteration

                        if event.type == pygame.MOUSEBUTTONDOWN:

                            color = ([0,0,0])

                            pygame.draw.circle(screen, color, event.pos, radius)
                            draw_on = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            draw_on = False
                        if event.type == pygame.MOUSEMOTION:
                            if draw_on:
                                pygame.draw.circle(screen, color, event.pos, radius)
                                line(screen, color, event.pos, last_pos, radius)
                            last_pos = event.pos
                        pygame.display.flip()

                except StopIteration:
                    pass
                # TODO add code that records the mouse position and color into the array

            # TODO add code to update the screen with what has been drawn
            # I would advise iterating over a for loop and calling the put_pixel function
            # you should be able to do this in one line. Give it a try if you can!
            # i.e. function that draws stuff according to the array
            pygame.display.flip()
            clock.tick(30)  # limits frames to 30 fps
    pygame.quit()


if __name__ == "__main__":
    paint()
    print("exiting")
    quit(0)
