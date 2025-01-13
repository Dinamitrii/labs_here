def convert_size_in_bytes(size_in_bytes: int, size_only: bool = False) -> int | str:
    size_bytes = int(size_in_bytes)
    if size_bytes == 0:
        return "0B"  # Handle the case when size is 0
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024
        i += 1
    if size_only:
        return int(size_bytes)
    else:
        return f"{size_bytes:.2f} {size_names[i]}"


print(convert_size_in_bytes(65754))
