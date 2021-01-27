from utils import cls_repr


class _Group:
    def __init__(self, obj):
        self.obj = obj
        self.set = {self}

    def merge(self, rhs):
        self.set.update(rhs.set)
        for item in rhs.set:
            item.obj = self.obj
            item.set = self.set


class Group:
    def __init__(self, **kwargs):
        self._group = _Group(kwargs)

    @property
    def kwargs(self):
        return self._group.obj

    def merge(self, rhs):
        self._group.merge(rhs._group)

    def __eq__(self, rhs):
        return self._group.set is rhs._group.set

    def __getattr__(self, key):
        return self.kwargs[key]

    def __repr__(self):
        return cls_repr(type(self), **self.kwargs)


if __name__ == '__main__':
    a = Group(color=0)
    b = Group(color=1)
    c = Group(color=2)
    d = Group(color=3)
    e = Group(color=4)

    a.merge(b)
    d.merge(e)
    print(a, b, c, d, e)
    print(a == e)
    c.merge(a)
    c.merge(e)
    print(a, b, c, d, e)
    print(a == e)
