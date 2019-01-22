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