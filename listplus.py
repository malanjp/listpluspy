#!/usr/bin/env python
class List(list):

    def head(self):
        """
        >>> l = List(range(1, 5))
        >>> l.head()
        1
        """
        return self[0]

    def tail(self):
        """
        >>> l = List(range(1, 5))
        >>> l.tail()
        [2, 3, 4]
        >>> l.tail().tail().tail()
        [4]
        >>> l.tail().tail().tail().tail()
        []
        """
        return List(self[1:])

    def init(self):
        """
        >>> l = List(range(1, 5))
        >>> l.init()
        [1, 2, 3]
        """
        return List(self[0:-1])

    def last(self):
        """
        >>> l = List(range(1, 5))
        >>> l.last()
        4
        """
        return self[-1]

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
        >>> print l
        ['c', 'b', 'a']
        """
        tmp = self.__getitem__(idx1)
        self.__setitem__(idx1, self.__getitem__(idx2))
        self.__setitem__(idx2, tmp)

    def length(self):
        """
        >>> l = List([1, 2, 3, 4, 5])
        >>> print l.length()
        5
        >>> from random import randint
        >>> generate_count = randint(0, 1000)
        >>> l = List([x for x in range(0, generate_count)])
        >>> l.length() == generate_count
        True
        """
        return len(self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

