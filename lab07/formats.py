import json

def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()

    if not lines:
        return []

    headers = [header.strip() for header in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue

        values = [value.strip() for value in line.split(",")]
        records.append(dict(zip(headers, values)))

    return records

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_key = None

    for line in lines:
        line = line.split("#")[0].strip()

        if not line:
            continue

        if line.startswith("- "):
            if current_key is not None:
                value = line[2:].strip()
                settings[current_key].append(convert_value(value))
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value == "":
                settings[key] = []
                current_key = key
            else:
                settings[key] = convert_value(value)
                current_key = None

    return settings

def convert_value(value: str):
    if value.lower() in ("true", "yes"):
        return True

    if value.lower() in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value.replace(",", "."))
    except ValueError:
        pass

    return value

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        row_key = row.get(key)
        additional = extra.get(row_key, {})

        merged = additional.copy()
        merged.update(row)

        result.append(merged)

    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, sort_keys=True, indent=2)
