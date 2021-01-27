import itertools


def cls_repr(cls, /, *args, **kwargs):
    args = (repr(arg) for arg in args)
    kwargs = (f'{key}={arg!r}' for key, arg in kwargs.items())
    args_txt = ', '.join(itertools.chain(args, kwargs))
    return f'{cls.__qualname__}({args_txt})'
