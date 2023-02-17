import re

from modules.Language import Language

class Localizer():
    def __init__(self, lang: Language):
        self.lang = lang
    
    def is_valid_proj_file(self, path_to_proj_file, name=""):
        prefix = f"\w+{name}.vcxproj"
        if self.lang == Language.CPP:
            return re.match(f"{prefix}.vcxproj", path_to_proj_file)
        if self.lang == Language.CS:
            return re.match(f"{prefix}.csproj", path_to_proj_file)
        if self.lang == Language.VB:
            return re.match(f"{prefix}.vbproj", path_to_proj_file)