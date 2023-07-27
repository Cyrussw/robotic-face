import pygame
import sys
import time
import os
import platform
import psutil


def set_process_priority(priority):
    if platform.system() == "Windows":
        current_process = psutil.Process(os.getpid())
        current_process.nice(priority)


pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 400, 200  # Updated width and height

# Ekranın genişlik ve yükseklik değerlerini al
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Renkler
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Açık Mavi Renk
RED = (255, 0, 0)

# Hedeflenen pencere pozisyonunu hesapla
window_x = SCREEN_WIDTH - WIDTH
window_y = 0

# Pencere oluştur ve ekranın hedeflenen pozisyonunda başlat
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_x},{window_y}"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sairus')  # Set the new caption to 'Sairus'


def draw_robot_face(eye_color, eyebrow_color, dead=False):
    # Arka planı siyah yap
    screen.fill(BLACK)

    # Gözleri çiz
    pygame.draw.rect(screen, eye_color, pygame.Rect(
        100, 70, 80, 60))
    pygame.draw.rect(screen, eye_color, pygame.Rect(
        220, 70, 80, 60))
    # Kaşları çiz
    pygame.draw.rect(screen, eyebrow_color, pygame.Rect(
        100, 50, 80, 20))
    pygame.draw.rect(screen, eyebrow_color, pygame.Rect(
        220, 50, 80, 20))

    # Ölme durumunda kırmızı X çiz
    if dead:
        pygame.draw.line(screen, RED, (100, 70), (180, 130),
                         5)
        pygame.draw.line(screen, RED, (100, 130), (180, 70),
                         5)
        pygame.draw.line(screen, RED, (220, 70), (300, 130),
                         5)
        pygame.draw.line(screen, RED, (220, 130), (300, 70),
                         5)

    pygame.display.flip()


def animation_idle():
    # Boşta bekleme animasyonu
    for _ in range(3):
        draw_robot_face(LIGHT_BLUE, BLACK)
        time.sleep(0.5)
        draw_robot_face(BLACK, BLACK)
        time.sleep(0.5)


def animation_angry():
    # Sinirlenme animasyonu
    for _ in range(5):
        draw_robot_face(RED, LIGHT_BLUE)
        time.sleep(0.2)
        draw_robot_face(LIGHT_BLUE, BLACK)
        time.sleep(0.2)


def animation_spin():
    # Baş dönme animasyonu
    for _ in range(36):  # 36 kademe ile 10 tur dönüş
        screen.fill(BLACK)
        rotated_image = pygame.transform.rotate(eye_surface, _ * 10)
        screen.blit(rotated_image, (250, 250))
        screen.blit(rotated_image, (450, 250))
        pygame.display.flip()
        time.sleep(0.1)


def animation_dead():
    # Ölme animasyonu
    for i in range(3):
        # Gözler kırmızı X ile çiziliyor
        draw_robot_face(LIGHT_BLUE, BLACK, True)
        time.sleep(0.3)
        draw_robot_face(BLACK, BLACK)  # Gözler ve kaşlar siyah ile çiziliyor
        time.sleep(0.3)


def animation_happy():
    # Sevilme/Mutlu olma animasyonu
    for _ in range(5):
        draw_robot_face(LIGHT_BLUE)
        time.sleep(0.2)
        draw_robot_face(BLACK)
        time.sleep(0.2)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    animation_idle()
                elif event.key == pygame.K_2:
                    animation_angry()
                elif event.key == pygame.K_3:
                    animation_spin()
                elif event.key == pygame.K_4:
                    animation_dead()
                elif event.key == pygame.K_5:
                    animation_happy()


if __name__ == "__main__":
    # You can try different constants here
    priority_level = psutil.HIGH_PRIORITY_CLASS
    set_process_priority(priority_level)

    eye_surface = pygame.Surface((100, 100))
    eye_surface.fill(LIGHT_BLUE)
    main()
