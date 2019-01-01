from ghwiki.environment.vars import __env_add__, env_add
from jinja2.exceptions import UndefinedError

# Default functions
@env_add
def debug(*args,**kwargs):
    print(args,kwargs)

@env_add
def md_link(text,link):
    return '[%s](%s)' % (text, link)

@env_add
def md_file_link(path,base):
    return md_link(path,base+'/'+path)

@env_add
def md_issue_link(ref,repo_link):
    ref = str(ref)
    return md_link('#'+ref,repo_link+'/issues/'+ref)

@env_add
def md_pr_link(ref,repo_link):
    ref = str(ref)
    return md_link('#'+ref,repo_link+'/pull/'+ref)

order = {'issue':1,'pull_request':2, 'status':3 }
translate = {'issue':'Addresses Issue','pull_request':'Pull Request'}
@__env_add__
def process_tags(tags):
    lines = []
    try:
        items = tags.items()
    except UndefinedError:
        return

    for key, value in sorted( items, key=lambda pair: order.get(pair[0],0), reverse=True ):
        lines.append("**%s:** %s" % ( translate.get(key, key.capitalize() ) , value) )
    return '\n'.join(lines)
