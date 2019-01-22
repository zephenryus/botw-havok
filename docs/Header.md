## The Header class

### Introduction

Represents the file header.

### Class synopsis

```python
class Header:
    # Properties
    signature: bytes
    version: str
    size: int
    
    # Methods
    def __init__(infile: BinaryIO) -> None: pass
    def is_long() -> bool: pass
```

#### Properties

##### `signature`

Binary file signature. *Havok* files always have signature bytes `57 E0 E0 57 10 C0 C0 10`

##### `version`

Indicates the target version of the *Havok* Engine. *Breath of the Wild* targets hk_2014.2.0-r1.

##### `size`

The size of the header in bytes. There are two known header sizes: 64 bytes (short header) and 80 bytes (long header).

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### Header.\_\_init\_\_

Creates a new *Havok* Header object

#### Description

```
Header(infile: BinaryIO) -> None
```

Creates a new *Havok* Header object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new *Havok* Header object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Decompiling a Havok Binary Header

```python
import havok
with open('../assets/G-6-2.hksc', 'rb') as infile:
    header = havok.Header(infile)
    print(header.version)  # hk_2014.2.0-r1
```

### Header.is_long

Checks if the header for the file is 80 bytes (True) or 64 bytes (False).

#### Description

```
Header.is_long() -> bool
```

#### Return Values

Returns `True` if the header is 80 bytes and `False` if it is 64 bytes.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 File with long header

```python
import havok
with open('/assets/19-13.hknm2', 'rb') as infile:
    header = havok.Header(infile)
    print(header.is_long())  # True
```

##### Example #2 File with short header

```python
import havok
with open('/assets/G-6-2.hksc', 'rb') as infile:
    header = havok.Header(infile)
    print(header.is_long())  # False
```