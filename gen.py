from numpy import random, reshape, argmax  # for utility functions
from pickle import load  # for loading total notes present in our model
from music21 import instrument, note, chord, stream, tempo  # for writing midi file
from keras.models import load_model  # for loading hdf5 model
from time import time  # for unix time


def midi_gen(genre):
    # genre_tempo =  o/p from tempocheck
    genre_tempo = {'Anthem': 74, 'Classical': 108, 'Indie': 105, 'Metal n Rock': 119, 'Pop n Rock': 114}
    # laoding model and total notes
    music_model = load_model(f"model_data/{genre}_model.hdf5")
    note_file = f'model_data/{genre}_total_notes'

    sequence_length = 100
    net_input = []
    net_output = []

    with open(note_file, 'rb') as f:
        total_notes = load(f)
        pitches = sorted(set(total_notes))
        elem_to_num = dict((e, n) for n, e in enumerate(pitches))
        unique_notes = len(set(total_notes))

    for i in range(len(total_notes) - sequence_length):
        sequence_input = total_notes[i: i + sequence_length]
        net_input.append([elem_to_num[ch] for ch in sequence_input])

    start = random.randint(len(net_input) - 1)

    num_to_elem = dict((num, ele) for num, ele in enumerate(pitches))

    pattern = net_input[start]

    # generate 200 elements
    for iterator in range(150):
        prediction_input = reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(unique_notes)  # normalize

        prediction = music_model.predict(prediction_input, verbose=0)

        idx = argmax(prediction)
        result = num_to_elem[int(idx)]
        net_output.append(result)

        pattern.append(int(idx))
        pattern = pattern[1:]

    offset = 0
    output_notes = []

    for pattern in net_output:
        # if the pattern is a chord
        if ('+' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('+')
            temp_notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                temp_notes.append(new_note)

            new_chord = chord.Chord(temp_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)

        else:
            # if the pattern is a note
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    midi_stream.insert(0, tempo.MetronomeMark(number=genre_tempo[genre]))
    midi_stream.show('text')
    unixt = str(int(time()))
    filename = genre+unixt
    midi_stream.write('midi', fp=f"outputs/{filename}.mid")
    return filename
