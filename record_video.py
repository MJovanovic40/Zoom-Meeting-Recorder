from screen_recorder_sdk import screen_recorder
import time

def record(subject, directory):
    params = screen_recorder.RecorderParams()

    # intialize the screen recoder
    screen_recorder.init_resources(params)

    # start video recording
    print('Video Started')
    screen_recorder.start_video_recording(f'{directory}/output.mp4', 30, 8000000, True)

    # time limit
    time.sleep(subject.duration * 3600)

    # stop the recording
    screen_recorder.stop_video_recording()
    print('Video Stopped')
