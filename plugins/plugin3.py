import os


def help_plugin3():
    print(get_json_from_video.__doc__)


def get_json_from_video(path):
    '''
    plugin3

    Accepts a path to a media file and
    calls ffmpeg's ffprobe binary
    to extract per-frame information
    for a first video stream into a json file

    Available function:
    get_json_from_video
    Parameters:
    path
    '''

    print('Running plugin3\n')
    try:
        os.system(
            f"ffprobe -v error -select_streams v:0 -print_format json -show_frames {path} > frames.json"
        )

    except Exception as e:
        print(f"Error \"{e}\" occurred!")
