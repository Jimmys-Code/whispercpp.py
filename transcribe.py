import time
import os
import sys
import contextlib
from whispercpp import Whisper
counter=0
# Ensures 'output.txt' exists and is empty at the start
if not os.path.exists("output.txt"):
    open("output.txt", "w").close()

# Initialize Whisper outside of the function to avoid re-initialization on each call
w = Whisper("base")

def transcribe_audio(file_path):
    # Transcribe the audio file
    result = w.transcribe(file_path)

    # Extract text from the result
    text = w.extract_text(result)

    return text

# Example usage
file_path = "output.wav"

while True:
    # Start timing
    start_time = time.time()
    print("Transcribing audio...")
    # Suppressing function's verbose output using contextlib
    with open(os.devnull, 'w') as devnull, contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
        # Call the transcribe_audio function and store its return value in the 'transcription' variable
        transcription = transcribe_audio(file_path)
    print(f"{counter}]ranscription complete!")
    end_time = time.time()
    time_taken = int(end_time - start_time)  # Convert to integer

    print(f"version {counter}: {transcription}\n")
    # print(f"Time taken to transcribe: {time_taken} seconds")
    print(f"Which is {time_taken/30:.2f} seconds a sentence")  # Updated for improved formatting
    #play a sound to alert the user
    os.system("aplay /usr/share/sounds/alsa/Front_Center.wav")
    # Write output to file 'output.txt'
    with open("output.txt", "w") as f:
        f.write(f"version {counter}: {transcription}\n")
        # f.write(f"Time taken to transcribe: {time_taken} seconds\n")
        f.write(f"Which is {time_taken/30:.2f} seconds a sentence\n")  # Updated for improved formatting
    counter+=1

    
    
