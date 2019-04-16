from PIL import Image
from PIL import ImageSequence
from PIL import TiffImagePlugin
import PIL

with TiffImagePlugin.AppendingTiffWriter(dir_name + '.tiff') as tf:     # dir_name = Final name of the merged images
    for i in list_dir:        # List of those images
        tmp_im = PIL.Image.open(path_tmp+'/'+i)     #path_tmp = Path of your image directory
        tmp_im.load()
        list_im = tmp_im        
        list_im.save(tf)
        tf.newFrame()
        tmp_im.close()
