"""TOMLlib module for open toml files."""

import tomllib
from pathlib import Path

toml_file_path = Path(__file__).parent / "extras" / "sample.toml"

# There is a built-in error in Tomllib in this version of python! :: "Python 3.11.0"
with open(toml_file_path, "r") as toml_file:
    content = tomllib.loads(toml_file.read())

print(content)
