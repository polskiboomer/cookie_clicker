alien = Actor('alien')

alien.topleft = 0, 0
print(alien.height)
print(alien.width)

WIDTH = alien.width
HEIGHT = alien.height-40

def draw():
    screen.clear()
    alien.draw()