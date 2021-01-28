from contextlib import contextmanager

from utils import cls_repr


class _Group:
    def __init__(self, key):
        self.key = key
        self.set = {self}

    def merge(self, rhs):
        self.set.update(rhs.set)
        for item in rhs.set:
            item.key = self.key
            item.set = self.set

    def clear(self):
        self.set.clear()


class Group:
    def __init__(self, **kwargs):
        self._group = _Group(kwargs)

    @property
    def kwargs(self):
        return self._group.key

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
    #print(a, b, c, d, e)
    assert a != e
    c.merge(a)
    c.merge(e)
    #print(a, b, c, d, e)
    assert a == e


class HashInstance:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, rhs):
        if not isinstance(rhs, __class__):
            return NotImplemented
        return self.obj is rhs.obj

    def __hash__(self):
        return object.__hash__(self.obj)

    def __repr__(self):
        return cls_repr(type(self), self.obj)


class Grouper:
    def __init__(self):
        self._groups = set()
        self._groups_by_object = {}

    def add(self, obj, key=None):
        group = _Group(key)
        group.obj = obj
        self._groups.add(group)
        obj = HashInstance(obj)
        self._groups_by_object[obj] = group

    def _obj_group(self, obj):
        objh = HashInstance(obj)
        return self._groups_by_object[objh]

    def equal(self, lhs, rhs):
        lgroup = self._obj_group(lhs)
        rgroup = self._obj_group(rhs)
        return lgroup.set is rgroup.set

    def merge(self, lhs, rhs):
        lgroup = self._obj_group(lhs)
        rgroup = self._obj_group(rhs)
        lgroup.merge(rgroup)

    def groups(self):
        for group in self._groups:
            yield group.key, [g.obj for g in group.set]

    def clear(self):
        for group in self._groups:
            del group.obj
            group.clear()
        self._groups.clear()
        self._groups_by_object.clear()


@contextmanager
def grouper():
    g = Grouper()
    try:
        yield g
    finally:
        g.clear()


if __name__ == '__main__':
    l = [1]
    l2 = [1]
    assert len({HashInstance(l), HashInstance(l2), HashInstance(l)}) == 2

    objects = [{f'obj-{i}'} for i in range(10)]

    with grouper() as g:
        for i, obj in enumerate(objects):
            g.add(obj, i)

        for left, right in zip(objects[::2], objects[1::2]):
            g.merge(left, right)

        groups = {k: sorted(v, key=tuple) for k, v in g.groups()}

    assert groups == {
        i: [{f'obj-{i}'}, {f'obj-{i+1}'}]
        for i in range(0, 10, 2)
    }
