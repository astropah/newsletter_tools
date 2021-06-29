
from typing import Dict, List
from pathlib import Path
from ruamel.yaml import YAML


def get_yaml_data(filepath: str) -> Dict[str, str]:
    target = Path(filepath)
    if target.exists():
        reader = YAML()
        with open(target, "r") as read_file:
            return reader.load(read_file)
    else:
        raise FileNotFoundError(f"{filepath} is not found, expecting YAML file.")


def extract_authors(author_list: str) -> List[str]:
    return author_list.split(";")