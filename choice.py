import pygame
import subprocess
import button

# Initialize Pygame
pygame.init()

# Set screen size and caption
logo = pygame.image.load("images/logo.png")
bg = pygame.image.load("images/bg.jpg")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((540, 540))
pygame.display.set_caption("ヒルキア の ボード")

# button
chess = pygame.image.load("images/chess.png").convert_alpha()
checkers = pygame.image.load("images/checkers.png").convert_alpha()
playchess = button.Button(10, 100, chess, 0.8)
playcheckers = button.Button(70, 300, checkers, 0.8)

# Main game loop
running = True
while running:
    screen.blit(bg, (0, 0))

    if playchess.draw(screen):
        subprocess.run(["python", "chaos-chess.py"])
    if playcheckers.draw(screen):
        subprocess.run(["python", "checkers.py"])

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()
    # Draw button on screen
    pygame.display.update()