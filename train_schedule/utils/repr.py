import itertools


def cls_repr(cls, /, *args, **kwargs):
    """
    Get representation of a class instance

    cls_repr(Object, 1, 'a', foo='bar')
    => "Object(1, 'a', foo='bar')"
    """
    args = (repr(arg) for arg in args)
    kwargs = (f'{key}={arg!r}' for key, arg in kwargs.items())
    args_txt = ', '.join(itertools.chain(args, kwargs))
    return f'{cls.__qualname__}({args_txt})'
