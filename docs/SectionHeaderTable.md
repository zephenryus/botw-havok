## The SectionHeaderTables class

### Introduction

A container for the three section headers, classnames, types and data.

### Class synopsis

```python
class SectionHeaderTables:
    # Properties
    classnames: SectionHeader
    types: SectionHeader
    data: SectionHeader
    
    # Methods
    def __init__(infile: BinaryIO) -> None: pass
```

#### Properties

##### `classnames`

Represents the classnames section header.

##### `types`

Represents the types section header.

##### `data`

Represents the data section header.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### SectionHeaderTables.\_\_init\_\_

Creates a new SectionHeaderTables object

#### Description

```
SectionHeaderTables(infile: BinaryIO) -> None
```

Creates a new SectionHeaderTables object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new SectionHeaderTables object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Reading all section header tables

```python
import havok
with open('/assets/19-13.hknm2', 'rb') as infile:
    infile.seek(80)
    section_header_tables = havok.SectionHeaderTables(infile)
    print(section_header_tables.classnames.name)  # '__classnames__'
```