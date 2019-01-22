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