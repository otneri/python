import pygame
pygame.init()
pygame.mixer.music.load('snoop.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()