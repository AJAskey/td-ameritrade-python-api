import os
import pathlib
import sys
import json

if sys.version_info >= (3, 5):
    home_dir = str(pathlib.Path.home())
else:
    home_dir = os.path.expanduser('~')

default_dir = os.path.join(home_dir, '.tdunofficial')

class StatePath():

    def __init__(self):
        """Initalizes the StatePath Class"""
        self.python_version = sys.version_info
        self.credenitals_file_name = 'td_state.json'

    def path_home(self) -> pathlib.PurePath:
        """Determines the user's Home Path using Pathlib.

        Returns:
        ----
        {pathlib.PurePath} -- A PurePath object that points to
            the user's home directory.
        """

        home_directory = pathlib.Path.home()
        return home_directory

    @property
    def home_directory(self) -> pathlib.PurePath:
        """Returns the Home directory path.

        Returns:
        ----
        {pathlib.PurePath} -- A path object.
        """        
        return self.path_home()

    @property
    def library_directory(self) -> pathlib.PurePath:
        """Returns the TD Library directory path.

        Returns:
        ----
        {pathlib.PurePath} -- A path object.
        """    
        return self.path_library()

    @property
    def settings_directory(self) -> pathlib.PurePath:
        """Returns the `.td_python_library` directory path.

        Returns:
        ----
        {pathlib.PurePath} -- A path object.
        """    
        return self.path_settings()

    def path_library(self) -> pathlib.PurePath:
        """Generates the TD Library Path.

        Returns:
        ----
        {pathlib.PurePath} -- A PurePath object pointing to the TD
            library.
        """     
        library_directory = pathlib.Path(__file__).parent
        return library_directory

    def path_settings(self) -> pathlib.PurePath:
        """Generates a path to the `.td_python_library` directory.

        Returns:
        ----
        {pathlib.PurePath} -- A PurePath object pointing to the `.td_python_library` 
            directory.
        """
        self.home_directory
        settings_directory = self.home_directory.joinpath('.td_python_library')
        return settings_directory

    def json_settings_path(self):
        """Generates a path to the `.td_python_library/td_state.json` file.

        Returns:
        ----
        {pathlib.PurePath} -- A PurePath object pointing to the
             `.td_python_library/td_state.json` file.
        """
        return self.settings_directory.joinpath(self.credenitals_file_name)
    
    def json_library_path(self):
        """Generates a path to the `td/td_state.json` file.

        Returns:
        ----
        {pathlib.PurePath} -- A PurePath object pointing to the
             `td/td_state.json` file.
        """
        return self.library_directory.joinpath(self.credenitals_file_name)

    def does_file_exist(self, file_path: pathlib.Path) -> bool:
        """Checks if a file exists.

        Arguments:
        ----
        file_path {pathlib.Path} -- A path to a specific file.

        Returns:
        ----
        bool -- `True` if it exists, `False` if it does not exist.
        """        
        return file_path.exists()
    
    def does_directory_exist(self, file_path: pathlib.Path) -> bool:
        """Checks if a directory exists.

        This takes a file path and checks if folder that the file is supposed
        to exist in exists. It only does one level up.

        Arguments:
        ----
        file_path {pathlib.Path} -- A path to a specific directory.

        Returns:
        ----
        bool -- `True` if it exists, `False` if it does not exist.
        """
               
        # Grab the directory
        directory = file_path.parent

        # See if it exists
        return directory.exists()

    def write_to_settings(self, state: dict) -> pathlib.Path:
        """Writes the credentials to the Settigns folder.

        Arguments:
        ----
        state {dict} -- The session state dictionary.

        Returns:
        ----
        pathlib.Path -- The path to credentials path.
        """        

        json_settings_path = self.json_settings_path()

        # Check to see if the folder exists.
        if not self.does_directory_exist(file_path=json_settings_path):
            json_settings_path.parent.mkdir()
        
        # write to the JSON file.
        with open(file=json_settings_path, mode='w+') as credenitals_file:
            json.dump(obj=state,fp=credenitals_file)

        return json_settings_path

if __name__ == '__main__':

    state_path = StatePath()
    state_path.write_to_settings(state={'value':'key'})
