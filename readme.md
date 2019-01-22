# Breath of the Wild Havok Decompiler

This Python package aims to decompile (and eventually recompile) *Havok* binary files for *the Legend of Zelda: Breath of the Wild*.

The pre-release of this package does not fully decompile the binary data, but organizes the file into a `Havok` object.

# Table of Contents

* Classes
    * The Havok class
        * Havok.\_\_init\_\_
    * The Header class
        * Header.\_\_init\_\_
        * Header.is_long
    * The SectionHeader class
        * SectionHeader.\_\_init\_\_
    * The SectionHeaderTables class
        * SectionHeaderTables.\_\_init\_\_
    * The SectionHeaderItem class
        * SectionHeaderItem.\_\_init\_\_
    * The ClassNames class
        * ClassNames.\_\_init\_\_
    * The DataSectionOffsetTable class
        * DataSectionOffsetTable.\_\_init\_\_
        * DataSectionOffsetTable.append
    * The DataSectionOffsetTableItem class
        * DataSectionOffsetTableItem.\_\_init\_\_
    * The Data class
        * Data.\_\_init\_\_
        

# Classes

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

## The ClassNames class

### Introduction

A list of class names used by the file.

### Class synopsis

```python
class ClassNames:
    # Properties
    class_names: List[ClassName]
    
    # Methods
    def __init__(infile: BinaryIO, section_header: SectionHeader) -> None: pass
```

#### Properties

##### `class_names`

List of `ClassName` objects

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### ClassNames.\_\_init\_\_

Creates a new ClassNames object

#### Description

```
ClassNames(infile: BinaryIO, section_header: SectionHeader) -> None
```

Creates a new ClassNames object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

#### Return Values

Creates a new ClassNames object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Read list of class names

```python
import havok
with open('/assets/Npc_King_Vagrant.hkcl', 'rb') as infile:
    infile.seek(64)
    section_header_tables = havok.SectionHeaderTables(infile)
    classnames = havok.ClassNames(infile, section_header_tables.classnames)
    print(classnames[0].name)  # hkClass
    print(classnames[5].name)  # hclClothContainer
```

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

## The DataSectionOffsetTable class

### Introduction

A container for the data section offset table.

### Class synopsis

```python
class DataSectionOffsetTable:
    # Properties
    items: List[DataSectionOffsetTableItem]
    
    # Methods
    def __init__(infile: BinaryIO, table_start: int, table_size: int) -> None: pass
    def append(data: DataSectionOffsetTableItem) -> int: pass
```

#### Properties

##### `items`

Items in the offset table.

### DataSectionOffsetTable.\_\_init\_\_

#### Description

```
DataSectionOffsetTable(infile: BinaryIO, table_start: int, table_size: int) -> None
```

Creates a new DataSectionOffsetTable object

#### Parameters

##### `infile`

A [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode.

##### `table_start`

Absolute offset to the beginning of the data section offset table (located after the raw data segment).

##### `table_size`

Size of the data section offset table in bytes

#### Return Values

Creates a new DataSectionOffsetTable object

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Read data section offset table

```python
import havok
havok_file = havok.Havok('/assets/FldObj_FallingRock_A_01.hkrb')  # grab section header tables

with open('/assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
    data_section_offset_table = havok.DataSectionOffsetTable(
        infile,
        havok_file.section_header_tables.data.offsets[0].abs_offset,
        havok_file.section_header_tables.data.offsets[0].size
    )
    print(data_section_offset_table[0].meta)  # 0
    print(data_section_offset_table[0].data)  # 16
    print(data_section_offset_table[4].meta)  # 120
    print(data_section_offset_table[4].data)  # 192
```

### DataSectionOffsetTable.append

Appends a DataSectionOffsetTableItem object to the end of the offset list.

#### Description

```
DataSectionOffsetTable.append(data: DataSectionOffsetTableItem) -> int
```

#### Parameters

##### `data`

An instance of a DataSectionOffsetTableItem object

#### Return Values

The index of the appended DataSectionOffsetTableItem.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Append a DataSectionOffsetTableItem to list

```python
import havok
havok = havok.Havok('../assets/FldObj_FallingRock_A_01.hkrb')  # get section header tables

with open('../assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
    data_section_offset_table = havok.DataSectionOffsetTable(
        infile,
        havok.section_header_tables.data.offsets[0].abs_offset,
        havok.section_header_tables.data.offsets[0].size
    )
    new_offset_index = data_section_offset_table.append(
        DataSectionOffsetTableItem(
            0x1c0,
            0x9d0
        )
    )
    print(data_section_offset_table[new_offset_index].meta)  # 448
    print(data_section_offset_table[new_offset_index].data)  # 2512
```

## The DataSectionOffsetTableItem class

### Introduction

A single offset table item.

### Class synopsis

```python
class DataSectionOffsetTableItem:
    # Properties
    meta: int
    data: int
    size: int
    array_length: int
    
    # Methods
    def __init__(meta_offset: int, data_offset: int, length=0, array_length=0) -> None: pass
```

#### Properties

##### `meta`

Relative offset to the entry meta data (usually the array length).

##### `data`

Relative offset to the entry data.

##### `size`

Size of the data segment in bytes.

##### `array_length`

Length of the data segment array. `0` if the segment is not an array or a string.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

### DataSectionOffsetTableItem.\_\_init\_\_

#### Description

```
DataSectionOffsetTableItem(meta_offset: int, data_offset: int, size=0, array_length=0) -> None: pass
```

Creates a new `DataSectionOffsetTableItem` object

#### Parameters

##### `meta_offset`

Relative offset to the data segment metadata. The metadata typically contains array length.

##### `data_offset`

Relative offset to the data segment raw data.

##### `size`

Size in bytes of the raw data entry.

##### `array_length`

The number of elements in the raw data array.

#### Return Value

Creates a new `DataSectionOffsetTableItem` object.

By default size and array_length are `0` because the values for these parameters are not located in the data section offset table.

#### Changelog

| Version | Description |
|:--|:--|
| 0.9 | Initially added. |

#### Examples

##### Example #1 Passing offsets to DataSectionOffsetTableItem

```python
import havok
data_offsets = havok.DataSectionOffsetTableItem(0x00, 0x10)
print(data_offsets.meta_offset)  # 0
print(data_offsets.data_offset)  # 16
```

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