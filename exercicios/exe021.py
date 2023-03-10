"""
Tocando uma música de um arquivo MP3 com Python
"""
import pygame
pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
