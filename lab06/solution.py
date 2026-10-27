def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}

    for path in paths:
        filename = path.split("/")[-1]

        if "." in filename:
            extension = filename.split(".")[-1].lower()
        else:
            extension = ""

        if extension in counts:
            counts[extension] += 1
        else:
            counts[extension] = 1

    return counts


def deepest_path(paths: list[str]) -> str:
    deepest = ""
    max_depth = -1

    for path in sorted(paths):
        depth = path.count("/")

        if depth > max_depth:
            max_depth = depth
            deepest = path

    return deepest


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size = size / 1024
        unit_index += 1

    if unit_index == 0:
        return f"{n_bytes} Б"
    else:
        return f"{size:.1f} {units[unit_index]}"