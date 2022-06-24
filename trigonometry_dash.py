import pygame

draw_rect = False
map_scout = False

# initialize pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Trigonometry Dash")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


# The stage of the colour will change based on the number. Color Count counts how many times it has been changed.
# 0 = +green, 1 = -red, 2 = +blue, 3 = -green, 4 = +red, 5 = -blue
color_stage = 0
color_count = 0
color_change = 11.8


# background_img = pygame.image.load('')

class Ground:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blit(self):
        screen.blit(ground_img, (self.x, self.y))

    def move(self):
        self.x -= 10
        if self.x <= -340:
            self.x = 780


Ground_piece_1 = Ground(-35, 490)
Ground_piece_2 = Ground(270, 490)
Ground_piece_3 = Ground(565, 490)
Ground_piece_4 = Ground(870, 490)
ground_pieces = [Ground_piece_1, Ground_piece_2, Ground_piece_3, Ground_piece_4]


def set_ground_piece_starting_position():
    Ground_piece_1.x = -35
    Ground_piece_2.x = 270
    Ground_piece_3.x = 565
    Ground_piece_4.x = 870

ground_img = pygame.image.load('Platform.png')
character_img = pygame.image.load('Character.png')
high_quality_character_img = pygame.image.load("Drawing-2-2.png")
high_quality_character_img = pygame.transform.scale(high_quality_character_img, (400, 349))
platform_img = pygame.image.load('Obstacle_platform.png')
spike_img = pygame.image.load('spike.png')
spike_img = pygame.transform.scale(spike_img, (43, 38))
background_img = pygame.image.load('background.jpeg')
finish_wall_img = pygame.image.load("finish_wall.jpeg")
finish_wall_light_img = pygame.image.load("Finish_wall_light.png")
finish_wall_light_img = pygame.transform.scale(finish_wall_light_img, (700, 70))
finish_wall_light_img = pygame.transform.rotate(finish_wall_light_img, 90)
finish_wall_img = pygame.transform.scale(finish_wall_img, (700, 70))
finish_wall_img = pygame.transform.rotate(finish_wall_img, 90)


class Spike:

    def __init__(self, x, y, rect_top, rect_bottom):
        self.x = x
        self.y = y
        self.rect_bottom = rect_top
        self.rect_bottom = rect_bottom

    def move(self):
        self.x -= 10

    def blit(self):
        screen.blit(spike_img, (self.x, self.y))

    def update_rect(self):
        self.rect_top = pygame.Rect(self.x + 9, self.y, 25, 30)
        self.rect_bottom = pygame.Rect(self.x, self.y + 23, 43, 15)

def make_spike(x, y, amount_of_spikes):

    spike = Spike(x, y, pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0))
    spikes.append(spike)
    for t in range(amount_of_spikes - 1):
        spike = Spike(spike.x + 43, y, pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0))
        spikes.append(spike)

# spikes on top of a platform should be 10 greater in x, and 38 greater in y
spikes = []
def add_spikes_to_list():
    make_spike(1000, 452, 1)
    make_spike(1730, 452, 1)
    make_spike(3880, 240, 1)
    make_spike(5072, 101, 1)
    make_spike(2200, 452, 4)
    make_spike(2975, 452, 3)
    make_spike(3250, 452, 150)
    make_spike(5201, 126, 5)

class Platform:

    def __init__(self, x, y, image, rect, player_collide_platform_y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = rect
        self.player_collide_platform_y = player_collide_platform_y

    def move(self):
        self.x -= 10

    def blit(self):
        screen.blit(self.image, self.rect)

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 43, 43)

# ground is 450, and each is 43 tall. recommended distance for platform towers is 170.
# recommended distance for platform normal falls are x + 230 and y + 100


def make_spike_on_platform(x,y, amount_of_spike_on_platforms):
    platform = Platform(x, y, platform_img, pygame.Rect(0, y, 43, 43), 0)
    spike = Spike(x + 10, y - 38, pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0))
    platforms.append(platform)
    spikes.append(spike)
    for u in range(amount_of_spike_on_platforms - 1):
        platform = Platform(platform.x + 43, y, platform_img, pygame.Rect(0, y, 43, 43), 0)
        spike = Spike(platform.x, y - 38, pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0))
        platforms.append(platform)
        spikes.append(spike)

# always use the x and y of the first platform
def make_platform(x, y, amount_of_platforms):
    platform = Platform(x, y, platform_img, pygame.Rect(0, y, 43, 43), 0)
    platforms.append(platform)
    for i in range(amount_of_platforms - 1):
        platform = Platform(platform.x + 43, y, platform_img, pygame.Rect(0, y, 43, 43), 0)
        platforms.append(platform)

height = 43
platforms = []


