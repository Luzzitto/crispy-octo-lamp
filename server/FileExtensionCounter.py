import os
import argparse
from collections import defaultdict
from tabulate import tabulate
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

class FileExtensionCounter:
    def __init__(self, path):
        self.path = path
        self.extension_counts= defaultdict(int)
        self.total_files = 0
        self.total_size = 0

    def count_extensions(self):
        if os.path.isdir(self.path):
            for filename in os.listdir(self.path):
                self.total_files += 1
                self.total_size = os.path.getsize(os.path.join(self.path, filename))
                _, file_extension = os.path.splitext(filename)
                if file_extension:
                    self.extension_counts[file_extension] += 1

    def print_counts(self):
        table = [[extension, count] for extension, count in self.extension_counts.items()]
        print(f"Path: {self.path}\n")
        print(tabulate(table, headers=["Extension", "Count"], tablefmt="fancy_grid"))
        print(f"\nTotal Files: {self.total_files}, Size: {convert_size(self.total_size)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of files with each extension in a folder.")
    parser.add_argument("path", help="The path to the folder.")
    args = parser.parse_args()

    counter = FileExtensionCounter(args.path)
    counter.count_extensions()
    counter.print_counts()

