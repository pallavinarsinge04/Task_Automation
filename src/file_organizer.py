import os
import shutil

def organize_files(target_directory):
    """
    Scans the target directory and sorts files into categorized subfolders based on file extension.
    """
    if not os.path.exists(target_directory):
        print(f"[Error] Directory '{target_directory}' does not exist.")
        return 0

    # Define file extension mappings
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx'],
        'Archives': ['.zip', '.tar', '.gz', '.7z', '.rar'],
        'Code_Files': ['.py', '.js', '.html', '.css', '.json', '.cpp', '.c']
    }

    files_moved = 0

    # Iterate over all items in the target directory
    for item in os.listdir(target_directory):
        file_path = os.path.join(target_directory, item)

        # Process only files (ignore directories)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False

            # Match extension to category
            for category, extensions in categories.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(target_directory, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, item))
                    files_moved += 1
                    moved = True
                    break

            # Fallback for uncategorized extension types
            if not moved and file_extension:
                dest_folder = os.path.join(target_directory, 'Others')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, item))
                files_moved += 1

    print(f"[Success] Organized {files_moved} file(s) in '{target_directory}'.")
    return files_moved