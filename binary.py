import os
import shutil


class BinaryFileManager:
    @staticmethod
    def read(file_path: str):
        """Reads the content of a binary file."""
        with open(file_path, 'rb') as file:
            return file.read()

    @staticmethod
    def write(file_path: str, content: bytes):
        """Writes content to a binary file, overwriting existing content."""
        with open(file_path, 'wb') as file:
            file.write(content)

    @staticmethod
    def append(file_path: str, content: bytes):
        """Appends content to a binary file."""
        with open(file_path, 'ab') as file:
            file.write(content)

    @staticmethod
    def exclusive_append(file_path: str, content: bytes):
        """Appends content to a binary file only if the file doesn't exist."""
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as file:
                file.write(content)
        else:
            raise FileExistsError("File already exists.")

    @staticmethod
    def delete(file_path: str):
        """Deletes the binary file."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"{file_path} does not exist.")

    @staticmethod
    def move(file_path: str, destination: str):
        """Moves the binary file to a new location."""
        if os.path.exists(file_path):
            shutil.move(file_path, destination)
        else:
            raise FileNotFoundError(f"{file_path} does not exist.")
