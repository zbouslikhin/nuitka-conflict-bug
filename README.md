# Setup to reproduce: [Nuitka#3185](https://github.com/Nuitka/Nuitka/issues/3185)

## Step

1. Install [Poetry](https://python-poetry.org/docs/)
2. `poetry install`
3. Compile using: `poetry run python -m nuitka --deployment --standalone --onefile --msvc=latest --follow-imports .\mypackage\to_build.py`
