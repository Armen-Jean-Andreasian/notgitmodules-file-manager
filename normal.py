import os
import shutil


class FileManager:
    @staticmethod
    def read(file_path: str):
        """Reads the content of a file."""
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write(file_path: str, content: str):
        """Writes content to a file, overwriting existing content."""
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def append(file_path: str, content: str):
        """Appends content to a file."""
        with open(file_path, 'a') as file:
            file.write(content)

    @staticmethod
    def exclusive_append(file_path: str, content: str):
        """Appends content to a file only if the file doesn't exist."""
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)
        else:
            raise FileExistsError("File already exists.")

    @staticmethod
    def delete(file_path: str):
        """Deletes the file."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"{file_path} does not exist.")

    @staticmethod
    def move(file_path: str, destination: str):
        """Moves the file to a new location."""
        if os.path.exists(file_path):
            shutil.move(file_path, destination)
        else:
            raise FileNotFoundError(f"{file_path} does not exist.")
