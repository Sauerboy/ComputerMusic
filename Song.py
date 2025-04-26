import pydub
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects
import ffmpeg

wiiSound=AudioSegment.from_wav('/Users/arielsauer/Downloads/WiiSound.wav')
oofSound=AudioSegment.from_mp3('/Users/arielsauer/Downloads/oof.mp3')

play(oofSound)