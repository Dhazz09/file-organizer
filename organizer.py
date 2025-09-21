import os
import shutil

# Define file categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} → {folder}/")
                    moved = True
                    break

            if not moved:
                target_folder = os.path.join(folder_path, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} → Others/")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    if os.path.exists(folder):
        organize_folder(folder)
        print("✅ Organization complete!")
    else:
        print("❌ Invalid folder path")
