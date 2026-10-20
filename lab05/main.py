from logstats import parse_event, count_levels, format_report

with open("events.log", "r", encoding="utf-8") as file:
    for line in file.readlines():
        res_1 = parse_event(line)

    res_2 = count_levels(file)

print(format_report(res_1, res_2))