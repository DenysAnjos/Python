# Faça um programa em Python que abra e reproduza um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('xaropin.mp3')
pygame.mixer.music.play()
pygame.event.wait()
