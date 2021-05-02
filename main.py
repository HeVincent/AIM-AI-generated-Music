from flask import Flask, render_template, request, send_file  # for python server
from gen import midi_gen  # for generating our midi files
from os import listdir  # for navigating the directory

app = Flask(__name__)
routes = ['/midi_gen', '/export', '/', '/db', '/results']  # list of paths


# utility routes
@app.route(routes[0], methods=['POST'])
def get_midi():
    data = request.get_json()
    return midi_gen(data['genre'])  # returning the file's name of the output MIDI


@app.route(routes[1])
def export():
    filename = request.args.get('filename')  # getting the file name from the parameter in url
    export_file = f"outputs/{filename}.mid"
    return send_file(
        export_file,
        as_attachment=True
    )


# render routes
@app.route(routes[2])
def home():
    genres = listdir('midi_files')  # getting a list of genres
    return render_template("index.html", title='Home', genres=genres)


@app.route(routes[3])
def db():
    # defining data structure for different genres
    midis1 = {'Anthem': {'artist': list(), 'title': list()}, 'Classical': {'artist': list(), 'title': list()},
              'Pop n Rock': {'artist': list(), 'title': list()}}
    midis2 = {'Indie': {'title': list()},
              'Traditional': {'title': list()}}

    # populating the data by navigating directories
    for genre in midis1:
        for midi in listdir(f'midi_files/{genre}'):
            songdet = midi.split(' - ')  # splitting song details into artist and filename
            midis1[genre]['artist'].append(songdet[0])
            midis1[genre]['title'].append(songdet[1])
    for genre in midis2:
        for midi in listdir(f'midi_files/{genre}'):
            midis2[genre]['title'].append(midi)

    return render_template("dataset.html", title='Dataset', midis1=midis1, midis2=midis2)


@app.route(routes[4])
def results():
    genres = [genre.replace('.png', '') for genre in listdir('static/images/loss-per-epoch')]  # getting genre list
    return render_template("output.html", title='Observations and Results', genres=genres)


if __name__ == '__main__':
    app.run(debug=True)
