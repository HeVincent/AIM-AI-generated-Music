from flask import Flask, render_template, request, send_file  # for python server
from gen import midi_gen  # for generating our midi files
from os import listdir, path, chdir, remove  # for navigating the directory
from ast import literal_eval  # for reading dictionary data

app = Flask(__name__)
routes = ['/midi_gen', '/export', '/', '/db', '/results']  # list of url paths


# to clear MIDI cache
def clear_midi():
    for x in listdir('outputs'):
        remove('outputs\\'+x)


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
    clear_midi()
    genres = listdir('midi_files')  # getting a list of genres
    return render_template("index.html", title='Home', genres=genres)


@app.route(routes[3])
def db():
    clear_midi()
    # reading dictionary data
    with open('midis1', 'rb') as f1:
        midis1 = literal_eval(f1.read().decode('utf-8'))
    f1.close()
    with open('midis2', 'rb') as f2:
        midis2 = literal_eval(f2.read().decode('utf-8'))
    f2.close()

    return render_template("dataset.html", title='Dataset', midis1=midis1, midis2=midis2)


@app.route(routes[4])
def results():
    clear_midi()
    genres = [genre.replace('.png', '') for genre in listdir('static/images/loss-per-epoch')]  # getting genre list
    return render_template("output.html", title='Observations and Results', genres=genres)


if __name__ == '__main__':
    chdir(path.dirname(path.abspath(__file__)))
    app.run()
