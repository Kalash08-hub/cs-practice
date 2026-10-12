import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

    invalid_count = sum(
        1 for line in lines
        if line.strip()
    ) - len(records)

    print(len(records))
    print(invalid_count)

    if records:
        city = warmest_city(records)
        averages = average_by_city(records)
        print(f"{averages[city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()