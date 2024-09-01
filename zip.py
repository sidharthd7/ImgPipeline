import argparse
import os
import zipfile

def zip_folder (input_folder, output_zip):
    if not os.path.exists(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        return
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, input_folder))
                
                
    print(f"Folder '{input_folder}' has been zipped successfully into 'output_zip'.")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zip the contents of a folder.")
    parser.add_argument("input_folder", type=str, help="Path to the folder to zip.")
    parser.add_argument("output_zip", type=str, help="Path for the output zip file.")
    
    args = parser.parse_args()
    
    
    zip_folder(args.input_folder, args.output_zip)