def add_platforms_to_list():
    make_platform(1300, 450, 1)
    make_platform(1800, 450, 1)
    make_platform(1970, 450, 1)
    make_platform(1970, 407, 1)
    make_platform(2140, 450, 1)
    make_platform(2140, 407, 1)
    make_platform(2140, 364, 1)
    make_platform(2350, 364, 1)
    make_platform(3360, 407, 1)
    make_platform(3530, 364, 1)
    make_platform(3700, 321, 1)
    make_platform(3870, 278, 1)
    make_platform(3870, 407, 1)
    make_platform(4212, 364, 1)
    make_platform(4382, 321, 1)
    make_platform(4552, 278, 1)
    make_platform(4722, 235, 1)
    make_platform(4892, 192, 1)
    make_platform(5062, 139, 1)
    make_platform(2700, 450, 6)
    make_platform(3104, 450, 3)
    make_platform(3913, 407, 4)
    make_platform(5062, 250, 3)
    make_platform(5191, 293, 5)
    make_platform(5191, 164, 5)
    make_platform(5406, 270, 5)
    make_spike_on_platform(5680, 330, 5)
    make_platform(5680, 221, 7)
    make_spike_on_platform(5981, 221, 1)
    make_spike_on_platform(6024, 300, 1)
    make_platform(6067, 300, 5)
    make_platform(6425, 400, 1)
    make_platform(6595, 357, 1)
    make_platform(6765, 314, 1)
    make_platform(6935, 271, 1)
    make_platform(7105, 228, 1)
    make_platform(7275, 185, 1)
    make_spike_on_platform(7455, 142, 1)
    make_platform(7480, 312, 1)
    make_platform(7800, 400, 1)
    make_platform(7970, 356, 1)
    make_platform(8140, 313, 4)
    make_platform(8482, 270, 1)
    make_platform(8525, 227, 1)
    make_platform(8525, 270, 1)
    make_platform(8525, 313, 1)
    make_platform(8482, 400, 4)
    make_spike_on_platform(8654, 400, 1)
    make_platform(8697, 400, 18)


gravity = 1


class Avatar:
    def __init__(self, x, y, x_speed, y_speed, angle, jump_state):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.angle = angle
        self.jump_state = jump_state

    def blit(self):
        screen.blit(character_img, (self.x, self.y))

    def update_pos(self, gravity):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.y_speed = self.y_speed + gravity

    def jump(self):
        player.y_speed = -10


player = Avatar(75, 448, 0, 0, 0, False)
player_rect = pygame.Rect(player.x, player.y, 43, 38)
ground_rect = pygame.Rect(0, 490, 800, 111)

# Print text on the Screen
class Text:
    """Creates a text but does not display it on screen."""

    def __init__(self, text, font_type, size, color, x, y):
        self.text = text
        self.font_type = font_type
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def display_text(self):
        text_displayed = pygame.font.Font(self.font_type, self.size).render(str(self.text), True, self.color)
        screen.blit(text_displayed, (self.x, self.y))

press_start = Text('PRESS SPACE TO START', 'Supermario.ttf', 53, (168, 50, 50), 35, 275)
you_died = Text('YOU DIED!q!1!', 'supermario.ttf', 75, (168, 56, 50), 125, 75)
press_enter_to_retry = Text('please press "enter" to retry.', 'supermario.ttf', 30, (120, 66, 64), 130, 175)
you_won = Text('YOU WON!!11', 'supermario.ttf', 75, (227, 202, 108), 125, 75)
woa_much_praise = Text("WOA MUCH PRAISE!!", 'supermario.ttf', 65, (227, 202, 108), 35, 150)
class Finish_wall_and_light:

    def __init__(self, x, y, rect, light_x, light_y):
        self.x = x
        self.y = y
        self.rect = rect
        self.light_x = light_x
        self.light_y = light_y

    def blit(self):
        screen.blit(finish_wall_light_img, (self.light_x, self.light_y))
        screen.blit(finish_wall_img, (self.x, self.y))

    def move(self):
        self.x -= 10
        self.light_x -= 10

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 70, 700)

finish_wall = Finish_wall_and_light(9471, -5, 0, 9425, -50)

screen_state = "ready"
player_collide_ground_y = (ground_rect.top - player_rect.height + 1)
first_play_loop = True

