import subprocess
import sys
import sounddevice as sd
import soundfile as sf
import numpy

def transcribe_audio(file_path):
  
    
    # Using sys.executable to ensure the same Python interpreter is used
    process = subprocess.Popen([sys.executable, 'transcribe.py', file_path],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the process to complete and capture both stdout and stderr (if needed for debugging)
    stdout, stderr = process.communicate()
    
    # Read the output from the file output.txt
    with open("output.txt", "r") as f:
        output = f.read()
    
    return output

# Start recording the input microphone and when the user presses enter, stop the recording and save it as an audio file.

import threading

import sounddevice as sd
import soundfile as sf
import threading
import numpy

def record_audio(file_path):
    print("Recording... Press Enter to stop.")

    # Set up a flag to indicate when recording should stop
    stop_recording = threading.Event()

    def capture_audio(file_path, sample_rate=8000):
        # Initialize a dynamically growing list to store frames
        frames = []

        # Correct callback implementation
        def callback(indata, _, time, status):
            # Directly append to frames, as it's correctly in scope
            frames.append(indata.copy())

        # Open a stream that continuously records audio
        with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
            stop_recording.wait()  # Wait here until we're told to stop
        
        # Concatenate all frames and save to a file
        audio_data = numpy.concatenate(frames, axis=0)
        sf.write(file_path, audio_data, sample_rate)


    # Start the recording in a separate thread
    threading.Thread(target=lambda: capture_audio(file_path), daemon=True).start()

    # Wait for the user to press Enter to stop recording
    input()

    # Signal the recording thread to stop
    stop_recording.set()

#while true
while True:
    record_audio("output.wav")
    #get the file path of the audio file
    file_path = "output.wav"

    transcription_result = transcribe_audio(file_path)

    print(transcription_result)