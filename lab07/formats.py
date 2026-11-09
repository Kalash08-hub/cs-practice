import csv
import io
import json


def csv_to_records(text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(text)))


def _parse_value(value: str):
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    list_key = None

    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue

        if line.startswith("- ") or line == "-":
            if list_key is None:
                raise ValueError("Элемент списка без ключа")
            settings[list_key].append(_parse_value(line[1:].strip()))
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            settings[key] = _parse_value(value)
            list_key = None
        else:
            settings[key] = []
            list_key = key

    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    return [{**extra.get(row.get(key), {}), **row} for row in rows]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, sort_keys=True, indent=2)
