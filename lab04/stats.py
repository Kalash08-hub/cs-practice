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
        temp = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }


def read_valid(lines: list[str]):
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
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}

    for city in total:
        averages[city] = round(total[city] / count[city], 1)

    return averages


def warmest_city(records: list[dict]):
    averages = average_by_city(records)

    if not averages:
        return ""

    return sorted(averages, key=lambda city: (-averages[city], city))[0]
