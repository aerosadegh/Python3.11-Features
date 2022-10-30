"""TOMLlib module for open toml files."""

import tomllib
from datetime import datetime
from pathlib import Path
from pprint import pprint


def get_toml_content(toml_file_path: Path):
    with open(toml_file_path, "rb") as toml_file:
        content = tomllib.load(toml_file)

    # process datetime string to Datetime object
    content["process"]["start"] = datetime.fromisoformat(content["process"]["start"])
    return content


def main():
    content = get_toml_content(
        toml_file_path=Path(__file__).parent.joinpath("extras/sample.toml")
    )
    pprint(content)


if __name__ == "__main__":
    main()
    print()
