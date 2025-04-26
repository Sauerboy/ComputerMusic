import pydub
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects
import ffmpeg
import random

sound_list=[AudioSegment.from_wav('sounds/WiiSound.wav'),
           AudioSegment.from_mp3('sounds/oof.mp3'),
           AudioSegment.from_mp3('sounds/spongebob.mp3'),
           AudioSegment.from_mp3('sounds/onepiece.mp3'),
           AudioSegment.from_mp3('sounds/deltaco.mp3'),
           AudioSegment.from_mp3('sounds/mario.mp3')]

dur_str=input("This game will randomly select a sound and play it at a random speed each round. How many rounds would you like to play? Please enter a number:     ")
dur=int(dur_str)
for i in range(dur):
    play(sound_list[random.randint(0, len(sound_list)-1)].speedup(random.uniform(.5,2)))