## The ClassName class

### Introduction

A container for a single class name and its id.

### Class synopsis

```python
class ClassName:
    # Properties
    id: int
    name: str
    
    # Methods
    def __init__(id: int, name: str) -> None: pass
```

#### Properties

##### `id`

The class name id.

##### `name`

The name of the class.

### ClassName.\_\_init\_\_

Creates a new ClassName object

#### Description

```
ClassName(id: int, name: str) -> None
```

Creates a new ClassName object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new ClassName object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |