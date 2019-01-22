## The Data class

### Introduction

Representation of the binary data separated into segments.

Currently the data list is the result of a BinaryIO.read(), so the data is not yet interprated.

### Class synopsis

```python
class Data:
    # Properties
    data: List[bytes]
    data_section_offset_table: DataSectionOffsetTable
    
    # Methods
    def __init__(
        infile: BinaryIO,
        data_section_header: SectionHeader,
        data_section_offset_table: DataSectionOffsetTable,
        classnames
    ) -> None: pass
```

#### Properties

##### `data`

A list of data segments.

##### `data_section_offset_table`

A table of offsets for the data section.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### Data.\_\_init\_\_

#### Description

```
Data(infile: BinaryIO, data_section_header: SectionHeader, data_section_offset_table: DataSectionOffsetTable, classnames) -> None: pass
```

Creates a new Havok object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

##### `data_section_header`

The section header decompiled from the file header.

##### `data_section_offset_table`

The offset table decompiled from the end of the data section.

##### `classnames`

The class name data decompiled from the class name section.

#### Return Value

Creates a new `Data` object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Decompiling the data section

```python
import havok
with open('/assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
    infile.seek(0x40)
    classnames_header = havok.SectionHeader(infile)
    class_names = havok.ClassNames(infile, classnames_header)
    infile.seek(0xc0)
    data_header = havok.SectionHeader(infile)
    data_section_offset_table = havok.DataSectionOffsetTable(infile, 0x9d0, 80)
    data_section = havok.Data(infile, data_header, data_section_offset_table, class_names)

    print(data_section[0])  # 0x00000000
    print(data_section[1])  # 0x50687973
```