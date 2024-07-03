import os
import shutil
import argparse
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: The source directory '{source_dir}' does not exist.")
            return
        
        # Check if destination directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"The destination directory '{dest_dir}' was created.")

        # Walk through the source directory
        for root, dirs, files in os.walk(source_dir):
            # Preserve the directory structure in the destination
            relative_path = os.path.relpath(root, source_dir)
            dest_path = os.path.join(dest_dir, relative_path)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            for file in files:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_path, file)

                # If the file already exists in the destination, append a timestamp
                if os.path.exists(dest_file_path):
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    base, ext = os.path.splitext(file)
                    dest_file_path = os.path.join(dest_path, f"{base}_{timestamp}{ext}")

                # Copy the file
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied '{src_file_path}' to '{dest_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Backup files from source to destination directory.')
    parser.add_argument('source', type=str, help='The source directory to backup')
    parser.add_argument('destination', type=str, help='The destination directory for backup')
    args = parser.parse_args()

    backup_files(args.source, args.destination)

if __name__ == '__main__':
    main()
