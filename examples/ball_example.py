import pygame, sys

board_size = width, height = 500, 500
speed = [2,3]

def main():
    pygame.init()
    screen = pygame.display.set_mode(board_size)
    ball = pygame.image.load("graphics/img/beach_ball.gif")
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill((0,0,0))
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
