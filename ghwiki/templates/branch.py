from ghwiki.environment.vars import __env_add__, env_get
from ghwiki.environment.functions import md_file_link
import json # json.__name__ ='json'

def branch(kwargs):
    __env_add__(json)
    file_edits = None
    prepend='This PR can be verified by viewing %s'
    if 'files' in kwargs:
        files = kwargs['files']
        if not isinstance(files, list): raise TypeError("'files' is not of type list!")
        repo_url = '%s/tree/%s' % ( env_get('repo_url'),kwargs['name'] )
        if len(files) > 1:
            file_edits = prepend % 'the following files:\n'
            file_edits+= '\n'.join( [ md_file_link( file,repo_url ) for file in files] )+'\n'
        else:
            file_edits = prepend % md_file_link( files[0],repo_url )+'.\n'

    if 'testing_instructions' in kwargs:
        testing_instructions = kwargs['testing_instructions']
        file_edits = '' if file_edits is None else file_edits
        if testing_instructions is None:
            testing_instructions = file_edits+'\n'+env_get('testing_instructions_default')
        else:
            testing_instructions = testing_instructions+'\n'+file_edits
    else:
        testing_instructions = file_edits
    kwargs['testing_instructions'] = testing_instructions
    return kwargs
