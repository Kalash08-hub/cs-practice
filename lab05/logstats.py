from datetime import datetime

def parse_event(line):
    fields = line.split()

    if len(line) < 3:
        raise ValueError("Негодная строка")

    time = fields[0]
    level = fields[1]
    message = " ".join(fields[2:])
    try:
        level  in ["DEBUG", "INFO", "WARNING", "ERROR"]
    except ValueError:
        raise ValueError("негодная строка")

    """try:
        datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("Негодная строка")"""

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines):
    res = {}

    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            res["level"] = res.get("BROKEN", 0) + 1

        res[event["level"]] = res.get(event["level"], 0) + 1

    return res


def top_errors(lines, n):

    count = {}

    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            count[message] = count.get(message, 0) + 1

    sorted_errors = sorted(
        count.items(),
        key=lambda x: (-x[1], x[0]),
    )

    top_errors = sorted_errors[:n]

    return top_errors

def format_report(counts, errors):
    report = "Отчёт по журналу\n\n"

    for level in sorted(counts):
        report += f"{level}: {counts[level]}\n"

    report += "\nЧастые ошибки:\n"

    for message, amount in errors.items():
        report += f"- {message} — {amount}\n"

    return report