import package_installer
import pygame
from pygame import gfxdraw


def put_text(txt: str, x: int, y: int, color: tuple[int, int, int], screen) -> None:

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(txt, True, color)
    screen.blit(text, [x, y])  
    

def put_pixel(color, x, y, screen) -> None:
    gfxdraw.pixel(screen, x, y, color)


def paint() -> None:  # Keep this the last function above main
    # gamestate variables here
    done: bool = False
    pixel_locations: set = set()  # You should append tuples of (x_pos, y_pos, (r, g, b), radius)
    mouse_down: bool = False
    radius: int = 0  # set default to one pixel
    color: tuple[int, int, int] = (0, 0, 0)  # set default to black
    place_text: bool = False

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

                # textbox
                if event.key == pygame.K_t:
                    place_text = True

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
                if event.key == pygame.K_a: 
                    color = (192, 192, 192)  # sets color to gray 
                if event.key == pygame.K_l: 
                    color = (229, 184, 11)   # sets color to gold
                if event.key == pygame.K_p: 
                    color = (221, 160, 221)  # sets color to purple (plum) 
                if event.key == pygame.K_v:   
                    color = (127, 0, 255)  # sets color to violet
                if event.key == pygame.K_i: 
                    color = (75, 0, 130)  # sets color to indigo 
                if event.key == pygame.K_o: 
                    color = (255, 127, 0)  # sets color to orange 
                if event.key == pygame.K_y: 
                    color = (255, 255, 0)  # sets color to yellow 
                if event.key == pygame.K_n: 
                    color = (237, 166, 196)  # sets color to pink 
                if event.key == pygame.K_m: 
                    color = (68, 33, 18)  # sets color to brown
                if event.key == pygame.K_e:
                    color = (0, 155, 119)  # sets color to emerald green 
                if event.key == pygame.K_q: 
                    color = (181, 101, 29)  # sets color to light brown 
                if event.key == pygame.K_x: 
                    color = (67, 232, 216)  # sets color to turquoise 
                if event.key == pygame.K_f: 
                    color = (217, 2, 125)  # sets color to fuchsia
                if event.key == pygame.K_h: 
                    color = (156, 175, 136)  # sets color to sage green
                if event.key == pygame.K_j: 
                    color = (185, 162, 129)  # sets color to taupe brown 
                if event.key == pygame.K_z:
                    color = (144, 0, 32)  # sets color to burgundy 
                if event.key == pygame.K_k: 
                    color = (198, 81, 2)  # sets color to burnt orange 
                if event.key == pygame.K_d: 
                    color = (0, 0, 128)  # sets color to navy blue

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
                if place_text:
                    place_text = False
                    put_text(input("Input your text here:\n"), x, y, color, screen)
                else:
                    pixel_locations.add((x, y, color, radius))

            for location in pixel_locations:
                if location[3] == 0:
                    put_pixel(location[2], location[0], location[1], screen)

                else:
                    pygame.draw.circle(screen, location[2], (location[0], location[1]), location[3])

            pygame.display.flip()
            clock.tick()
    pygame.quit()


if __name__ == "__main__":
    paint()
    print("exiting")
    quit(0)
