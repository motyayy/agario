from pygame import *
from math import *
from random import randint

class Ball:
    def __init__(self, x, y, radius, color, speed=0):
        self.speed=speed
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.scale = 1

    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.y -= self.speed
        if keys[K_DOWN]:
            self.y += self.speed
        if keys[K_LEFT]:
            self.x -= self.speed
        if keys[K_RIGHT]:
            self.x += self.speed

    def reset(self):
        self.scale = max(0.3, min(50 / self.radius, 1.5))

        player_screen_radius = int(self.radius * self.scale)
        draw.circle(window, self.color, (size[0] // 2, size[1] // 2), player_screen_radius)
        draw.circle(window, self.color, (self.x, self.y),self.radius)

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)

init()

size = 500, 500

window = display.set_mode(size)
display.set_caption("Agario")
clock = time.Clock()

bg = image.load('15796580-agario-android-title-screen.png')
bg = transform.scale(bg, size)

ball = Ball(300, 300, 25, (255, 100, 255), speed=5)

f = font.Font(None, 50)
running = True
lose = False

cells = [Ball(randint(-2000, 2000), randint(-2000, 2000), 10,(randint(50, 220), randint(50, 220))) for _ in range(300)]

while running:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill((40, 40, 60))

    to_remove = []
    for cell in cells:
        if cell.collidecircle(ball):
            to_remove.append(cell)
            ball.radius += int(cell.radius * 0.2)
        else:
            sx = int((cell.x - ball.x) * ball.scale + size[0] // 2)
            sy = int((cell.y - ball.y) * ball.scale + size[1] // 2)

            cell_radius = int(cell.radius * ball.scale)
            draw.circle(window, cell.color, (sx, sy), cell_radius)

    for cell in to_remove:
        cells.remove(cell)

    if not lose:
        ball.reset()


    if lose:
        t = f.render("You lose!", 1, (244, 0, 0))
        window.blit(t, (400, 500))



    display.update()
    clock.tick(60)

    if not lose:
        ball.move


