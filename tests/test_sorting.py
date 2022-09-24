import os
import pytest
from enum import Enum
from shutil import rmtree

from clean_folder.const import FilesDirAndExt
from clean_folder.clean import sorting


class WorkDirAndFiles(Enum):
    WORKDIR = 'trash'
    DOC_FILE = 'hello.txt'
    NOT_RECOGNIZE_FILE = 'hello.py'
    TEST_DIR = 'traЇ'
    TEST_RENAME_DIR = 'traYi'


workdir = WorkDirAndFiles.WORKDIR.value
doc_dir = FilesDirAndExt.DOCS.value.directory
notrec_dir = FilesDirAndExt.NOT_RECOGNIZE.value.directory
test_dir = WorkDirAndFiles.TEST_DIR.value
test_rename_dir = WorkDirAndFiles.TEST_RENAME_DIR.value

doc_file = WorkDirAndFiles.DOC_FILE.value
notrec_file = WorkDirAndFiles.NOT_RECOGNIZE_FILE.value

doc_file_path = os.path.join(workdir, doc_file)
notrec_file_path = os.path.join(workdir, notrec_file)
test_dir_path = os.path.join(workdir, test_dir)
test_rename_dir_path = os.path.join(workdir, test_rename_dir)


@pytest.fixture()
def test_dir_and_files():
    for tdir in (workdir, test_dir_path):
        os.mkdir(tdir)

    for file in (doc_file_path, notrec_file_path):
        with open(file, 'w') as ftw:
            ftw.write('test')

    yield

    rmtree(workdir)


class TestSorting:
    def test_rename_and_replace(self, test_dir_and_files):
        sorting(workdir)
        assert os.path.isfile(os.path.join(workdir, doc_dir, doc_file))
        assert os.path.isfile(os.path.join(workdir, notrec_dir, notrec_file))
        assert os.path.isdir(test_rename_dir_path)
