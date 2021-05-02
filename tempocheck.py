from music21 import converter
from glob import glob


def avgtempos():
    res = {}
    for genre in glob('midi_files/*'):
        avg = 0
        for midi in glob(genre+'/*'):
            s = converter.parse(midi)
            m = s.metronomeMarkBoundaries()[0][2]
            avg += m.number
        if genre != 'Indie':
            avg = int(avg/26)
        else:
            avg = int(avg/33)
        genre = genre.replace('midi_files\\', '')
        res[genre] = avg
    return res


if __name__ == '__main__':
    print(avgtempos())
