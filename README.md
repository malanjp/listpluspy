ListPlus.py
========

## Overview

ListPlusPy is Scala like list class library for Python.

### Usage

```python
>>> from listplus import List
>>> l = List(range(1, 5))
>>> l.head()
1
```

### Methods

#### head

```python
>>> l = List(range(1, 5))
>>> l.head()
1
```

#### tail

```python
>>> l = List(range(1, 5))
>>> l.tail()
[2, 3, 4]
```

#### init

```python
>>> l = List(range(1, 5))
>>> l.init()
[1, 2, 3]
```

#### last

```python
>>> l = List(range(1, 5))
>>> l.last()
4
```

#### get

```python
>>> l = List(range(1, 5))
>>> l.get(1)
```

#### swap

```python
>>> l = List(['a', 'b', 'c'])
>>> l.swap(0, 2)
>>> print(l)
['c', 'b', 'a']
 ```

### Properties

#### length

```python
>>> l = List([1, 2, 3, 4, 5])
>>> print(l.length)
5
```


