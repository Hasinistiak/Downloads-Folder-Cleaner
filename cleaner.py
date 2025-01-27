import os
import shutil
from watchdog.observers import Observer
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler

downloads_folder = 'C:/Users/ENAN/Downloads'

files_in_downloads = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]


file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Docs': ['.pdf', '.docx', '.txt', '.pptx', '.json', '.md'],
    'Installers': ['.exe', '.msi'],
    'Zips': ['.zip', '.tar', '.gz', '.tar.xz'],
}


for category in file_categories:
    category_folder = os.path.join(downloads_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

def move_file(file, category_folder):
    file_path = os.path.join(downloads_folder, file)
    folder_path = os.path.join(category_folder, file)
    shutil.move(file_path, folder_path)

for file in files_in_downloads:
    file_extension = os.path.splitext(file)[1].lower()
    moved = False

    for category, extensions in file_categories.items():
        if file_extension in extensions:
            category_folder = os.path.join(downloads_folder, category)
            move_file(file, category_folder)
            moved = True
            break

    
    if not moved:
        others_folder = os.path.join(downloads_folder, 'others')
        if not os.path.exists(others_folder):
            os.makedirs(others_folder)

        if file_extension != '.py':
            move_file(file, others_folder)
