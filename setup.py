from setuptools import setup

setup(
    name='cleaner',
    version='1.1a',
    description='normalize_your_dirs',
    url='https://github.com/ProcenkoDmitro/clean_folder',
    author='Procenko_Dmitro',
    author_email='procenkod@ukr.net',
    packages = ['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorting']}
    )
