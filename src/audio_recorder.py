import pyaudio
import wave
import threading
import time
import numpy as np

# Global variables to maintain state
_audio = pyaudio.PyAudio()
_frames = []
_is_recording = False
_recording_thread = None

# Default audio parameters
CHANNELS = 1
RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paFloat32

def _record_audio():
    global _frames, _is_recording
    
    stream = _audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    while _is_recording:
        data = stream.read(CHUNK)
        _frames.append(data)
        
    stream.stop_stream()
    stream.close()

def start_recording():
    global _frames, _is_recording, _recording_thread
    if _is_recording:
        return
        
    _frames = []
    _is_recording = True
    
    _recording_thread = threading.Thread(target=_record_audio)
    _recording_thread.start()

def stop_recording():
    global _is_recording, _recording_thread
    if not _is_recording:
        return None
        
    _is_recording = False
    _recording_thread.join()
    
    # Convert frames to numpy array
    audio_data = np.frombuffer(b''.join(_frames), dtype=np.float32)
    return audio_data

def save_to_wav(filename, audio_data):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(_audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(audio_data.tobytes())

def play_audio(audio_data):
    stream = _audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True
    )
    
    stream.write(audio_data.tobytes())
    stream.stop_stream()
    stream.close()

def cleanup():
    _audio.terminate()


# Example usage
if __name__ == "__main__":
    print("Starting recording...")
    start_recording()
    
    # Record for 5 seconds
    time.sleep(5)
    
    print("Stopping recording...")
    audio_data = stop_recording()
    
    print("Playing back the recording...")
    play_audio(audio_data)
    
    print("Saving recording to file...")
    save_to_wav("recording.wav", audio_data)
    
    cleanup()