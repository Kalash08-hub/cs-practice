from pathlib import Path
import os

def count_by_extension(paths):

    count_extension = {}

    for path in paths:
        extension = Path(path.file_name).suffix.lower()

        count_extension[extension] = count_extension.get(extension, 0) + 1

    return count_extension

def deepest_path(paths):

    count_deepest = {}

    for path in paths:
        name = Path(path.file_name)
        count_deepest[name] = count_deepest.get(name, 0) + 1

    return count_deepest

def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes:.2f} Б"