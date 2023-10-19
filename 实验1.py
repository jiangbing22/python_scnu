import pygame
import os
import random
import time
happy=[i for i in os.listdir('music/happy') if i=='*.mp3']
sad =[j for j in os.listdir('music/happy') if j=='*.mp3']
def play(emo):
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(emo))
    pygame.mixer.music.play()
    time.sleep(100)
def main():
    emotion = 0
    while emotion !=8:
        emotion=input('请输入数字:')
        if emotion == 0:
            play(happy)
        if emotion ==1:
            play(sad)

if __name__ =='__main__':
    main()

