import argparse
import os
import sys
from datetime import datetime
from log_to_db import log_message
from fun import get_files

class CompareFolders:
    def __init__(self, main, copy, action_type):
        self.start_time = start_time
        self.main = main if os.path.isdir(main) else Exception(f"{main} is not a directory")
        self.copy = copy if os.path.isdir(copy) else Exception(f"{copy} is not a directory")
        self.action_type = 'shallow' if str(action_type).lower() == "shallow" else "deep"
        
        if type(self.main) == Exception or type(self.copy) == Exception:
            log_message('compare.py', f'{os.path.abspath(main)} ({ "file" if os.path.isfile(main) else "folder"}) and {os.path.abspath(copy)} ({ "file" if os.path.isfile(copy) else "folder"})', 'ERROR', datetime.now())
            sys.exit()
    
    def run(self):
        log_message('compare.py', f'Started comparing: {self.main} and {self.copy}', 'START', datetime.now())

        main_tree = get_files(self.main)
        copy_tree = get_files(self.copy)

        if len(main_tree) != len(copy_tree):
            log_message('compare.py', f'Main ({len(main_tree)}) is not equal Copy ({len(copy_tree)})', 'ERROR')
            sys.exit()

        log_message('compare.py', f'Folders are the same ({self.main}) and ({self.copy})', 'FINISH')
        

if __name__ == "__main__":
    start_time = datetime.now()
    parser = argparse.ArgumentParser(description="Compare if two folders are different")
    parser.add_argument('folder1', help='first folder')
    parser.add_argument('folder2', help='Second folder')
    parser.add_argument('-t', '--type', default='shallow', help="Shallow or Deep")
    args = parser.parse_args()

    app = CompareFolders(args.folder1, args.folder2, args.type)
    app.run()
