import os
import re
from typing import List

class FileHelper():
    def __init__(self):
        pass
    
    def get_file_by_match(self, search_path: str, pattern: str = "", excludes: List[str] = list()) -> str:
        for entry in search_path:
            if os.path.isdir(entry):
                return self.get_file_by_match(entry, pattern)
            is_excluded = False
            for exclude in excludes:
                if re.match(exclude, entry):
                    is_excluded = True
            if re.match(pattern, entry) and not is_excluded:
                return entry
        return None
    
    def get_file_by_name(self, search_path: str, name: str = "") -> str:
        return self.get_file_by_match(search_path, rf"\w+{name}.?\w*")
    
    def get_files_by_type(self, search_path: str, type: str = "") -> List[str]:
        files = list()
        excludes = list()
        for file in self.get_file_by_match(search_path, rf"\w+.{type}", excludes):
            files.append(file)
            tokens = file.split("\\")
            if len(tokens) <= 1:
                file_name = file.split("/").pop()
            else:
                file_name = tokens.pop()
                
            excludes.append(rf"\w+{file_name}.{type}")
            
    def contains_keyword(self, file: str, keyword: str):
        with open(file) as f:
            lines = f.readlines()
        for line in lines:
            if keyword in line: # TODO change for proper pattern that definitely is a reference to that keyword
                return True
            
        
    
    def find_references(self, search_path: str, keyword: str) -> List[str]:
        """
        Finds all references of given keyword.
        
        Returns:
            List of files where the keyword was referenced

        Args:
            search_path (str): path to search in
            keyword (str): keyword to find references for
        """
        srcs = self.get_files_by_type(search_path, "cs")
        refs = list()
        for src in srcs:
            if self.contains_keyword(src, keyword):
                refs.append(src)
                
        return refs
        