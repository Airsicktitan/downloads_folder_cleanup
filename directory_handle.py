from pathlib import Path
import os
import shutil as s

downloads_path = str(Path.home() / "Downloads")
unknown_types = fr'{downloads_path}\UnknownTypes'
pdfs = fr'{downloads_path}\PDFs'
docs = fr'{downloads_path}\Documents'
png = fr'{downloads_path}\Pictures'
exe = fr'{downloads_path}\Apps'
zip = fr'{downloads_path}\Zipped'
mp3 = fr'{downloads_path}\Downloaded Music'

def make_dir() -> None:
    make_Dir(unknown_types)
    make_Dir(pdfs)
    make_Dir(docs)
    make_Dir(png)
    make_Dir(exe)
    make_Dir(zip)
    make_Dir(mp3)


def make_Dir(dir) -> None:
    if(os.path.exists(dir)):
       print("Folder already exists")
    else:
        print(f'Creating directory {dir} ...')
        os.mkdir(dir)


def categorize_file(filename) -> str:
    get_category = lambda ext: {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code",
        ".mp3": "MP3",
        ".png": "PNG",
        ".pdf": "PDF",
        ".exe": "Windows Application",
        ".zip": "ZIP File"
        }.get(ext, "Unknown")
    return get_category(filename[filename.rfind("."):])


def compare_extension(ext, item) -> None:
    if(ext in unknown_types):
        print(f'moving {ext} file extension to {unknown_types}')
        s.move(fr'{downloads_path}\{item}', unknown_types)
    elif(ext in pdfs):
        print(f'moving {ext} file extension to {pdfs}')
        s.move(fr'{downloads_path}\{item}', pdfs)
    elif(ext in docs or ext.lower() == 'text'):
        print(f'moving {ext} file extension to {docs}')
        s.move(fr'{downloads_path}\{item}', docs)
    elif(ext.lower() == 'png'):
        print(f'moving {ext} file extension to {png}')
        s.move(fr'{downloads_path}\{item}', png)
    elif(ext.lower() == 'windows application'):
        print(f'moving {ext} file extension to {exe}')
        s.move(fr'{downloads_path}\{item}', exe)
    elif(ext.lower() == 'zip file'):
        print(f'moving {ext} file extension to {zip}')
        s.move(fr'{downloads_path}\{item}', zip)
    elif(ext.lower() == 'mp3'):
        print(f'moving {ext} file extension to {mp3}')
        s.move(fr'{downloads_path}\{item}', mp3)
    else:
        print(f'{ext = } folder not found')

def send_item_to_compare() -> str:
    dir_list = os.listdir(downloads_path)
    for item in dir_list:
        if(os.path.isdir(fr'{downloads_path}\{item}')):
            print("Item is a Folder")
        else:
            extension = categorize_file(item)
            compare_extension(extension, item)