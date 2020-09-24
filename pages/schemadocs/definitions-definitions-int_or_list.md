# Untitled undefined type in JSON Schema Definitions File. This file is used for declaring definitions that are referenced from other schemas Schema

```txt
definitions.schema.json#/definitions/status/properties/returncode
```

Specify a list of returncodes to match with script's exit code. buildtest will PASS test if script's exit code is found in list of returncodes. You must specify unique numbers as list and a minimum of 1 item in array


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## returncode Type

merged type ([Details](definitions-definitions-int_or_list.md))

one (and only one) of

-   [Untitled integer in JSON Schema Definitions File. This file is used for declaring definitions that are referenced from other schemas](definitions-definitions-int_or_list-oneof-0.md "check type definition")
-   [Untitled array in JSON Schema Definitions File. This file is used for declaring definitions that are referenced from other schemas](definitions-definitions-list_of_ints.md "check type definition")