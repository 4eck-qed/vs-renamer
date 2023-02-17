import os
import re
from modules.FileHelper import FileHelper

from modules.Language import Language
from modules.Localizer import Localizer

class Renamer():
    def __init__(self, lang: Language):
        self.localizer = Localizer(lang)
        self.file_helper = FileHelper()

    def _get_proj_file(self, search_path: str, name: str = "") -> str:
        for entry in search_path:
            if os.path.isdir(entry):
                return self._get_proj_file(entry)
            if self.localizer.is_valid_proj_file(entry):
                return entry
        return None
    
    def rename_all_uniform(in_dir: str, new_name: str):
        """
        Uniform rename operation.
        Every prefix is expected to be the same as such:
        MyProj.A
        MyProj.B
        MyProj.C
        
        Args:
            in_dir (str): directory of the solution
        """
        # get solution name
        # get 

    def rename_project(self, in_dir: str, proj_name: str, new_name: str):
        """
        Renames given project.
        
        Args:
            in_dir (str): directory of the solution
        """
        # Rename folder
        os.rename(f"{in_dir}/{proj_name}", f"{in_dir}/{new_name}")
        
        # Rename proj file (e.g .vcxproj)
        proj_file = self._get_proj_file(in_dir, proj_name)
        proj_dir = os.path.dirname(proj_file)
        
        new_file = f"{proj_dir}/{new_name}"
        os.rename(proj_file, new_file)
        
        # Rename references
        refs = self.file_helper.find_references(in_dir, proj_name)
        for ref in refs:
            with open(ref) as f:
                content = f.read()
                # replace old name with new name
                f.write(content.replace(proj_name, new_name))
        
