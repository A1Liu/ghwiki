# Global variables for module, also functions for getting variables
from ghwiki.environment.vars import *
import ghwiki.environment.vars as vars
import ghwiki.environment.functions as functions
import os

DEFAULT_TEMPLATE_PATH = os.path.join( os.path.dirname( os.path.dirname(__file__) ),'templates' )

# Default search paths to look for templates in
default_search_paths = [
    DEFAULT_TEMPLATE_PATH, # Template folder
    os.path.join( os.getcwd() ), # Current working directory
    os.path.abspath(os.sep) # Root directory
     ]

env_set('- item1\n- item2\n- ...', name = 'ul_template')
env_set("",name="testing_instructions_default")
env_set('octocat', name="username")
