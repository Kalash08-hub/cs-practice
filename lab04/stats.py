def parse_record(line: str):
    fields = line.split(";")

    if len(fields) != 3:
        raise ValueError("В записи должно быть ровно три поля")

    city, temp, date = fields

    city = city.strip()
    temp = temp.strip()
    date = date.strip()

    if not city:
        raise ValueError("Название города не может быть пустым")

    if not date:
        raise ValueError("Дата не может быть пустой")

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temp": temp,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records

def average_by_city(records: list[dict]):
    pass

def warmest_city(records: list[dict]):
    pass
