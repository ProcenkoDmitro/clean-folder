from setuptools import setup

setup(
    name='hw6_goit',
    version='1',
    description='normalize_your_dirs',
    url='http://github.com/dummy_user/useful',
    author='Procenko_Dmitro',
    author_email='procenkod@ukr.net',
    packages = ['hw6_goit'],
    entry_points={'console_scripts': ['clean-folder = clean-folder.clean:sorting']}
    )
