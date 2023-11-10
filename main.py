import os
import shutil

path = input("Input your path: ")

file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".doc", ".xls", ".csv", ".odt"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".eps"],
    "Audio": [".m4a", ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma"],
    "Video": [".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js", ".json", ".sql", ".php"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "3D Models": [".f3d", ".STL", ".blend", ".obj"],
    "Spreadsheets": [".xlsx", ".ods"],
    "Presentations": [".ppt", ".key", ".sxi"],
    "Ebooks": [".epub", ".mobi", ".azw", ".djvu"],
    "Text": [".rtf", ".log", ".md", ".tex", ".yml"],
    "Database": [".db", ".sqlite", ".dbf", ".sql", ".mdb"],
    "Executable": [".exe", ".bat", ".sh", ".msi", ".app"],
    "Web": [".html", ".css", ".js", ".php", ".xml", ".asp"],
    "Config": [".yaml", ".json", ".xml", ".ini", ".cfg"],
    "Images Raw": [".raw", ".nef", ".dng", ".cr2"],
    "Compressed Audio": [".flac", ".ape"],
    "Compressed Video": [".mkv", ".avi"],
    "GIS Data": [".shp", ".kml", ".gpx"],
    "Fonts": [".ttf", ".otf"],
    "CAD Drawings": [".dwg", ".dxf"],
}

file_extensions = {ext: category for category, ext_list in file_categories.items() for ext in ext_list}

file_extensions["Other"] = []

file_names = os.listdir(path)

for file in file_names:
    file_extension = os.path.splitext(file)[1].lower()

    if file_extension in file_extensions:
        category = file_extensions[file_extension]
    else:
        category = "Other"

    folder_name = category + " folder"
    folder = os.path.join(path, folder_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    source_path = os.path.join(path, file)
    destination_path = os.path.join(folder, file)

    if not os.path.exists(destination_path):
        shutil.move(source_path, destination_path)
