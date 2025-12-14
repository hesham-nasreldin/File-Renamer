import os

def number_files_in_folder(folder_path, start_number=1):
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at '{folder_path}'")
        return
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        files.sort()
    except Exception as e:
        print(f"An error occurred while reading the directory: {e}")
        return

    print(f"Found {len(files)} files to rename.")

    current_number = start_number
    for old_filename in files:
        name, extension = os.path.splitext(old_filename)
        new_filename = f"{str(current_number).zfill(2)}{extension}"

        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{old_filename}' -> '{new_filename}'")
            current_number += 1
        except Exception as e:
            print(f"Could not rename '{old_filename}'. Error: {e}")

    print("\nRenaming process complete!")


if __name__ == "__main__":
    target_folder = "./test_files"
    number_files_in_folder(target_folder, start_number=1)