# Game Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if screen_state == "ready":
                    screen_state = "playing"
                elif screen_state == 'playing' or "near finish":
                    if jump_ready:
                        player.jump()
            elif event.key == pygame.K_RETURN:
                if screen_state == "dead":
                    screen_state = "ready"


    screen.fill((0, 0, 0))
    if color_count <= 10:
        if color_stage == 0:
            press_start.color = (press_start.color[0], press_start.color[1] + color_change, press_start.color[2])
            color_count += 1
        elif color_stage == 1:
            press_start.color = (press_start.color[0] - color_change, press_start.color[1], press_start.color[2])
            color_count += 1
        elif color_stage == 2:
            press_start.color = (press_start.color[0], press_start.color[1], press_start.color[2] + color_change)
            color_count += 1
        elif color_stage == 3:
            press_start.color = (press_start.color[0], press_start.color[1] - color_change, press_start.color[2])
            color_count += 1
        elif color_stage == 4:
            press_start.color = (press_start.color[0] + color_change, press_start.color[1], press_start.color[2])
            color_count += 1
        elif color_stage == 5:
            press_start.color = (press_start.color[0], press_start.color[1], press_start.color[2] - color_change)
            color_count += 1
        elif color_stage == 6:
            color_stage = 0
    else:
        color_stage += 1
        color_count = 0


    if screen_state == 'ready':
        if first_play_loop == True:
            print("all good!")
            first_play_loop = False
            platforms.clear()
            spikes.clear()
            add_spikes_to_list()
            add_platforms_to_list()
            set_ground_piece_starting_position()
            for platform in platforms:
                platform.player_collide_platform_y = (platform.rect.top - player_rect.height + 1)
        player.x = 75
        player.y = 453
        press_start.x = 35
        for ground in ground_pieces:
            ground.blit()
            ground_rect = pygame.Rect(0, 490, 800, 111)
    elif screen_state == 'playing':
        for ground in ground_pieces:
            ground.move()
            ground_rect = pygame.Rect(0, 490, 800, 111)
        finish_wall.move()
        for spike in spikes:
            spike.move()
        press_start.x = 5000
    elif screen_state == "dead":
        first_play_loop = True
        press_start.x = 5000
        player.x = 100000
        for platform in platforms:
            platform.x = 10000
        ground_rect = pygame.Rect(10000, 490, 800, 111)
        for ground in ground_pieces:
            ground.x = 10000
        for spike in spikes:
            spike.x = 10000
        finish_wall.x = 10000
        finish_wall.light_x = 10000
    elif screen_state == "near finish":
        player.x += 10
    elif screen_state == "win":
        first_play_loop = True
        player.x = 100000
        for platform in platforms:
            platform.x = 10000
        ground_rect = pygame.Rect(10000, 490, 800, 111)
        for ground in ground_pieces:
            ground.x = 10000
        for spike in spikes:
            spike.x = 10000
        finish_wall.x = 10000
        finish_wall.light_x = 10000


    finish_wall.update_rect()
    player.update_pos(gravity)
    player_rect = pygame.Rect(player.x, player.y, 43, 38)

    for platform in platforms:
        platform.update_rect()
    for spike in spikes:
        spike.update_rect()

    jump_ready = False

    collision_tolerance = abs(player.y_speed) + 10
    for platform in platforms:
        if player_rect.colliderect(platform.rect):
            print('collision')
            if abs(player_rect.bottom - platform.rect.top) < collision_tolerance:
                print("top and bottom collision")
                player.y = platform.player_collide_platform_y
                player.y_speed = 0
                jump_ready = True
            elif abs(player_rect.right - platform.rect.left) < collision_tolerance:
                print("side collision")
                screen_state = "dead"
            elif abs(player_rect.top - platform.rect.bottom) < collision_tolerance:
                print("bottom collision")
                screen_state = "dead"

    for spike in spikes:
        if player_rect.colliderect(spike.rect_top):
            screen_state = "dead"
        elif player_rect.colliderect(spike.rect_bottom):
            screen_state = "dead"

    if player_rect.colliderect(finish_wall.rect):
        screen_state = "win"

    if player_rect.colliderect(ground_rect):
        player.y = player_collide_ground_y
        player.y_speed = 0
        jump_ready = True

    player_rect = pygame.Rect(player.x, player.y, 43, 38)
    if screen_state == "playing":
        for platform in platforms:
            platform.move()
            platform.blit()

    # drawing
    # these print the floor , not the platforms you jump on, as in the class
    screen.blit(background_img, (0, 0))
    for spike in spikes:
        spike.blit()
    for platform in platforms:
        platform.blit()
    finish_wall.blit()
    for ground in ground_pieces:
        ground.blit()
    if map_scout:
        player.x = 1000000
    player.blit()
    press_start.display_text()
    if screen_state == "dead":
        you_died.display_text()
        press_enter_to_retry.display_text()
    elif screen_state == "win":
        you_won.display_text()
        woa_much_praise.display_text()
        screen.blit(high_quality_character_img, (175, 225))
        character_img = pygame.transform.scale(character_img, (344, 304))

    if draw_rect:
        pygame.draw.rect(screen, (0, 255, 0), ground_rect)
        pygame.draw.rect(screen, (255, 0, 0), player_rect)
        for platform in platforms:
            pygame.draw.rect(screen, (0, 0, 255), platform.rect)
        for spike in spikes:
            pygame.draw.rect(screen, (255, 255, 255), spike.rect_top)
            pygame.draw.rect(screen, (255, 255, 255), spike.rect_bottom)
        pygame.draw.rect(screen, (0, 150, 0), finish_wall.rect)

    if finish_wall.x < 700:
        if screen_state != "win":
            screen_state = "near finish"

    clock.tick(30)
    pygame.display.update()
