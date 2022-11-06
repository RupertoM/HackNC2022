class Sound:
    import pygame
    def __init__(self,file):
        self.file = file

    def playChannel(self,channelNum):
        self.pygame.mixer.Channel(channelNum).play(self.pygame.mixer.Sound(self.file), maxtime=550)


