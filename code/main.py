import pygame
from settings import *
from pygame.image import load

from editor import Editor

class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Super Pirate Maker")
		self.clock = pygame.time.Clock()
		self.editor = Editor()
		cursor_surf = load('./graphics/cursors/mouse.png').convert_alpha()
		cursor = pygame.cursors.Cursor((0, 0), cursor_surf)
		pygame.mouse.set_cursor(cursor)

	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			
			self.editor.run(dt)
			pygame.display.update()


if __name__ == '__main__':
	main = Main()
	main.run()
