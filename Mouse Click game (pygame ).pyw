import pygame
import random
import math

pygame.init()

# Tam ekran modunda pencere aç
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Mouse click game")

# Yazı ayarı - büyük font
font = pygame.font.SysFont(None, 100)

click_count = 0

def draw_parametric_image(surface, seed):
    random.seed(seed)
    # Arka plan rengi yumuşak beyaz ton
    base_r = random.randint(50, 255)
    base_g = random.randint(50, 255)
    base_b = random.randint(50, 255)
    bg_color = (255 - base_r//2, 255 - base_g//2, 255 - base_b//2)
    surface.fill(bg_color)

    center_x, center_y = WIDTH // 2, HEIGHT // 2

    circle_count = 5 + (seed % 10)
    max_radius = min(WIDTH, HEIGHT) // 3

    for i in range(circle_count):
        radius = max_radius - i * (max_radius // circle_count)
        color_variation = ((base_r + i*20) % 256, (base_g + i*30) % 256, (base_b + i*40) % 256)
        pygame.draw.circle(surface, color_variation, (center_x, center_y), radius, width=5)

    line_count = 10 + (seed % 20)
    base_color = (base_r, base_g, base_b)
    for i in range(line_count):
        angle = (i * 2 * math.pi / line_count) + (seed % 360) * math.pi / 180
        length = max_radius
        x_end = int(center_x + length * math.cos(angle))
        y_end = int(center_y + length * math.sin(angle))
        pygame.draw.line(surface, base_color, (center_x, center_y), (x_end, y_end), 3)

    pygame.draw.circle(surface, base_color, (center_x, center_y), 40)

    eye_radius = 8
    eye_x_offset = 15
    eye_y_offset = 10

    pygame.draw.circle(surface, (255, 255, 255), (center_x - eye_x_offset, center_y - eye_y_offset), eye_radius)
    pygame.draw.circle(surface, (255, 255, 255), (center_x + eye_x_offset, center_y - eye_y_offset), eye_radius)

    pygame.draw.circle(surface, (0, 0, 0), (center_x - eye_x_offset, center_y - eye_y_offset), eye_radius//2)
    pygame.draw.circle(surface, (0, 0, 0), (center_x + eye_x_offset, center_y - eye_y_offset), eye_radius//2)

    mouth_rect = pygame.Rect(center_x - 20, center_y + 10, 40, 20)
    pygame.draw.arc(surface, (0, 0, 0), mouth_rect, 3.14, 0, 3)

def draw_click_text(surface, count):
    text = font.render(f"Click: {count}", True, (0, 0, 0))
    rect = text.get_rect(center=(WIDTH // 2, 80))
    surface.blit(text, rect)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sol tık
                click_count += 1

    draw_parametric_image(screen, click_count)
    draw_click_text(screen, click_count)

    pygame.display.flip()
    clock.tick(60)
