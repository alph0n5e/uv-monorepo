# UV Monorepo

An example Python mono-repository built with [UV](https://docs.astral.sh/uv/).

This illustrates a setup with no workspaces, each library and app is meant to be installed and tested in its own virtual environment.

Local dependencies are indicated with `[tool.uv.sources] myorg-utils = { path = "../utils" }`.

## Overview
This project presents two skeleton libraries and two applications, with the following depdendencies:

- `libs/utils`, a standalone utility library,
- `libs/core`, the core buisness logic library, depending on `utils`,
- `apps/api`, the main API, depending on `core`,
- `apps/cli`, a CLI application, depdending on both `core` and `utils` (although `utils` is already a dependency of `core`, it is good practice to make it explicit if `cli` uses it directly),

The idea is that:
- applications *can* depend on one or many libraries,
- libraries *can* depend on other libraries,

but:
- libraries **cannot** depend on applications,
- applications **cannot** depend on other applications,

## Tooling

Running `ruff check` with `uv tool run` (or `uvx`):
```
uvx ruff check
```
will run it in a one-off environment.

If yo want to install tool dependencies, you can:
```
uv tool install ruff
```
and then run `ruff` globally

## Namespace

This example project uses the namespace `myorg` to demonstrate a namespace-based architecture for the packages of the monorepo.

Each library (under `libs`) and application (under `apps`) use the same namespace.

For example, `myorg-core`, in `libs/core` uses the following struture:
```
core/
    myorg/
        # specifically no __init__.py
        core/
            __init__.py
            ...
    pyproject.toml
    ...
```

and is imported as follows:
```python
from myorg.core import hello
...
```

Namespaces are discovered by default by the `setuptools` build system, however they may need to be specified explicitly in other build systems.

E.g. with `Poetry`:
```toml
[tool.poetry]
...
packages = [
  { include = "myorg" }
]
...
```