ListPlus.py
========

## Overview

ListPlus.py is Scala like list class library for Python.

### Requirements
Python >= 3.3.2

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
2
```

#### swap

```python
>>> l = List(['a', 'b', 'c'])
>>> l.swap(0, 2)
>>> print(l)
['c', 'b', 'a']
 ```

#### forall

```python
>>> l = List(range(1, 5))
>>> l.forall('_ > 0')
True
>>> l.forall('_ > 3')
False
```

### Properties

#### length

```python
>>> l = List([1, 2, 3, 4, 5])
>>> print(l.length)
5
```


