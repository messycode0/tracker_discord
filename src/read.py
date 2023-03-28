def read_file_whole(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()