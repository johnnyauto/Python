import os
import pandas as pd

def traverse_directory(directory, ext, sheet_name):
    # load mapping data from Excel
    mapping_data = pd.read_excel('mapping.xlsx', sheet_name=sheet_name)

    # traverse and replace
    for root, dirs, files in os.walk(directory): # traverse subdirectoryies and files
        for filename in files:
            file_path = os.path.join(root, filename) # get the file path
            print(file_path)

            if filename.endswith(ext): # looking for the target file
                
                # replace original with current
                for index, row in mapping_data.iterrows():
                    original = row['Original']
                    current = row['Current']
                    
                    #with open(file_path, 'r', encoding='utf-8') as file:
                    with open(file_path, 'r') as file:
                        content = file.read()
                    
                    modified_content = content.replace(original, current)
                    print(original, ' -> ', current, '  |  ', file_path)

                    #with open(file_path, 'w', encoding='utf-8') as file:
                    with open(file_path, 'w') as file:
                        file.write(modified_content)

def main():
    sheet_name = input('Please enter the sheet name: ')
    root_directory = input('Please enter the directory: ')
    ext = input('Please enter the target file extension (e.g., .can): ')
    #root_directory = r'D:\OneDrive - Inventec Corp\VectorRepository\Save_vTS\CEM\TU_FrontWiperWash\Temp'
    #ext = '.vtsd'
    traverse_directory(root_directory, ext, sheet_name)

if __name__ == '__main__':
    main()