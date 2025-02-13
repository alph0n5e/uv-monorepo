# UV Monorepo

An example Python mono-repository built with [UV](https://docs.astral.sh/uv/).

This illustrates a setup with no workspaces, each library and app is meant to be installed and tested in its own virtual environment.

Local dependencies are indicated with `[tool.uv.sources] myorg-utils = { path = "../utils" }`.

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