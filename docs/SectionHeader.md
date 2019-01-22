## The SectionHeader class

### Introduction

Contains header information for a single section.

### Class synopsis

```python
class SectionHeader:
    # Properties
    name: str
    start: int
    offsets: List[SectionHeaderItem]
    
    # Methods
    def __init__(infile: BinaryIO) -> None: pass
```

#### Properties

##### `name`

The name of the section. Can be `__classnames__`, `__types__` or `__data__`.

##### `start`

The absolute offset to the beginning of the section.

##### `offsets`

A list of `SectionHeaderItem` (which are a list of relative and absolute offsets to different segments in the section).

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### SectionHeader.\_\_init\_\_

Creates a new SectionHeader object

#### Description

```
SectionHeader(infile: BinaryIO) -> None
```

Creates a new SectionHeader object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new SectionHeader object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Reading the classnames section header

```python
import havok
with open('/assets/G-6-2.hksc', 'rb') as infile:
    infile.seek(64)
    section_header = havok.SectionHeader(infile)
    print(section_header.name)  # __classnames__
```