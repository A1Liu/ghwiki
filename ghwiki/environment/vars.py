__env_vars__ = {}

def __env_set__(obj, name, env):
    env[name] = obj
    return obj

# Sets a variable namespace in the environment
def env_set(obj, name):
    global __env_vars__
    return __env_set__(obj, name, __env_vars__)

# Usage:
# @env_add
# def my_func():
#     return "my_info"
# @env_add(name = "my_func_name")
# def my_func():
#     return "my_info"
def env_add(func = None, name = None):
    if name is not None:# If we use it as @env_add(as="name") then the function should be added as "name"
        return lambda x: env_set(x, name)
    if func is None and name is None: # For those that try to use @env_add()
        return lambda _func: env_set(_func, _func.__name__)
    return env_set(func,func.__name__)

def env_remove(name):
    global __env_vars__
    __env_vars__.pop(name)

def env_remove_all():
    global __env_vars__
    __env_vars__.clear()

def env_get(key):
    global __env_vars__
    return __env_vars__[key]

def get_env():
    global __env_vars__
    return __env_vars__

# Secret evnironment for secret sauce package functions 

__secret_env__ = {}
@env_add
def __env_get__(key):
    global __secret_env__
    return __secret_env__[key]

def __env_add__(func):
    global __secret_env__
    return __env_set__(func, func.__name__, __secret_env__)
