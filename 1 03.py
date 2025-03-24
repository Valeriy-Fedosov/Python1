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
speed_x = 1
speed_y = 1

# цвет фона
blue = (0, 0, 255)

#Загружаем картинку

sprite_sheet = pygame.image.load("1.png")

#Создаем список и закидываем в него картинки
# Добавляем модуль pygame.SRCALPHA

"""
pygame.Surface - поверхности в Pygame используются
для представления внешнего вида объекта и его положения на экране. 
"""

"""
pygame.SRCALPHA — это флаг, который указывает на то,
что поверхность имеет альфа-канал для прозрачности
"""

sprites = []
for i in range(sprite_sheet.get_width()//12):
    surface = pygame.Surface((50, 50), pygame.SRCALPHA)
    rect = pygame.Rect(i *80 + 15, 15 , 60, 60)
    surface.blit(sprite_sheet, (0, 0), rect)
    sprites.append(surface)


sprites_1 = []
for i in range(7):
    surface = pygame.Surface((80, 50), pygame.SRCALPHA)
    rect1 = pygame.Rect(i *80 + 5 , 95 , 100, 60)
    surface.blit(sprite_sheet, (0, 0), rect1)
    sprites_1.append(surface)

sprites_2 = []
for i in range(11):
    surface = pygame.Surface((85, 50), pygame.SRCALPHA)
    rect2 = pygame.Rect(i *80 + 5 , 175 , 100, 60)
    surface.blit(sprite_sheet, (0, 0), rect2)
    sprites_2.append(surface)

# Создаем переменную для анамирования картинки
animation_count = 0
animation_count_1 = 0
animation_count_2 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += speed_x
    y += speed_y

    # Допишем программу, чтобы шарик не уходил за рамки экрана
    if x > WIDTH - 50 or x < 50:
        speed_x = speed_x * -1
    if y > HEIGHT - 50 or y < 50:
        speed_y = speed_y * -1
 
    # Зарисовываем круги синим цветом
    screen.fill((blue))

    # Работаем с анимацией
    animation_count += 1
    animation_count = animation_count % 11
    animation_count_1 += 1
    animation_count_1 = animation_count_1 % 7
    animation_count_2 += 1
    animation_count_2 = animation_count_2 % 11

    # нарисуем круг
#    pygame.draw.circle(screen, red, (x, y), r)
    

    # Рисуем картинку по середине
    screen.blit(sprites[animation_count], (x, HEIGHT / 2))
    screen.blit(sprites_1[animation_count_1], (x, 100))
    screen.blit(sprites_2[animation_count_2], (x, 400))
    
    pygame.display.update()
    pygame.time.delay(30)
