from logstats import top_errors, count_levels, format_report

def main():
    path = input().strip()
    with open(path, encoding="utf-8") as log:

        count = count_levels(log)

        log.seek(0)

        errors = top_errors(log, 3)

    print(format_report(count, errors))

if __name__ == "__main__":
    main()