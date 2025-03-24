import pygame

pygame.init()

# укажем размер окна
WIDTH = 800
HEIGHT = 600

# создадим окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# координаты круга
x = 50
y = 50

# Создадим переменные для изменеия скорости координат
speed_x = 5
speed_y = 5

# радиус круга
r = 40

# цвет круга
red = (255, 0, 0)

# цвет фона
blue = (0, 0, 255)

#Загружаем картинку

sprite_sheet = pygame.image.load("1.png").convert_alpha()

#Создаем список и закидываем в него картинки
# Добавляем модуль pygame.SRCALPHA
sprites = []
for i in range(sprite_sheet.get_width()//12):
    surface = pygame.Surface((50, 50), pygame.SRCALPHA)
    rect = pygame.Rect(i *80 + 15 , 15 , 60, 60)
    surface.blit(sprite_sheet, (0, 0), rect)
    sprites.append(surface)

# Создаем переменную для анамирования картинки
animation_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += speed_x
    y += speed_y

    # Допишем программу, чтобы шарик не уходил за рамки экрана
    if x > WIDTH - r or x < r:
        speed_x = speed_x * -1
    if y > HEIGHT - r or y < r:
        speed_y = speed_y * -1
 
    # Зарисовываем круги синим цветом
    screen.fill((blue))

    # Работаем с анимацией
    animation_count += 1
    animation_count = animation_count % 11

    # Рисуем картинку по середине
    screen.blit(sprites[animation_count], (x, HEIGHT / 2))
    # нарисуем круг
    pygame.draw.circle(screen, red, (x, y), r)
    
    pygame.display.update()
    pygame.time.delay(100)
