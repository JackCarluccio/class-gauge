import json
import os
import numpy as np
import audio_recorder
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-en-us-0.15"

if not os.path.exists(MODEL_PATH):
    print(f"Please download the model from https://alphacephei.com/vosk/models")
    print(f"and unpack it to {MODEL_PATH}")
    exit(1)

model = Model("vosk-model-small-en-us-0.15")


def transcribe_audio(audio_data):
    global model
    
    # Convert float32 audio data to int16
    if audio_data.dtype == np.float32:
        audio_data = (audio_data * 32767).astype(np.int16)
    
    # Create recognizer instance
    rec = KaldiRecognizer(model, audio_recorder.RATE)
    
    # Process audio data
    raw_data = audio_data.tobytes()
    rec.AcceptWaveform(raw_data)
    result = json.loads(rec.FinalResult())
    
    return result['text']
