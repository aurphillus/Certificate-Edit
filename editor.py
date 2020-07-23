from PIL import Image, ImageFilter
import os



def image_edit(original,basewidth,background,save_name):
    try:
        base_img = Image.open(original)
        bg = Image.open(background)
        wpercent = (basewidth/float(base_img.size[0]))
        hsize = int((float(base_img.size[1])*float(wpercent)))
        new_img = base_img.resize((basewidth,hsize), Image.ANTIALIAS)
        # new_img.save(os.path.join(temp_location,temp_name))
        
        w1, h1 = int(bg.size[0]/2), int(bg.size[1]/2) 
        w2, h2 = int(new_img.size[0]/2), int(new_img.size[1]/2)
        
        wo = w1 - w2
        ho = h1 - h2
        size = (wo,ho)
        
        bg.paste(new_img,size)
        if os.path.exists(save_name):
            print(f"File already exists: {save_name}")
        else:
            bg.save(save_name)
            print(f"File saved at: {save_name}")
            
        return True
    
    except Exception as e:
        print(f"#. Faced exception loading base image: {e}")
        return False

