#!/usr/bin/env python
from functools import reduce

class List(list):

    """
    Methods
    """
    def get(self, index, default=None):
        """
        >>> l = List(range(1, 5))
        >>> l.get(1)
        2
        >>> l.get(9, 0)
        0
        >>> l.get(9, 'fail')
        'fail'
        >>> l.get(9)
        """
        try:
            return self.__getitem__(index)
        except IndexError:
            return default

    def swap(self, idx1, idx2):
        """
        >>> l = List(['a', 'b', 'c'])
        >>> l.swap(0, 2)
        >>> print(l)
        ['c', 'b', 'a']
        """
        tmp = self.__getitem__(idx1)
        self.__setitem__(idx1, self.__getitem__(idx2))
        self.__setitem__(idx2, tmp)

    def forall(self, expr):
        """
        >>> l = List([1, 2, 3])
        >>> l.forall('_ > 2')
        False
        >>> l.forall('_ > 0')
        True
        """
        ifstr = '[_ for _ in {0} if {1}]'.format(self, expr)
        result = eval(ifstr)
        if len(result) == len(self):
            return True
        return False

    def contains(self, value):
        """
        >>> l = List([1, 2, 3])
        >>> l.contains(2)
        True
        >>> l.contains(5)
        False
        >>> l = List(['a', 'b', 'c'])
        >>> l.contains('b')
        True
        >>> l.contains('f')
        False
        """
        return value in self

    def apply(self, index):
        """
        >>> l = List([1, 2, 3])
        >>> l.apply(2)
        3
        >>> l.apply(3) is None
        True
        """
        return self.get(index, None)


    def take(self, count):
        """
        >>> l = List([1, 2, 3])
        >>> l.take(2)
        [1, 2]
        >>> l.take(3)
        [1, 2, 3]
        >>> l.take(4)
        [1, 2, 3]
        """
        return List(self[:count])

    def drop(self, count):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> l.drop(2)
        [3, 4, 5]
        >>> l = List(['a', 'b', 'c', 'd', 'e'])
        >>> l.drop(3)
        ['d', 'e']
        """
        return List(self[count:])

    def dropRight(self, count):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> l.dropRight(2)
        [1, 2, 3]
        >>> l = List(['a', 'b', 'c', 'd', 'e'])
        >>> l.dropRight(3)
        ['a', 'b']
        """
        return List(self[:-count])


    """
    Properties
    """
    @property
    def head(self):
        """
        >>> l = List(range(1, 5))
        >>> l.head
        1
        """
        return self[0]

    @property
    def tail(self):
        """
        >>> l = List(range(1, 5))
        >>> l.tail
        [2, 3, 4]
        >>> l.tail.tail.tail
        [4]
        >>> l.tail.tail.tail.tail
        []
        """
        return List(self[1:])

    @property
    def init(self):
        """
        >>> l = List(range(1, 5))
        >>> l.init
        [1, 2, 3]
        """
        return List(self[0:-1])

    @property
    def last(self):
        """
        >>> l = List(range(1, 5))
        >>> l.last
        4
        """
        return self[-1]

    @property
    def length(self):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> print(l.length)
        5
        >>> from random import randint
        >>> generate_count = randint(0, 1000)
        >>> l = List([x for x in range(0, generate_count)])
        >>> l.length == generate_count
        True
        >>> l.length == -1
        False
        """
        return len(self)

    @property
    def min(self):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> print(l.min)
        1
        """
        return min(self)

    @property
    def max(self):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> print(l.max)
        5
        """
        return max(self)

    @property
    def size(self):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> print(l.size)
        5
        """
        return self.length

    @property
    def isEmpty(self):
        """
        >>> l = List([])
        >>> print(l.isEmpty)
        True
        >>> l = List([1])
        >>> print(l.isEmpty)
        False
        """
        return True if len(self) == 0 else False

    @property
    def sorted(self):
        """
        >>> l = List([5, 4, 3, 2, 1])
        >>> print(l.sorted)
        [1, 2, 3, 4, 5]
        """
        self.sort()
        return self

    @property
    def reverse(self):
        """
        >>> l = List([5, 4, 3, 2, 1])
        >>> print(l.sorted)
        [1, 2, 3, 4, 5]
        """
        self.reverse()
        return self

    @property
    def sum(self):
        """
        >>> l = List([1,2,3])
        >>> l.sum
        6
        >>> l = List([])
        >>> l.sum
        0
        """
        return sum(self)

    @property
    def product(self):
        """
        >>> l = List([1,2,3])
        >>> l.product
        6
        >>> l = List([])
        >>> l.product
        0
        """
        if len(self) < 1:
            return 0
        return reduce(lambda a, b: a * b, self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


