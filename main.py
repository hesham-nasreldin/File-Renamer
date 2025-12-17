import streamlit as st
import os


def number_files_in_folder(folder_path, start_number=1):
    if not os.path.isdir(folder_path):
        st.error(f"Error: Folder not found at '{folder_path}'")
        return
    try:
        files = [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        files.sort()
    except Exception as e:
        st.error(f"An error occurred while reading the directory: {e}")
        return

    st.write(f"Found {len(files)} files to rename.")

    current_number = start_number
    renamed = []
    for old_filename in files:
        name, extension = os.path.splitext(old_filename)
        new_filename = f"{str(current_number).zfill(2)}{extension}"

        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
            renamed.append(f"Renamed: '{old_filename}' -> '{new_filename}'")
            current_number += 1
        except Exception as e:
            st.error(f"Could not rename '{old_filename}'. Error: {e}")

    if renamed:
        st.success("Renaming process complete!")
        for msg in renamed:
            st.write(msg)


st.title("File Renamer")

st.write(
    "Enter the folder path where you want to rename the files. To get the path, you can drag the folder to a text editor or copy it from file explorer."
)

folder_path = st.text_input("Enter the folder path:")

start_number = 1

confirm = st.checkbox("Is it okay to rename the files?")

if st.button("Rename Files"):
    if not confirm:
        st.error("Please confirm that it's okay to rename the files.")
    elif folder_path:
        number_files_in_folder(folder_path, int(start_number))
    else:
        st.error("Please enter a folder path.")
