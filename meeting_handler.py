import webbrowser
import record_audio
import threading
import ffmpeg
import record_video
import time
import os


def start_audio_recording(length, subject): # in seconds
    record_audio.record(length, subject)


def start_video_recording(length, subject): # in seconds
    record_video.record(length, subject)


def join_meeting(link):
    webbrowser.open(link)


def merge_video(video, audio, directory):
    input_video = ffmpeg.input(directory + "/" + video)
    input_audio = ffmpeg.input(directory + "/" + audio)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'{directory}/video.mp4').run()

def record_meeting(subject):
    print("Initializing meeting...")
    root_dir = os.path.join(os.curdir, f"videos\\{subject.name}")
    run_id = time.strftime(f"%Y-%m-%d_{subject.type}")
    directory = os.path.join(root_dir, run_id)
    os.mkdir(directory)

    join_meeting(subject.link)

    time.sleep(5)

    threads = []

    thread = threading.Thread(target=start_video_recording, args=(subject, directory))
    thread2 = threading.Thread(target=start_audio_recording, args=(subject, directory))

    thread.start()
    thread2.start()

    threads.append(thread)
    threads.append(thread2)

    while threads:
        indexes = []
        for i in range(len(threads)):
            if not threads[i].is_alive():
                indexes.append(i)
        c = 0
        for i in indexes:
            threads.pop(i - c)
            c += 1

    print("Done recording the meeting.")


    print("Merging video and audio...")
    merge_video("output.mp4", "output.wav", directory)

    print("Removing temporary files...")
    os.remove(directory + "\\" + "output.mp4")
    os.remove(directory + "\\" + "output.wav")

    print("Meeting recording done!")