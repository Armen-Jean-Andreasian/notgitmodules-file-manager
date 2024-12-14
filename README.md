# FileManager [Not Gitmodule]

---
## What's Not Gitmodule?

[Read](https://github.com/Armen-Jean-Andreasian/not_gitmodules)

---
## Core Functionality

The `FileManager` and `BinaryFileManager` classes provide core file management capabilities to handle text and binary files, respectively. These classes include methods for:

1. **Reading**: Retrieve the content of a file.
2. **Writing**: Overwrite an existing file with new content.
3. **Appending**: Add content to the end of an existing file.
4. **Exclusive Append**: Add content to a file only if it does not already exist.
5. **Deleting**: Remove a file from the system.
6. **Moving**: Move a file to a different location.

---
### Text File Operations (`FileManager`)
The `FileManager` class is designed to handle text files. It works with standard text encoding (e.g., UTF-8) and provides the following methods:
- `read`: Reads the content of a text file.
- `write`: Writes content to a text file, overwriting any existing content.
- `append`: Appends content to the end of a text file.
- `exclusive_append`: Appends content only if the file doesn't already exist.
- `delete`: Deletes a text file from the system.
- `move`: Moves a text file to a new location.

---
### Binary File Operations (`BinaryFileManager`)
The `BinaryFileManager` class handles binary file operations, such as reading and writing non-textual data. This class is particularly useful for handling files like images, videos, or any other binary data. The provided methods are similar to `FileManager` but designed for binary files:
- `read`: Reads the content of a binary file.
- `write`: Writes binary data to a file, overwriting any existing content.
- `append`: Appends binary data to an existing file.
- `exclusive_append`: Appends binary data only if the file does not already exist.
- `delete`: Deletes a binary file from the system.
- `move`: Moves a binary file to a new location.

---

## Usage
### Example Usage with `not_gitmodules`:

With `not_gitmodules`, the file manager module can be easily added to your project by including it in your `not_gitmodules.yaml` file. Once the module is added and installed, you can directly use it within your code as shown below:

1. Modify not_gitmodules.yaml file.

```yaml
file_manager_module: https://github.com/Armen-Jean-Andreasian/notgitmodules-file-manager-py
```

2. Install
```bash
not_gitmodules
```

3. Use
```python
from my_gitmodules.file_manager_module import BinaryFileManager
from my_gitmodules.file_manager_module import FileManager

# Usage
FileManager.write("example.txt", "Hello, world!")
BinaryFileManager.write("example.bin", b'\x00\x01\x02')
```

### Usage with `gitmodules`:
For `gitmodules`, follow the usual steps to add the repository as a submodule to your project and use it as needed.


## Typehint

As this is a module you may be need to typehint. 

- For CPython it's pretty straightforward

```python
# implementation 1
from typing import Protocol, Callable


class BinaryFileManager(Protocol):
    read: Callable
    write: Callable
    append: Callable
    exclusive_append: Callable
    delete: Callable
    move: Callable
```

or you wish you can mention the args as well in Callable:

```python
# implementation 2
from typing import Protocol, Callable

class BinaryFileManager(Protocol):
    read: Callable[[str], bytes]
    write: Callable[[str, bytes], None]
    append: Callable[[str, bytes], None]
    exclusive_append: Callable[[str, bytes], None]
    delete: Callable[[str], None]
    move: Callable[[str, str], None]
```

- For MyPy you need:

```python
from typing import Protocol


class BinaryFileManager(Protocol):
    def read(self, file_path: str) -> bytes:
        ...

    def write(self, file_path: str, content: bytes) -> None:
        ...

    def append(self, file_path: str, content: bytes) -> None:
        ...

    def exclusive_append(self, file_path: str, content: bytes) -> None:
        ...

    def delete(self, file_path: str) -> None:
        ...

    def move(self, file_path: str, destination: str) -> None:
        ...
```

---

## P.S.

This module provides a simple, modular, and extensible solution for managing files, which can be easily integrated into projects using either `not_gitmodules` or `gitmodules`.
