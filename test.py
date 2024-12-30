import pygame
from pygame.time import get_ticks

# Lớp Timer như bạn đã định nghĩa
class Timer:
    def __init__(self, duration, func=None, repeat=False):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
        self.repeat = repeat

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                if self.func and self.start_time != 0:
                    self.func()
                self.deactivate()

# Hàm callback sẽ được gọi khi timer hết thời gian
def timer_done():
    print("Timer done!")

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Timer Test")

# Khởi tạo một đối tượng Timer với thời gian 2 giây
test_timer = Timer(2000, timer_done, repeat=True)
test_timer.activate()

# Vòng lặp game
running = True
clock = pygame.time.Clock()

while running:
    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật timer
    test_timer.update()

    # Vẽ màn hình
    screen.fill((0, 0, 0))  # Lấy màu đen làm nền
    pygame.display.flip()

    # Giới hạn FPS
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
