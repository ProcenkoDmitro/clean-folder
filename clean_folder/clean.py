from dataclasses import replace
from pathlib import Path
import sys
import os


from .const import translit, FilesDirAndExt


def normalize(name_file):
    norm_name = ""
    for key in translit:
        name_file = name_file.replace(key, translit[key])
    for i in name_file:
        if not i.isnumeric() and not i.isalpha():
            norm_name = norm_name + "_"
        else:
            norm_name = norm_name + i
    return norm_name


def sorting():
    main_directory = sys.argv[1]

    for file_structure in FilesDirAndExt:
        file_path = os.path.join(
            main_directory, file_structure.value.directory
        )

        if not os.path.exists(file_path):
            os.makedirs(file_path)

    for i in os.listdir(main_directory):
        norm_name = normalize(os.path.splitext(i)[0])
        old_name = os.path.join(main_directory, i)
        new_name = os.path.join(main_directory, norm_name + os.path.splitext(i)[1])
        os.rename(old_name, new_name)

    for file in os.listdir(main_directory):
        file_ext = os.path.splitext(file)[-1]
        file_path = os.path.join(main_directory, file)

        for file_structure in FilesDirAndExt:
            if any((
                    (file_ext in file_structure.value.extensions),
                    (
                        (not file_structure.value.extensions) \
                         and os.path.isfile(file_path)
                    )
            )):
                new_file = os.path.join(
                    main_directory, file_structure.value.directory, file
                )
                os.replace(file_path, new_file)
                break

