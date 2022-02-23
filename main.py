from plugins import *
import sys
import os

from plugins.plugin1 import help_plugin1
from plugins.plugin2 import help_plugin2
from plugins.plugin3 import help_plugin3
from plugins.plugin4 import help_plugin4
from plugins.plugin5 import help_plugin5


choice_method = {
    'help plugin1': 'plugin1_info',
    'help plugin2': 'plugin2_info',
    'help plugin3': 'plugin3_info',
    'help plugin4': 'plugin4_info',
    'help plugin5': 'plugin5_info',
}


def plugin1_info():
    '''
    Function to call help_plugin1
    '''
    help_plugin1()


def plugin2_info():
    '''
    Function to call help_plugin2
    '''

    help_plugin2()


def plugin3_info():
    '''
    Function to call help_plugin3
    '''

    help_plugin3()


def plugin4_info():
    '''
    Function to call help_plugin4
    '''

    help_plugin4()


def plugin5_info():
    '''
    Function to call help_plugin5
    '''

    help_plugin5()


def help():
    '''
    Function to get information about
    available plugins
    '''

    print('Available plugins:')
    for plugin in os.listdir('plugins'):
        if (plugin != '__init__.py' and plugin != '__pycache__'):
            print(plugin)


def run_plugins():
    '''
    Function to run all plugins function
    '''
    play_video('/home/nikita/Videos/IMG_4706.MOV')
    extract_video('/home/nikita/Videos/IMG_4706.MOV')
    get_json_from_video('/home/nikita/Videos/IMG_4706.MOV')
    save_json('/home/nikita/Desktop/Test/Task_MainConcept_2/my_project/frames.json')
    plotting('sqlite_python.db')


if __name__ == "__main__":
    if (sys.argv[1:] == []):
        run_plugins()
    else:
        if (sys.argv[1:].__len__() == 1):
            help()
        elif (sys.argv[1:].__len__() == 2):
            try:
                arguments = sys.argv[1:]
                eval(choice_method[' '.join(sorted(arguments))])()

            except Exception as e:
                print(f"Error \"{e}\" occurred!")
                print('Check the module call arguments!')
        else:
            print('Check the module call arguments!')
