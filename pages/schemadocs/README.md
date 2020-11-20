# README

## Top-level Schemas

-   [JSON Schema Definitions File. ](./definitions.md "This file is used for declaring definitions that are referenced from other schemas") – `definitions.schema.json`
-   [buildtest configuration schema](./settings.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json`
-   [compiler schema version 1.0](./compiler-v1.md "The compiler schema is of type: compiler in sub-schema which is used for compiling and running programs") – `compiler-v1.0.schema.json`
-   [global schema](./global.md "buildtest global schema is validated for all buildspecs") – `global.schema.json`
-   [python schema version 1.0](./python-v1.md "The script schema is of type: python in sub-schema which is used for running python scripts") – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json`
-   [script schema version 1.0](./script-v1.md "The script schema is of type: script in sub-schema which is used for running shell scripts") – `script-v1.0.schema.json`

## Other Schemas

### Objects

-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env-items.md) – `definitions.schema.json#/definitions/env/items`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env-items.md) – `definitions.schema.json#/definitions/env/items`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-status-properties-regex.md "Perform regular expression search using re") – `definitions.schema.json#/definitions/status/properties/regex`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env.md "One or more key value pairs for an environment (key=value)") – `definitions.schema.json#/definitions/env`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env-items.md) – `definitions.schema.json#/definitions/env/items`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-run_only.md "A set of conditions to specify when running tests") – `definitions.schema.json#/definitions/run_only`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-batch.md "The batch field is used to specify scheduler agnostic directives that are translated to #SBATCH or #BSUB based on your scheduler") – `definitions.schema.json#/definitions/batch`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-status.md "The status section describes how buildtest detects PASS/FAIL on test") – `definitions.schema.json#/definitions/status`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-status-properties-regex.md "Perform regular expression search using re") – `definitions.schema.json#/definitions/status/properties/regex`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-status-properties-regex.md "Perform regular expression search using re") – `definitions.schema.json#/definitions/status/properties/regex`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env-items.md) – `definitions.schema.json#/definitions/env/items`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-env-items.md) – `definitions.schema.json#/definitions/env/items`
-   [Untitled object in JSON Schema Definitions File. ](./definitions-definitions-status-properties-regex.md "Perform regular expression search using re") – `definitions.schema.json#/definitions/status/properties/regex`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers.md "Declare compiler section for defining system compilers that can be referenced in buildspec") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-find.md "Find compilers based on module names") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler.md "Start of compiler declaration") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-gcc.md "Declaration of one or more GNU compilers where we define C, C++ and Fortran compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/gcc`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-gcc-patternproperties-.md "A compiler section is composed of cc, cxx and fc wrapper these are required when you need to specify compiler wrapper") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/gcc/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-intel.md "Declaration of one or more Intel compilers where we define C, C++ and Fortran compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/intel`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-intel-patternproperties-.md "A compiler section is composed of cc, cxx and fc wrapper these are required when you need to specify compiler wrapper") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/intel/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-cray.md "Declaration of one or more Cray compilers where we define C, C++ and Fortran compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/cray`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-cray-patternproperties-.md "A compiler section is composed of cc, cxx and fc wrapper these are required when you need to specify compiler wrapper") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/cray/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-pgi.md "Declaration of one or more PGI compilers where we define C, C++ and Fortran compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/pgi`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-pgi-patternproperties-.md "A compiler section is composed of cc, cxx and fc wrapper these are required when you need to specify compiler wrapper") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/pgi/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-clang.md "Declaration of one or more Clang compilers where we define C, C++ compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/clang`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-clang-patternproperties-.md "The clang compiler section consist of cc and cxx wrapper to specify C and C++ wrapper which are generally clang and clang++") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/clang/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-cuda.md "Declaration of one or more Cuda compilers where we define C compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/cuda`
-   [Untitled object in buildtest configuration schema](./settings-properties-compilers-properties-compiler-properties-cuda-patternproperties-.md "The cuda compiler section consist of cc  where you generally specify path to nvcc") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/compiler/properties/cuda/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors.md "The executor section is used for declaring your executors that are responsible for running jobs") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-defaults.md "Specify default executor settings for all executors") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/defaults`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-local.md "The local section is used for declaring local executors for running jobs on local machine") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/local`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-local-patternproperties-.md "An instance object of local executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/local/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-lsf.md "The lsf section is used for declaring LSF executors for running jobs using LSF scheduler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/lsf`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-lsf-patternproperties-.md "An instance object of lsf executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/lsf/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-slurm.md "The slurm section is used for declaring Slurm executors for running jobs using Slurm scheduler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/slurm`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-slurm-patternproperties-.md "An instance object of slurm executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/slurm/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-cobalt.md "The cobalt section is used for declaring Cobalt executors for running jobs using Cobalt scheduler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/cobalt`
-   [Untitled object in buildtest configuration schema](./settings-properties-executors-properties-cobalt-patternproperties-.md "An instance object of cobalt executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/executors/properties/cobalt/patternProperties/^.*$`
-   [Untitled object in buildtest configuration schema](./settings-definitions-clang.md "The clang compiler section consist of cc and cxx wrapper to specify C and C++ wrapper which are generally clang and clang++") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/clang`
-   [Untitled object in buildtest configuration schema](./settings-definitions-cuda.md "The cuda compiler section consist of cc  where you generally specify path to nvcc") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cuda`
-   [Untitled object in buildtest configuration schema](./settings-definitions-compiler_section.md "A compiler section is composed of cc, cxx and fc wrapper these are required when you need to specify compiler wrapper") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section`
-   [Untitled object in buildtest configuration schema](./settings-definitions-local.md "An instance object of local executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/local`
-   [Untitled object in buildtest configuration schema](./settings-definitions-slurm.md "An instance object of slurm executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/slurm`
-   [Untitled object in buildtest configuration schema](./settings-definitions-lsf.md "An instance object of lsf executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/lsf`
-   [Untitled object in buildtest configuration schema](./settings-definitions-cobalt.md "An instance object of cobalt executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cobalt`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-batch.md "The batch field is used to specify scheduler agnostic directives that are translated to #SBATCH or #BSUB based on your scheduler") – `compiler-v1.0.schema.json#/properties/batch`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-env.md "One or more key value pairs for an environment (key=value)") – `compiler-v1.0.schema.json#/properties/env`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-vars.md "One or more key value pairs for an environment (key=value)") – `compiler-v1.0.schema.json#/properties/vars`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-run_only.md "A set of conditions to specify when running tests") – `compiler-v1.0.schema.json#/properties/run_only`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-status.md "The status section describes how buildtest detects PASS/FAIL on test") – `compiler-v1.0.schema.json#/properties/status`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-build.md "The build section is used for compiling a single program, this section specifies fields for setting C, C++, Fortran compiler and flags including CPP flags and linker flags") – `compiler-v1.0.schema.json#/properties/build`
-   [Untitled object in compiler schema version 1.0](./compiler-v1-properties-run.md "The run section is used for specifying launch configuration of executable") – `compiler-v1.0.schema.json#/properties/run`
-   [Untitled object in global schema](./global-properties-buildspecs.md "This section is used to define one or more tests (buildspecs)") – `global.schema.json#/properties/buildspecs`
-   [Untitled object in python schema version 1.0](./python-v1-properties-package.md) – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/package`
-   [Untitled object in python schema version 1.0](./python-v1-properties-status.md "The status section describes how buildtest detects PASS/FAIL on test") – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/status`
-   [Untitled object in script schema version 1.0](./script-v1-properties-batch.md "The batch field is used to specify scheduler agnostic directives that are translated to #SBATCH or #BSUB based on your scheduler") – `script-v1.0.schema.json#/properties/batch`
-   [Untitled object in script schema version 1.0](./script-v1-properties-env.md "One or more key value pairs for an environment (key=value)") – `script-v1.0.schema.json#/properties/env`
-   [Untitled object in script schema version 1.0](./script-v1-properties-vars.md "One or more key value pairs for an environment (key=value)") – `script-v1.0.schema.json#/properties/vars`
-   [Untitled object in script schema version 1.0](./script-v1-properties-run_only.md "A set of conditions to specify when running tests") – `script-v1.0.schema.json#/properties/run_only`
-   [Untitled object in script schema version 1.0](./script-v1-properties-status.md "The status section describes how buildtest detects PASS/FAIL on test") – `script-v1.0.schema.json#/properties/status`

### Arrays

-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-run_only-properties-linux_distro.md "Specify a list of Linux Distros to check when processing test") – `definitions.schema.json#/definitions/run_only/properties/linux_distro`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-int_or_list-oneof-1.md) – `definitions.schema.json#/definitions/int_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-string_or_list-oneof-1.md) – `definitions.schema.json#/definitions/string_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-list_of_strings.md) – `definitions.schema.json#/definitions/list_of_strings`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-string_or_list-oneof-1.md) – `definitions.schema.json#/definitions/string_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-list_of_ints.md) – `definitions.schema.json#/definitions/list_of_ints`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-int_or_list-oneof-1.md) – `definitions.schema.json#/definitions/int_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-string_or_list-oneof-1.md) – `definitions.schema.json#/definitions/string_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-sbatch.md "This field is used for specifying #SBATCH options in test script") – `definitions.schema.json#/definitions/sbatch`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-bsub.md "This field is used for specifying #BSUB options in test script") – `definitions.schema.json#/definitions/bsub`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-cobalt.md "This field is used for specifying #COBALT options in test script") – `definitions.schema.json#/definitions/cobalt`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-bb.md "Create burst buffer space, this specifies #BB options in your test") – `definitions.schema.json#/definitions/BB`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-dw.md "Specify Data Warp option (#DW) when using burst buffer") – `definitions.schema.json#/definitions/DW`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-run_only-properties-linux_distro.md "Specify a list of Linux Distros to check when processing test") – `definitions.schema.json#/definitions/run_only/properties/linux_distro`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-int_or_list-oneof-1.md) – `definitions.schema.json#/definitions/int_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-int_or_list-oneof-1.md) – `definitions.schema.json#/definitions/int_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-string_or_list-oneof-1.md) – `definitions.schema.json#/definitions/string_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-run_only-properties-linux_distro.md "Specify a list of Linux Distros to check when processing test") – `definitions.schema.json#/definitions/run_only/properties/linux_distro`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-int_or_list-oneof-1.md) – `definitions.schema.json#/definitions/int_or_list/oneOf/1`
-   [Untitled array in JSON Schema Definitions File. ](./definitions-definitions-string_or_list-oneof-1.md) – `definitions.schema.json#/definitions/string_or_list/oneOf/1`
-   [Untitled array in buildtest configuration schema](./settings-properties-buildspec_roots.md "Specify a list of directory paths to search buildspecs") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/buildspec_roots`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-gcc.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/gcc`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-intel.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/intel`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-cray.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/cray`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-clang.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/clang`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-cuda.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/cuda`
-   [Untitled array in buildtest configuration schema](./settings-properties-compilers-properties-find-properties-pgi.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/properties/compilers/properties/find/properties/pgi`
-   [Untitled array in buildtest configuration schema](./settings-definitions-compiler_section-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-compiler_section-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-compiler_section-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-compiler_section-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-clang-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/clang/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-cuda-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cuda/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-lsf-properties-options.md "Specify any options for bsub for this executor when running all jobs associated to this executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/lsf/properties/options`
-   [Untitled array in buildtest configuration schema](./settings-definitions-slurm-properties-options.md "Specify any other options for sbatch used by this executor for running all jobs") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/slurm/properties/options`
-   [Untitled array in buildtest configuration schema](./settings-definitions-cobalt-properties-options.md "Specify any options for qsub for this executor when running all jobs associated to this executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cobalt/properties/options`
-   [Untitled array in buildtest configuration schema](./settings-definitions-clang-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/clang/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-cuda-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cuda/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-compiler_section-properties-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/compiler_section/properties/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-unique_string_array.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/unique_string_array`
-   [Untitled array in buildtest configuration schema](./settings-definitions-modules.md "Specify list of modules to load when resolving compiler") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/modules`
-   [Untitled array in buildtest configuration schema](./settings-definitions-script.md) – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/script`
-   [Untitled array in buildtest configuration schema](./settings-definitions-slurm-properties-options.md "Specify any other options for sbatch used by this executor for running all jobs") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/slurm/properties/options`
-   [Untitled array in buildtest configuration schema](./settings-definitions-lsf-properties-options.md "Specify any options for bsub for this executor when running all jobs associated to this executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/lsf/properties/options`
-   [Untitled array in buildtest configuration schema](./settings-definitions-cobalt-properties-options.md "Specify any options for qsub for this executor when running all jobs associated to this executor") – `https://buildtesters.github.io/buildtest/schemas/settings.schema.json#/definitions/cobalt/properties/options`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-module.md "A list of modules to load into test script") – `compiler-v1.0.schema.json#/properties/module`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-sbatch.md "This field is used for specifying #SBATCH options in test script") – `compiler-v1.0.schema.json#/properties/sbatch`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-bsub.md "This field is used for specifying #BSUB options in test script") – `compiler-v1.0.schema.json#/properties/bsub`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-cobalt.md "This field is used for specifying #COBALT options in test script") – `compiler-v1.0.schema.json#/properties/cobalt`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-bb.md "Create burst buffer space, this specifies #BB options in your test") – `compiler-v1.0.schema.json#/properties/BB`
-   [Untitled array in compiler schema version 1.0](./compiler-v1-properties-dw.md "Specify Data Warp option (#DW) when using burst buffer") – `compiler-v1.0.schema.json#/properties/DW`
-   [Untitled array in global schema](./global-properties-maintainers.md "One or more maintainers or aliases") – `global.schema.json#/properties/maintainers`
-   [Untitled array in python schema version 1.0](./python-v1-properties-pyver.md) – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/pyver`
-   [Untitled array in python schema version 1.0](./python-v1-properties-package-properties-pypi.md) – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/package/properties/pypi`
-   [Untitled array in python schema version 1.0](./python-v1-properties-module.md) – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/module`
-   [Untitled array in python schema version 1.0](./python-v1-properties-sbatch.md "This field is used for specifying #SBATCH options in test script") – `https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/sbatch`
-   [Untitled array in script schema version 1.0](./script-v1-properties-sbatch.md "This field is used for specifying #SBATCH options in test script") – `script-v1.0.schema.json#/properties/sbatch`
-   [Untitled array in script schema version 1.0](./script-v1-properties-bsub.md "This field is used for specifying #BSUB options in test script") – `script-v1.0.schema.json#/properties/bsub`
-   [Untitled array in script schema version 1.0](./script-v1-properties-cobalt.md "This field is used for specifying #COBALT options in test script") – `script-v1.0.schema.json#/properties/cobalt`
-   [Untitled array in script schema version 1.0](./script-v1-properties-bb.md "Create burst buffer space, this specifies #BB options in your test") – `script-v1.0.schema.json#/properties/BB`
-   [Untitled array in script schema version 1.0](./script-v1-properties-dw.md "Specify Data Warp option (#DW) when using burst buffer") – `script-v1.0.schema.json#/properties/DW`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`