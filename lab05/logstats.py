def parse_event(line):
    fields = line.split()

    time = fields[0]
    level = fields[1]
    message = fields[2:]

    if level not in ["DEBUG", "INFO", "WARNING", "ERROR"] or len(time) != 19 or not message:
        raise ValueError ("негодная строка")

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines):
    lines = lines.readlines()
    broken_count = 0
    debug_count = 0
    error_count = 0
    info_count = 0
    warning_count = 0

    for line in lines:
        if parse_event(line)["level"] == "DEBUG":
            debug_count += 1
        elif parse_event(line)["level"] == "ERROR":
            error_count += 1
        elif parse_event(line)["level"] == "INFO":
            info_count += 1
        elif parse_event(line)["level"] == "WARNING":
            warning_count += 1
        else:
            broken_count += 1
    return{
        "BROKEN": broken_count,
        "DEBUG": debug_count,
        "ERROR": error_count,
        "INFO": info_count,
        "WARNING": warning_count,
    }