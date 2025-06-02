import librosa
# import matplotlib.pyplot as plt
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://root:example@localhost:27017/keystroke-detector?authSource=admin"

client = MongoClient(CONNECTION_STRING)
db = client['keystroke-detector']
keystroke_collection = db["key-strokes"]

sound_base_path = "sounds"
keys = ["A", "S", "D", "F", "L", "+"]
file_numbers = range(1, 5)

for key in keys:
    for file_number in file_numbers:
        filename = sound_base_path + "/" + key + "/" + key + "_" + str(file_number) + ".wav"
        waveform, sample_rate = librosa.load(filename)

        keystroke_collection.insert_one({"letter": key, "waveform": waveform.tolist()})
        print(filename)