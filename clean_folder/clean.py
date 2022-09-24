from dataclasses import replace
from pathlib import Path
import sys
import os


from .const import translit, FilesDirAndExt


def normalize(file_name):
    for char in file_name:
        if not char.isnumeric() and not char.isalpha():
            yield '_'
            continue

        translit_char = translit.get(char.lower())
        yield char \
            if translit_char is None else translit_char \
            if char.islower() else translit_char.title()


def sorting():
    main_directory = sys.argv[1]

    for file_structure in FilesDirAndExt:
        file_path = os.path.join(
            main_directory, file_structure.value.directory
        )

        if not os.path.exists(file_path):
            os.makedirs(file_path)

    for file in os.listdir(main_directory):
        file_name, file_ext = os.path.splitext(file)
        file_path = os.path.join(main_directory, file)
        norm_file_name = ''.join(normalize(file_name))
        norm_file_path = os.path.join(main_directory, norm_file_name)

        for file_structure in FilesDirAndExt:
            if any((
                    (file_ext in file_structure.value.extensions),
                    (
                        (not file_structure.value.extensions) \
                         and os.path.isfile(file_path)
                    )
            )):
                new_file = os.path.join(
                    main_directory, file_structure.value.directory,
                    norm_file_name
                )
                os.replace(file_path, new_file)
                break
        else:
            os.rename(file_path, norm_file_path)
