import pygame
import subprocess
import button
# Initialize Pygame
pygame.init()

# Set screen size and caption
logo = pygame.image.load("images/logo.png")
bg = pygame.image.load("images/bg.jpg")
logo = pygame.image.load("images/logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((540, 540))
pygame.display.set_caption("ヒルキア の アプリ")

# button
start = pygame.image.load("images/start.png").convert_alpha()
start_button = button.Button(160, 200, start, 0.8)

# Main game loop
running = True
while running:

	screen.blit(bg, (0, 0))

	if start_button.draw(screen):
		subprocess.run(["python", "choice.py"])

	# event handler
	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			running = False

		pygame.display.update()
	# Draw button on screen
	pygame.display.update()

# Quit Pygame
pygame.quit()