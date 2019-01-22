## The Havok class

### Introduction

A container class for all headers and data contained within a *Havok* binary file.

### Class synopsis

```python
class Havok:
    # Properties
    header: Header
    section_header_tables: SectionHeaderTables
    classnames: List[ClassName]
    data_section_offset_table: DataSectionOffsetTable
    data: Data

    # Methods
    def __init__(path: str) -> None: pass
```

#### Properties

##### `header`

Contains header information for the entire file

##### `section_header_tables`

Contains header information the three sections of the file: classnames, types and data.

##### `classnames`

A list of class names to be parsed from the file.

##### `data_section_offset_table`

A table of offsets of data segments contained in the data section of the file.

##### `data`

The parsed binary data.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### Havok.\_\_init\_\_

#### Description

```
Havok(path: str) -> None
```

Creates a new Havok object

#### Parameters

##### `path`

Path to the *Havok* binary to decompile.

**Note:** On the Windows platform, be careful to escape any backslashes used in the path to the file, or use forward slashes.

```python
from havok import Havok
havok = Havok('c:\\folder\\file.hkcl')
```

```python
from havok import Havok
havok = Havok('c:/folder/file.hkcl')
```

#### Return Value

Creates a new `Havok` object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Decompiling a Havok Binary

```python
import havok
havok_file = havok.Havok('/assets/12-16.hktmrb')
print(havok_file.classnames[0])  # ClassName <id: 869540739, name: 'hkClass'>
```