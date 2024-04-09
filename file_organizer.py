import argparse
import shutil
import os

def ifile_type(file_path):
    """Identify the type of the file based on its extension."""
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()  # Convert to lowercase for case-insensitivity

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    document_extensions = ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']
    python_extension = ['.py']

    if extension in image_extensions:
         return 'image'
    elif extension in document_extensions:
         return 'document'
    elif extension in video_extensions:
         return 'video'
    elif extension in python_extension:
         return 'python_file'
    else:
         return 'other'

def move_file(file_path, destination_dir):
    """Move a file to the specified destination directory."""
    try:
        shutil.move(file_path, destination_dir)
        print(f"Moved file: {file_path} to {destination_dir}")
    except Exception as e:
        print(f"Error moving file {file_path}: {str(e)}")

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='File Organizer')
    parser.add_argument('directory', type=str, help='Directory to organize')
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    directory = args.directory

    # Validate directory path
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return

    # Proceed with organizing files in the specified directory
    print(f"Organizing files in directory: {directory}")
    # Create directories for organizing files
    image_dir = os.path.join(directory, "Imagesss")
    document_dir = os.path.join(directory, "Documentsss")
    other_dir = os.path.join(directory, "Othersss")

    for dir_path in [image_dir, document_dir, other_dir]:
        os.makedirs(dir_path, exist_ok=True)

    # Organize files in the specified directory
    print(f"Organizing files in directory: {directory}")

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_type = ifile_type(file_path)
            # Move file to the appropriate directory based on its type
            if file_type == 'image':
                move_file(file_path, image_dir)
            elif file_type == 'document':
                move_file(file_path, document_dir)
           
            else:
                move_file(file_path, other_dir)

# Test the function
#file_path = r'C:\Users\satya\Documents\Pythonintern\File_organiserrrr_project\test_dicty\turr.txt'
#file_type = ifile_type(file_path)
#print(f"The file type of {file_path} is: {file_type}")

if __name__ == '__main__':
    main()
