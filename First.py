import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Snake starting position and initial direction
snake_pos = [WIDTH / 2, HEIGHT / 2]
snake_body = [[WIDTH / 2, HEIGHT / 2], [WIDTH / 2 - BLOCK_SIZE, HEIGHT / 2], [WIDTH / 2 - (2 * BLOCK_SIZE), HEIGHT / 2]]
direction = 'RIGHT'

# Food position
food_pos = [random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]

# Score
score = 0

# Function to display score
def display_score():
    font = pygame.font.SysFont('arial', 25)
    score_text = font.render("Score: " + str(score), True, WHITE)
    WIN.blit(score_text, [10, 10])

# Function to draw snake
def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

# Function to generate food
def generate_food():
    global food_pos
    food_pos = [random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]

# Main game loop
def main():
    global direction, score

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Move snake
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        elif direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        # Check if snake eats food
        if snake_pos == food_pos:
            score += 1
            generate_food()
        else:
            snake_body.pop()  # Remove tail segment

        # Check if snake hits wall or itself
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            run = False
        for block in snake_body[1:]:
            if snake_pos == block:
                run = False

        # Update snake body
        snake_body.insert(0, list(snake_pos))

        # Draw everything
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
        draw_snake()
        display_score()
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    main()
