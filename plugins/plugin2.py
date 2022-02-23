import os


def help_plugin2():
    print(extract_video.__doc__)


def extract_video(path):
    '''
    plugin2


    Accepts a path to a media file and
    calls ffmpeg's ffmpeg binary
    to extract a video stream.

    Available function:
    extract_video
    Parameters:
    path
    '''

    print('Running plugin2\n')
    try:
        os.system(
            f"ffmpeg -i {path} -v error -f image2 -vf fps=fps=10 frames/frame%d.png"
        )

    except Exception as e:
        print(f"Error \"{e}\" occurred!")
