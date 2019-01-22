## The SectionHeaderItem class

### Introduction

Container for a single entry in a section header offset table.

### Class synopsis

```python
class SectionHeaderItem:
    # Properties
    rel_offset: int
    abs_offset: int
    size: int
    
    # Methods
    def __init__(rel_offset: int, abs_offset: int, length: int) -> None: pass
```

#### Properties

##### `rel_offset`

The relative offset to a section segment.

##### `abs_offset`

The absolute offset (relative offset + section offset) to a section segment.

##### `size`

The section segment's size in bytes.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### SectionHeaderItem.\_\_init\_\_

Creates a new SectionHeaderItem object

#### Description

```
SectionHeaderItem(infile: BinaryIO) -> None
```

Creates a new SectionHeaderItem object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new SectionHeaderItem object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |