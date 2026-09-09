import os
import shutil

def organize_files(target_directory):
    """Sorts files into subdirectories based on file extensions."""
    if not os.path.exists(target_directory):
        print(f"Error: Directory '{target_directory}' does not exist.")
        return

    extensions = {
        'Images': ['.jpg', '.png', '.jpeg', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.csv'],
        'Archives': ['.zip', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html']
    }

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, ext_list in extensions.items():
                if ext in ext_list:
                    category_dir = os.path.join(target_directory, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_dir, filename))
                    moved = True
                    break
            if not moved:
                other_dir = os.path.join(target_directory, 'Others')
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, filename))
    
    print("Files successfully organized by category!")