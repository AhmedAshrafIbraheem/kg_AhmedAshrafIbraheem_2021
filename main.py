import sys


def can_map_strings(s1: str, s2: str) -> bool:
    return True


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(can_map_strings(sys.argv[1], sys.argv[2]))
    else:
        print("Incomplete Input")
