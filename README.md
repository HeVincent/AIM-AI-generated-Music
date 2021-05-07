# **AIM: AI-generated Music**

### **How to start?**
1. Create a python virtual environment and run `pip install -r req.txt`.
2. Run `main.py` or enter `flask run` (have to set `FLASK_APP=main.py`) from your virtual environment console.

### **Utility scripts used**
1. `fetch_midis.py` for fetching MIDIs from MuseScore database. (We do NOT condone piracy; this is for educational purpose only.)
2. `dict_dataset.py` for storing dictionary of MIDI files.
3. `tempo_check.py` for calculating average tempo for each genre.   
4. `model_training.py` for training our LSTM model.
5. `gen.py` for generating the desired MIDI output file(s).