import time
import sounddevice as sd
import numpy as np
from sklearn.linear_model import SGDClassifier

from db import get_collection

sample_rate = 22050
duration = 1

def guess():

    print("Listening in:")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    print("Listening now!")

    try:
        print("Listening: ")
        waveform = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64', blocking=True)
        print("Recording complete.")

        keystroke_data = get_collection("key-strokes")
        training_data = []
        target_values = []

        for keystroke in keystroke_data:
            training_data.append(np.array(keystroke["waveform"]))
            target_values.append(keystroke["letter"])

        recorded_waveform = np.array([waveform]).reshape(1, -1)

        model = SGDClassifier("log_loss")
        model.fit(training_data, target_values)
        predict = model.predict(recorded_waveform)

        print(predict)

    except Exception as e:
        print(f"ErrorL {e}")
