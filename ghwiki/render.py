# Contains environment and renders from environment
from jinja2 import Environment, FileSystemLoader, select_autoescape
import ghwiki.environment as ghwiki_env
from ghwiki.utils import get_default_template

ENV = None

# Default environment arguments
env_arg_defaults = dict(
    # autoescape=select_autoescape(['html','md']),
    line_statement_prefix='#py ',
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(ghwiki_env.default_search_paths)
    )

# Set the environment
def set_env(env):
    global ENV
    ENV = env

# Initialize the environment
def init(**kwargs):
    ENV = Environment( **{ **env_arg_defaults, **kwargs } )
    ENV.globals= ghwiki_env.get_env()
    set_env( ENV )

# Render a file, and initialize the environment if necessary
def render(file_path, **kwargs):
    if ENV is None: init()

    # Check to see if the path is the name of a default file
    template_processor, default_template_path = get_default_template(file_path)
    if default_template_path is not None:
        file_path = default_template_path
        kwargs = template_processor(kwargs)
    try:
        template = ENV.get_template(file_path)
    except FileNotFoundError:
        template = ENV.get_template( os.path.abspath(file_path) )
    return template.render(**kwargs).strip()

# Example usage
# from ghwiki import render
#
# txt = render('branch',name='my_branch',tags={'status':'wip'})
# with open('output_file.md','w') as file:
#     file.write(txt)
