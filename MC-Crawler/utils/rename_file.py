from pathlib import Path


def remove_invalid_symbol(dir_path: Path):
    invalid_chars = ['?', '*', ':', '"', '<', '>', '|', '\\', '/']
    for fd_path in dir_path.iterdir():
        if fd_path.is_file():
            old_name = fd_path.name
            # breakpoint()
            for char in invalid_chars:
                old_name = old_name.replace(char, '_')
            new_name = old_name
            if new_name != fd_path.name:
                print(f"{fd_path.name} -> {new_name}")
                # breakpoint()
                fd_path.rename(fd_path.with_name(new_name))
        elif fd_path.is_dir():
            remove_invalid_symbol(fd_path)

if __name__ == '__main__':
    remove_invalid_symbol(Path(__file__).parent.parent / 'crawler_data')

