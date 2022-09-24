from enum import Enum
from collections import namedtuple


translit = {
    'а': 'a', 'А': 'A',
    'б': 'b', 'Б': 'B',
    'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G',
    'ґ': 'g', 'Ґ': 'G',
    'д': 'd', 'Д': 'D',
    'е': 'e', 'Е': 'E',
    'є': 'ye', 'Є': 'Ye',
    'ж': 'j', 'Ж': 'J' ,
    'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I',
    'і': 'i', 'І': 'I',
    'ї': 'yi', 'Ї': 'Yi',
    'й': 'y', 'Й': 'Y',
    'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L',
    'м': 'm', 'М': 'M',
    'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O',
    'п': 'p', 'П': 'P',
    'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S',
    'т': 't', 'Т': 'T',
    'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F',
    'х': 'h', 'Х': 'H',
    'ц': 'c', 'Ц': 'C',
    'ч': 'ch', 'Ч': 'Ch',
    'ш': 'sh', 'Ш': 'Sc',
    'щ': 'sch', 'Щ': 'Sch',
    'ь': '',
    'ю': 'yu', 'Ю': 'Yu',
    'я': 'ya', 'Я': 'Ya'
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
