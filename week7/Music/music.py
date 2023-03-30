import pygame,sys

pygame.init()
pygame.mixer.music.load(r"D:\Programming\PyCharm ENG\week7\Music\The_Tokens_-_The_Lion_Sleeps_Tonight_64402105.mp3")
pygame.mixer.music.play(-1)

pygame.display.set_mode((500,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()