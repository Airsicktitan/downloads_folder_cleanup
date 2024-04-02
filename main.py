from directory_handle import make_dir, send_item_to_compare


def main() -> None:
    make_dir()
    print('\n')
    send_item_to_compare()
    
if __name__ == "__main__":
    main()