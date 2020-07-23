import editor as ed
import filehandling as fh
import configuration as conf
import os
import progressbar
import logging


def controller():
    try:
        config = conf.load_config()
    except Exception as e:
        print(f"error loading configuration file, error: {e}")
        return False
    log_file = os.path.join(config['parentdirectory'],config['logs_directory'],config['logfile'])
    print(log_file)
    logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s:%(process)d:%(levelno)s:%(message)s')

    
    logging.info(f"directory configuration check.")    
    directory = [config['input_directory'],config['output_directory'],config['logs_directory'],config['default_directory']]
    logging.debug(f"directory configs loaded from config file and stored in memory.")
    
    for dir in directory:
        logging.debug(f"checking for directory name: {dir}.")
        if not fh.check_directory(config['parentdirectory'],dir):
            logging.debug(f"directory: {dir} not present")
            fh.create_directory(config['parentdirectory'],dir)
            logging.info(f"directory: {dir} created successfully.")
            
    
    logging.info(f"directory configuration complete.")
    
    logging.info(f"checking for file: {config['transparentbackground']} to be present at {os.path.exists(os.path.join(config['default_directory']))}")
    if not os.path.exists(os.path.join(config['default_directory'],config['transparentbackground'])):
        logging.debug(f"{config['transparentbackground']} not found.")        
        note = "Due to a problem in downloading images through python, please download the transparent image manually from the given link:\nhttps://github.com/aurphillus/Certificate-Edit/blob/master/transparent.png\nor\nhttps://pasteboard.co/JiXOlCH.png\nEnsure to name the file 'transparent.png' and place it under 'default' folder.\n"
        print("You can find this message including the link at note.txt")
    
        with open('note.txt','w') as n:
            n.write(note)
        logging.debug(f"note generated.")
        print("Restart the program after downloading and placing the file.\n**If already done the steps ensure to check the name of the file**")
        return False
    
    logging.info(f"dependencies check complete.")
    
    
    print("Place the images under ingest folder")
    print("When complete press Y to contine else press N to exit the program")
    value = input("Enter response: ")
    
    if value == 'Y' or value =='y' or value =='yes':
        logging.debug(f"User entered Y, process started.")
        
        try:
            files = fh.load_files(parent_directory=config['parentdirectory'],accepted_extensions=config['extensions'],path=config['input_directory'])
            bar = progressbar.ProgressBar(maxval=len(files)-1).start()

            for idx, file in enumerate(files):
                file_split= file.split('\\')
                file_name = file_split[-1]
                # os.path.join(config['input_directory'],file)
                logging.debug(f"file: {file_name} getting converted.")
                edit_img = ed.image_edit(original=os.path.join(config['parentdirectory'],file),basewidth=int(config['basewidth']),background=os.path.join(config['parentdirectory'],config['default_directory'],config['transparentbackground']),save_name=os.path.join(config['parentdirectory'],config['output_directory'],file_name))
                logging.debug(f"file: {file_name} converted succesfully and stored at {os.path.join(config['parentdirectory'],config['output_directory'],file_name)}.")
                bar.update(idx)
            
            logging.debug(f"All files have been processed.")
            
            
        except Exception as e:
            logging.error(f"error converting files, error: {e}")
            print(f"Terminating program due to error. Check log file at {os.path.join(config['parentdirectory'],config['logs_directory'],config['logfile'])}")
            return False
    else:
        return False
    
    
if __name__ == '__main__':
    controller()
    