import sqlite3
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def help_plugin5():
    print(plotting.__doc__)


def plotting(sqlite_path):
    '''
    plugin5

    Accepts a path to an sqlite database created by plugin #5
    and uses the matplotplib Python module
    to build a plot and save is as a .png image

    Available function:
    plotting
    Parameters:
    sqlite_path
    '''

    print('Running plugin5\n')
    try:
        frames_size = []
        frames_number = []
        sqlite_connection = sqlite3.connect(sqlite_path)
        cursor = sqlite_connection.execute(
            '''SELECT json_extract(data, '$.coded_picture_number', '$.pkt_size')
            FROM FramesData
            ORDER BY json_extract(data, '$.coded_picture_number')''')
        for row in cursor:
            frames_number.append(json.loads(row[0])[0])
            frames_size.append(json.loads(row[0])[1])

        frames_size = list(map(int, frames_size))
        frames_number = list(map(int, frames_number))

        fig, ax = plt.subplots()
        ax.plot(frames_number, frames_size)

        ax.xaxis.set_major_locator(ticker.AutoLocator())
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

        ax.yaxis.set_major_locator(ticker.AutoLocator())
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

        fig.set_figwidth(20)
        fig.set_figheight(16)

        plt.savefig('plot.png')

    except Exception as e:
        print(f"Error \"{e}\" occurred!")
