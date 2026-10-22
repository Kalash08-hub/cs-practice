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

    try:
        datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("Негодная строка")

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
            Level = event.get("level", "BROKEN")
            if Level == "строка" or Level == "TRACE":
                Level = "BROKEN"

        except ValueError:
            Level = "BROKEN"

        res[Level] = res.get(Level, 0) + 1
    return res


def top_errors(lines):

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
        key=lambda x: x[1], reverse=True
    )

    return sorted_errors


def format_report(counts, errors):
    report = "Отчёт по журналу\n\n"

    for level in sorted(counts):
        report += f"{level}: {counts[level]}\n"

    report += "\nЧастые ошибки:\n"

    for message, count in errors:
        report += f"- {message} — {count}\n"

    return report