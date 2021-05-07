from music21 import converter
from glob import glob


def avg_tempos():
    res = {}
    for genre in glob('midi_files/*'):
        avg = 0
        for midi in glob(genre+'/*'):
            s = converter.parse(midi)
            m = s.metronomeMarkBoundaries()[0][2]
            avg += m.number
        avg = int(avg/33)
        genre = genre.replace('midi_files\\', '')
        res[genre] = avg
    return res


if __name__ == '__main__':
    print(avg_tempos())
