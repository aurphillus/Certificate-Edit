import editor as ed
import filehandling as fh
import configuration as conf
import os
#load configuration

def controller():
    print("#. Creating/Loading configuration file")
    try:
        config = conf.load_config()
    except Exception as e:
        print(f"Error loading configuration.")
        print(f"Exiting....")
        return False
    print("#. Configuration Loading complete")
    
    print('#. Checking directoriy configuration')
    
    directory = [config['input_directory'],config['output_directory'],config['logs_directory'],config['default_directory']]
    for dir in directory:
        if not fh.check_directory(config['parentdirectory'],dir):
            fh.create_directory(config['parentdirectory'],dir)
    
    print("#. Directory configuration complete")
    
    if not os.path.exists(os.path.join(config['default_directory'],config['transparentbackground'])):
        note = "Due to a problem in downloading images through python, please download the transparent image manually from the given link:\nhttps://github.com/aurphillus/Certificate-Edit/blob/master/transparent.png\nor\nhttps://pasteboard.co/JiXOlCH.png\nEnsure to name the file 'transparent.png' and place it under 'default' folder.\n"
        print("You can find this message including the link at note.txt")
    
        with open('note.txt','w') as n:
            n.write(note)
        print("Restart the program after downloading and placing the file.\n**If already done the steps ensure to check the name of the file**")
        return False
    
    print("#. Required dependencies check complete")
    
    print("####################")
    
    print("Place the images under ingest folder")
    print("When complete press Y to contine else press N to exit the program")
    value = input("Enter response: ")
    
    if value == 'Y' or value =='y' or value =='yes':
        try:
            files = fh.load_files(parent_directory=config['parentdirectory'],accepted_extensions=config['extensions'],path=config['input_directory'])
            for file in files:
                file_split= file.split('\\')
                file_name = file_split[-1]
                # os.path.join(config['input_directory'],file)
                edit_img = ed.image_edit(original=os.path.join(config['parentdirectory'],file),basewidth=int(config['basewidth']),background=os.path.join(config['parentdirectory'],config['default_directory'],config['transparentbackground']),save_name=os.path.join(config['parentdirectory'],config['output_directory'],file_name))
                
        except Exception as e:
            print(f"Exception occured {e}")
            return False
    else:
        return False
    
if __name__ == '__main__':
    controller()
    