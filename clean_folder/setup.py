from setuptools import setup

setup(
    name='cleaner',
    version='1',
    description='normalize_your_dirs',
    url='http://github.com/dummy_user/useful',
    author='Procenko_Dmitro',
    author_email='procenkod@ukr.net',
    packages = ['clean'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorting']}
    )
