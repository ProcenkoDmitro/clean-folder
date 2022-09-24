from enum import Enum
from collections import namedtuple


translit = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'ґ': 'g',
    'д': 'd',
    'е': 'e',
    'є': 'ye',
    'ж': 'j',
    'з': 'z',
    'и': 'i',
    'і': 'i',
    'ї': 'yi',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ь': '',
    'ю': 'yu',
    'я': 'ya',
}


FilesStructure = namedtuple('FilesStructure', ('directory', 'extensions'))


class FilesDirAndExt(Enum):
    DOCS = FilesStructure(
        "docs",
        {'.doc', '.docx', '.txt', '.pdf', '.xlxs', '.pptx',}
    )
    ZIPS = FilesStructure(
        "zips",
        {'.zip', '.gz', '.tar',}
    )
    IMAGES = FilesStructure(
        "images",
        {'.jpg', '.png', '.png', '.svg', '.jfif', '.gif',}
    )
    VIDEOS = FilesStructure(
        "videos",
        {'.avi', '.mp4', '.mov', '.mkv',}
    )
    MUSICS = FilesStructure(
        "musics",
        {'.mp3', '.ogg', '.wav', '.amr',}
    )
    NOT_RECOGNIZE = FilesStructure(
        "not_recognize",
        set()
    )
