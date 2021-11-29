import pyaudio
import wave
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def record(subject, directory):
    output_name = f"{directory}/output.wav"
    p = pyaudio.PyAudio()

    SPEAKERS = p.get_default_output_device_info()["hostApi"]

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_host_api_specific_stream_info = SPEAKERS,
                    frames_per_buffer=CHUNK)

    print("Recording audio...")

    frames = []

    start_time = time.time()
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if time.time() - start_time > (subject.duration * 3600): # broj sekundi
            break


    print("Finished recording audio.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
