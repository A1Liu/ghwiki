import os, re
import importlib
from ghwiki.environment import DEFAULT_TEMPLATE_PATH

# Generator to return file names from a directory that end in .yml
def get_ext(base, ext=None, ignore = None):
    base = os.path.abspath(base)
    for root, dirs, files in os.walk(base):
        yield from (os.path.join(root,file) for file in files if file.endswith(ext))
        if callable(ignore):
            dirs[:] = ignore(dirs)
        elif isinstance(ignore, list):
            dirs[:] = [dir for dir in dirs if dir not in ignore]

def get_default_template(name):
    file_name = name+'.md'
    path = os.path.join(DEFAULT_TEMPLATE_PATH,file_name)
    if os.path.exists(path):
        # Use importlib here to import and return the template processor
        module = importlib.__import__( 'ghwiki.templates.'+name, fromlist=('',) )
        processor = module.__getattribute__(name)
        return processor, file_name
    return None, None
