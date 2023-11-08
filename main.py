import os
import shutil

path = r"C:/Users/BLABLABLA"

fileExt = [
    ".pdf", ".m4a", ".mp3", ".png", ".txt", ".py", ".pptx", ".docx", ".mp4",
    ".jpg", ".csv", ".xlsx", ".html", ".xml", ".gif", ".jpeg", ".doc", ".xls",
    ".csv", ".json", ".java", ".cpp", ".zip", ".rar", ".avi", ".mkv", ".wav",
    ".flac", ".html", ".css", ".js", ".log", ".sql", ".php", ".ppt", ".odt",
    ".ods", ".json", ".sql", ".yaml", ".json", ".xml", ".zip", ".jpeg", ".exe",
    ".f3d", ".STL", ".blend"
]

fileName = os.listdir(path)

for file in fileName:
    for ext in fileExt:
        if file.endswith(ext):
            folder_name = ext.lstrip('.').replace('.', ' ').capitalize() + " folder"
            folder = os.path.join(path, folder_name)

            if not os.path.exists(folder):
                os.makedirs(folder)

            source_path = os.path.join(path, file)
            destination_path = os.path.join(folder, file)

            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
