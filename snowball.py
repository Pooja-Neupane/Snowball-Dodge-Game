import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("❄️ Snowball Dodge Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
DARK = (0, 0, 50)
RED = (255, 0, 0)

# Font
FONT = pygame.font.SysFont("comicsans", 40)

# Clock
clock = pygame.time.Clock()


class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 30
        self.speed = 8

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(SCREEN, BLUE, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Snowball:
    def __init__(self):
        self.radius = random.randint(15, 30)
        self.x = random.randint(0, WIDTH - self.radius)
        self.y = -self.radius
        self.speed = random.randint(3, 7)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def draw(self):
        pygame.draw.circle(SCREEN, WHITE, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def reset(self):
        self.__init__()


class Game:
    def __init__(self):
        self.player = Player()
        self.snowballs = [Snowball() for _ in range(7)]
        self.running = True
        self.score = 0

    def draw_ui(self):
        score_text = FONT.render(f"Score: {self.score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

    def game_over(self):
        text = FONT.render("Game Over! ❌", True, RED)
        SCREEN.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)

    def run(self):
        while self.running:
            clock.tick(60)
            SCREEN.fill(DARK)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.move(keys)
            self.player.draw()

            for ball in self.snowballs:
                ball.fall()
                ball.draw()
                if ball.get_rect().colliderect(self.player.get_rect()):
                    self.game_over()
                    self.running = False
                elif ball.y > HEIGHT:
                    self.score += 1

            self.draw_ui()
            pygame.display.update()

        pygame.quit()
        sys.exit()


# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
