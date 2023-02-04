import rawpy
import os
import sys
from tqdm import tqdm

def extract_thumb(file_path, folder_dest):
    img_name, img_ext = os.path.splitext(os.path.basename(file_path))
    with rawpy.imread(file_path) as raw:
        try:
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            tqdm.write("No thumbnail found")
        else:
            if thumb.format == rawpy.ThumbFormat.JPEG:
                with open(folder_dest + img_name + ".jpg", "wb") as f:
                    f.write(thumb.data)

if __name__ == "__main__":
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    counter = 0

    for filename in tqdm(os.listdir(source_folder), desc="dirs"):
        src_file = os.path.join(source_folder, filename)
        if os.path.splitext(filename)[1] != ".CR3":
            continue
        counter += 1
        extract_thumb(src_file, destination_folder)

    print(f"Files completed: {counter}")
