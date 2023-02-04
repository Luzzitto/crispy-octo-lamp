import rawpy
import os

def extract_thumb(file_path):
    img_name, img_ext = os.path.splitext(file_path)
    with rawpy.imread(file_path) as raw:
        try:
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            print("No thumbnail found")
        else:
            if thumb.format == rawpy.ThumbFormat.JPEG:
                with open(img_name + ".jpg", "wb") as f:
                    f.write(thumb.data)

extract_thumb('IMG_4934.CR3')