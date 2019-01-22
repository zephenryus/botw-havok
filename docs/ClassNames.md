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