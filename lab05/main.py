from logstats import top_errors, count_levels, format_report

with open("events.log", "r", encoding="utf-8") as file:

    res_1 = count_levels(file)
    file.seek(0)
    res_2 = top_errors(file, 3)

print(format_report(res_1, res_2))