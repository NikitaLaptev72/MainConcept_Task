import sqlite3
import json


def help_plugin4():
    print(save_json.__doc__)


def save_json(path_to_json):
    '''
    plugin4

    Accepts a path to a json file created by plugin #4
    and saves per-frame information into an sqlite database.

    Available function:
    save_json
    Parameters:
    path_to_json
    '''

    print('Running plugin4\n')
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "DROP TABLE IF EXISTS FramesData"
        cursor.execute(sqlite_select_query)

        sqlite_select_query = "CREATE TABLE FramesData (data json)"
        cursor.execute(sqlite_select_query)

        cursor.execute("DELETE FROM FramesData")

        with open(path_to_json, 'r') as f:
            frames = json.load(f)
            for frame in frames['frames']:
                cursor.execute(
                    "insert into FramesData values (?)",
                    [
                        json.dumps(
                            frame,
                            sort_keys=True
                        )
                    ]
                )
                sqlite_connection.commit()
        cursor.close()

    except Exception as e:
        print(f"Error \"{e}\" occurred!")

    finally:
        if (sqlite_connection):
            sqlite_connection.close()
