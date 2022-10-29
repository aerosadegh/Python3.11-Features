"""TOMLlib module for open toml files."""

import tomllib
from datetime import datetime
from pathlib import Path

toml_file_path = Path(__file__).parent.joinpath("extras/sample.toml")

with open(toml_file_path, "rb") as toml_file:
    content = tomllib.load(toml_file)

content["process"]["start"] = datetime.fromisoformat(content["process"]["start"])
print(content)
