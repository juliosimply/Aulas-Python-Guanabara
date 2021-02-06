#Exercicio 021 tocando mp3

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while(pygame.mixer.music.get_busy()):pass
