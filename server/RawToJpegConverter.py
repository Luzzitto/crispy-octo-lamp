import rawpy
import os
import sys

def extract_thumb(file_path, folder_dest):
    img_name, img_ext = os.path.splitext(os.path.basename(file_path))
    with rawpy.imread(file_path) as raw:
        try:
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            print("No thumbnail found")
        else:
            if thumb.format == rawpy.ThumbFormat.JPEG:
                with open(folder_dest + img_name + ".jpg", "wb") as f:
                    f.write(thumb.data)

extract_thumb(str(sys.argv[1]), str(sys.argv[2]))
