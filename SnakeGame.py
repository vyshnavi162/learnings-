# import pygame
# import time
# import random

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# width, height = 600, 400

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)

# # Snake block size
# block_size = 10
# clock = pygame.time.Clock()

# # Create the screen
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Snake Game")

# # Font for score
# font_style = pygame.font.SysFont("bahnschrift", 25)

# # Display message
# def message(msg, color, x, y):
#     mesg = font_style.render(msg, True, color)
#     screen.blit(mesg, [x, y])

# # Game loop
# def gameLoop():
#     game_over = False
#     game_close = False

#     x1, y1 = width // 2, height // 2
#     x1_change, y1_change = 0, 0

#     snake_list = []
#     snake_length = 1

#     food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
#     food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

#     while not game_over:
#         while game_close:
#             screen.fill(black)
#             message("Game Over! Press C-Play Again or Q-Quit", red, width // 6, height // 3)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -block_size
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = block_size
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -block_size
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = block_size
#                     x1_change = 0

#         if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         screen.fill(black)
#         pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])
#         snake_head = []
#         snake_head.append(x1)
#         snake_head.append(y1)
#         snake_list.append(snake_head)
#         if len(snake_list) > snake_length:
#             del snake_list[0]

#         for block in snake_list[:-1]:
#             if block == snake_head:
#                 game_close = True

#         for block in snake_list:
#             pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

#         pygame.display.update()

#         if x1 == food_x and y1 == food_y:
#             food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
#             food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
#             snake_length += 1

#         clock.tick(15)

#     pygame.quit()
#     quit()

# # Run the game
# gameLoop()


import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake block size
block_size = 10
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Font for score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Display message
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

# Game loop
def gameLoop():
    # Ask for user input on difficulty
    difficulty = input("Select difficulty (Beginner, Medium, Expert): ").lower()

    # Set speed based on difficulty
    if difficulty == "beginner":
        speed = 10
    elif difficulty == "medium":
        speed = 15
    elif difficulty == "expert":
        speed = 20
    else:
        print("Invalid difficulty! Defaulting to Medium.")
        speed = 15

    game_over = False
    game_close = False

    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(black)
            message("Game Over! Press C-Play Again or Q-Quit", red, width // 6, height // 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        for block in snake_list:
            pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(speed)  # Use speed based on difficulty

    pygame.quit()
    quit()

# Run the game
gameLoop()