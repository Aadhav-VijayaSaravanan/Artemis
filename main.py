import os
import shutil

def organize_files(source_path, extensions):
    if not os.path.exists(source_path):
        print("Source directory does not exist.")
        return

    for ext in extensions:
        ext = ext.lower()
        folder_name = ext.lstrip('.').replace('.', ' ').capitalize() + " folder"
        folder = os.path.join(source_path, folder_name)

        if not os.path.exists(folder):
            os.makedirs(folder)

    for root, dirs, files in os.walk(source_path):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            if ext in extensions:
                folder_name = ext + " files"
                folder = os.path.join(source_path, folder_name)
                source_path_file = os.path.join(root, file)
                destination_path = os.path.join(folder, file)

                if not os.path.exists(destination_path):
                    shutil.move(source_path_file, destination_path)
                    print(f"Moved: {file} to {folder_name}")

if __name__ == "__main__":
    source_path = input("Enter the source directory path: ")
    extensions = [
        ".pdf", ".m4a", ".mp3", ".png", ".txt", ".py", ".pptx", ".docx", ".mp4",
        ".jpg", ".csv", ".xlsx", ".html", ".xml", ".gif", ".jpeg", ".doc", ".xls",
        ".csv", ".json", ".java", ".cpp", ".zip", ".rar", ".avi", ".mkv", ".wav",
        ".flac", ".html", ".css", ".js", ".log", ".sql", ".php", ".ppt", ".odt",
        ".ods", ".json", ".sql", ".yaml", ".json", ".xml", ".zip", ".jpeg", ".exe",
        ".f3d", ".STL", ".blend"
    ]
    organize_files(source_path, extensions)
