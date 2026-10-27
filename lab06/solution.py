def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        extension = path.rsplit("/", 1)[-1].rpartition(".")[2].lower() if "." in path.rsplit("/", 1)[-1] else ""
        counts[extension] = counts.get(extension, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    return min(paths, key=lambda path: (-path.count("/"), path), default="")


def human_size(n_bytes: int) -> str:
    size = n_bytes
    for unit in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        if size < 1024 or unit == "ТБ":
            return f"{size:.0f} Б" if unit == "Б" else f"{size:.1f} {unit}"
        size /= 1024