import os
import shutil

def arrange_files(main_folder):
    files = os.listdir(main_folder)
    
    moved_files_count = 0
    for file in files:
        source_path = os.path.join(main_folder , file)
        if os.path.isfile(source_path):
            ext= file.split('.')[-1]

            destination_path = os.path.join(main_folder , ext.title()) #if any below extention will not match mean it will create one new folder by using 3 letters of extention
            
            if ext in ('txt'):
                destination_path = os.path.join(main_folder,'Textfiles')
            elif ext in ('mp3','mp4','wav'):
                destination_path = os.path.join(main_folder,'Music_&_Vedios')
            elif ext in ('pdf'):
                destination_path= os.path.join(main_folder,'PDFfiles')
            elif ext in ('doc','docx'):
                destination_path = os.path.join(main_folder,'Documents')
            elif ext in ('jpg','png','jpeg','gif'):
                destination_path = os.path.join(main_folder ,'Images')
            
            base, ext = os.path.splitext(file)
            i = 0
            
            while os.path.exists(os.path.join(destination_path,f"{base}({i}){ext}")):
                i += 1
            
            new_destination_path = os.path.join(destination_path, f"{base}({i}){ext}")

            if os.path.exists(destination_path):
                shutil.move(source_path,new_destination_path)
                moved_files_count += 1
            else:
                os.makedirs(destination_path)
                shutil.move(source_path, new_destination_path)
                moved_files_count += 1

    if moved_files_count > 0:
        print('Job is done successfully Files are organized.')
        print('Number of files organized:' , moved_files_count)
    else:
        print('No files are there to organize')


while True:
    main_folder_path = input("Enter the Main folder path to arrange files: ")
    if os.path.exists(main_folder_path):
        break
    else:
        print("Invalid main folder path Please try again")
    
arrange_files(main_folder_path)
