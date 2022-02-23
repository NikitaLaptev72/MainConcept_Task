import os


def help_plugin1():
    print(play_video.__doc__)


def play_video(path):
    '''
    plugin1

    Accepts a path to a media file and calls
    ffmpeg's ffplay binary to play the file.

    Available function:
    play_video
    Parameters:
    path
    '''

    print('Running plugin1')
    try:
        os.system(
            f"ffplay -v error {path}"
        )

    except Exception as e:
        print(f"Error \"{e}\" occurred!")
