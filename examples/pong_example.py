import pygame, sys

# Refactor into settings file
board_size = width, height = 500, 500
player_speed = [0,3]
fps = 60
game_name = "PONG"

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(board_size)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

    def run(self):
        # Event loop
        while True:
            self.__mainloop()

    def __mainloop(self):
        for event in pygame.event.get():
            self.__handle_event(event)
        self.screen.fill('black')
        pygame.display.update()
        self.clock.tick(fps)

    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
