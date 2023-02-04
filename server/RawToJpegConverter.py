import os
import argparse
import threading
import queue
import rawpy 
import shutil
from pathlib import Path


class RawToJpegConverter:
    def __init__(self, source_path, dest_path):
        self.source_path = source_path
        self.dest_path = dest_path
    
    def convert_raw_to_jpeg(self, file_queue):
        while True:
            filename = file_queue.get()
            if filename is None:
                break
            raw_file = Path(self.source_path) / filename
            jpeg_file = Path(self.dest_path) / raw_file.with_suffix('.jpg').name
            with rawpy.imread(raw_file) as raw:
                try:
                    thumb = raw.extract_thumb()
                except rawpy.LibRawNoThumbnailError:
                    print(f"No thumbnail found for {self.raw}")
                    break
                else:
                    if thumb.format == rawpy.ThumbFormat.JPEG:
                        with open(jpeg_file, "wb") as f:
                            f.write(thumb.data)
            
            print(f"Converted {raw_file} to {jpeg_file}")
            file_queue.task_done()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert raw files to JPEG format.")
    parser.add_argument("source_path", help="The path to the folder containing raw files.")
    parser.add_argument("dest_path", help="The path to the folder where the converted JPEG files should be saved.")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads to use for conversion.")
    args = parser.parse_args()

    file_queue = queue.Queue()

    for filename in os.listdir(args.source_path):
        raw_file = Path(args.source_path) / filename
        jpeg_file = Path(args.source_path) / filename.with_suffix('.JPG')
        if jpeg_file.is_file() and raw_file.is_file():
            shutil.copy2(jpeg_file, Path(args.dest_path) / filename)

        if raw_file.suffix == ".CR3":
            file_queue.put(filename)
    
    for i in range(args.threads):
        t = threading.Thread(target=RawToJpegConverter(args.source_path, args.dest_path).convert_raw_to_jpeg, args=(file_queue,))
        t.setDaemon = True
        t.start()
    
    file_queue.join()
    for i in range(args.threads):
        file_queue.put(None)
    
