from os import listdir, chdir, path


def dataset():
    # defining data structure for different genres
    midis1 = {'Anthem': {'artist': list(), 'title': list()}, 'Classical': {'artist': list(), 'title': list()},
              'Pop n Rock': {'artist': list(), 'title': list()}, 'Metal n Rock': {'artist': list(), 'title': list()}}
    midis2 = {'Indie': {'title': list()}}

    # populating the data by navigating directories
    for genre in midis1:
        for midi in listdir(f'midi_files/{genre}'):
            songdet = midi.split(' - ')  # splitting song details into artist and filename
            midis1[genre]['artist'].append(songdet[0])
            midis1[genre]['title'].append(songdet[1])
    for genre in midis2:
        for midi in listdir(f'midi_files/{genre}'):
            midis2[genre]['title'].append(midi)

    with open('midis1', 'wb') as f1:
        f1.write(bytes(str(midis1), 'utf-8'))
    f1.close()
    with open('midis2', 'wb') as f2:
        f2.write(bytes(str(midis2), 'utf-8'))
    f2.close()


if __name__ == '__main__':
    chdir(path.dirname(path.abspath(__file__)))
    dataset()
