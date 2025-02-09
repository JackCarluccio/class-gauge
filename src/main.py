import camera
import audio_recorder
import text_transcription
import question_validation
import participation_tracker
import time
import random
import threading
from queue import Queue

NAMES = ['Jack', 'Anthony', 'Rafayel']

QUESTION_BUFFERING_TIME = 1.0
QUESTION_PROCESSING_TIME = 5.0

time_of_question = None
is_processing_conversation = False
conversation_queue = Queue()

camera = camera.Camera()


def process_audio(audio_data):
    print("Processing audio...")
    text = text_transcription.transcribe_audio(audio_data)
    print("Transcription:", text)
    is_valid = question_validation.validate_question(text)
    if is_valid:
        participation_tracker.increment_participation_score(random.choice(NAMES))


def conversation_worker():
    while True:
        audio_data = conversation_queue.get()
        if audio_data is None:
            break

        process_audio(audio_data)
        conversation_queue.task_done()


def begin_conversation():
    global is_processing_conversation
    is_processing_conversation = True

    audio_recorder.start_recording()


def end_conversation():
    global is_processing_conversation
    is_processing_conversation = False

    audio_data = audio_recorder.stop_recording()
    conversation_queue.put(audio_data)


def on_camera_frame(frame):
    global time_of_question, is_processing_conversation

    detected_hand_raise = True
    if detected_hand_raise and not is_processing_conversation:
        print("Detected a hand raise!")
        time_of_question = time.time()
        begin_conversation()
    
    if is_processing_conversation and time.time() - time_of_question > QUESTION_PROCESSING_TIME:
        time_of_question = None
        end_conversation()


threading.Thread(target=conversation_worker, daemon=True).start()
camera.register_callback(on_camera_frame)
threading.Thread(target=camera.start).start()
