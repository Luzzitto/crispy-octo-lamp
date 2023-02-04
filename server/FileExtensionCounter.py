import os
import argparse
from collections import defaultdict
from tabulate import tabulate

class FileExtensionCounter:
    def __init__(self, path):
        self.path = path
        self.extension_counts= defaultdict(int)
        self.total_files = 0

    def count_extensions(self):
        if os.path.isdir(self.path):
            for filename in os.listdir(self.path):
                self.total_files += 1
                _, file_extension = os.path.splitext(filename)
                if file_extension:
                    self.extension_counts[file_extension] += 1

    def print_counts(self):
        table = [[extension, count] for extension, count in self.extension_counts.items()]
        print(f"Path: {self.path}\n")
        print(tabulate(table, headers=["Extension", "Count"], tablefmt="fancy_grid"))
        print(f"\nTotal Files: {self.total_files}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of files with each extension in a folder.")
    parser.add_argument("path", help="The path to the folder.")
    args = parser.parse_args()

    counter = FileExtensionCounter(args.path)
    counter.count_extensions()
    counter.print_counts()

