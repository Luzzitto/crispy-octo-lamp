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

if __name__ == "__main__":
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    for filename in os.listdir(source_folder):
        src_file = os.path.join(source_folder, filename)
        print(src_file)
