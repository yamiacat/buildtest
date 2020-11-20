# Untitled object in buildtest configuration schema Schema

```txt
https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section
```

A compiler section is composed of `cc`, `cxx` and `fc` wrapper these are required when you need to specify compiler wrapper.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## compiler_section Type

`object` ([Details](settings-definitions-compiler_section.md))

# undefined Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------ | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cc](#cc)           | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-cc.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/cc")                       |
| [cxx](#cxx)         | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-cxx.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/cxx")                     |
| [fc](#fc)           | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-fc.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/fc")                       |
| [modules](#modules) | `array`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-unique_string_array.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules") |

## cc

Specify path to C compiler wrapper. You may specify a compiler wrapper such as `gcc` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.


`cc`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-cc.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/cc")

### cc Type

`string`

## cxx

Specify path to C++ compiler wrapper. You may specify a compiler wrapper such as `g++` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.


`cxx`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-cxx.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/cxx")

### cxx Type

`string`

## fc

Specify path to Fortran compiler wrapper. You may specify a compiler wrapper such as `gfortran` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.


`fc`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-fc.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/fc")

### fc Type

`string`

## modules

Specify list of modules to load when resolving compiler. The modules will be inserted into test script when using the compiler


`modules`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-unique_string_array.md "https&#x3A;//buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules")

### modules Type

`string[]`

### modules Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.