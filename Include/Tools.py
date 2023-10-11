import numpy
import argparse
from pydub import AudioSegment
import sys
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
AudioSegment.ffmpeg = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
def spectro():
    return


def main(args):

    audio_file = AudioSegment.from_file(r"C:\Users\thiba\PycharmProjects\MixClassification\TakeMeToYourParadise.mp3")
    frame_interet = audio_file[:6*60+30]
    del audio_file
    sample = np.array(frame_interet.get_array_of_samples(), dtype=np.float32).reshape((-1, frame_interet.channels)) / (
            1 << (8 * frame_interet.sample_width - 1))
    f, t, Sxx = signal.spectrogram(sample[:, 0], fs=44100, nfft=514)
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.title('Spectrogram Using scipy.signal.spectrogram() method')
    plt.show()
    return audio_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-path" ,default="TakeMeToYourParadise.mp3",help="audio file")
    s = main(parser.parse_args())