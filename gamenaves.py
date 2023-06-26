import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
window_width = 800
window_height = 600

# Crear la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Naves")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Clase para la nave
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")  # Cargar imagen de la nave
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width // 2
        self.rect.bottom = window_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window_width:
            self.rect.right = window_width

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Clase para el proyectil de la nave
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png")  # Cargar imagen del proyectil
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# Clase para los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")  # Cargar imagen del enemigo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > window_height:
            self.rect.x = random.randint(0, window_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(1, 3)

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Crear la nave del jugador
ship = Ship()
all_sprites.add(ship)

# Crear enemigos
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Reloj para controlar la velocidad de actualización del juego
clock = pygame.time.Clock()

# Variables para el juego
game_over = False

# Bucle principal del juego
while not game_over:
    # Procesar eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                ship.speed_x = 5
            elif event.key == pygame.K_SPACE:
                ship.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.speed_x = 0

    # Actualizar elementos del juego
    all_sprites.update()

    # Comprobar colisiones entre proyectiles y enemigos
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Comprobar colisiones entre nave y enemigos
    if pygame.sprite.spritecollide(ship, enemies, False):
        game_over = True

    # Limpiar pantalla
    window.fill(black)

    # Dibujar todos los sprites en la pantalla
    all_sprites.draw(window)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización del juego
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
