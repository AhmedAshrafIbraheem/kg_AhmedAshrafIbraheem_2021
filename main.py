import sys


def can_map_strings(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    mapper: Dict[str, str] = {}
    for i in range(len(s1)):
        if s1[i] not in mapper:
            mapper[s1[i]] = s2[i]
        else:
            if mapper[s1[i]] != s2[i]:
                return False

    return True


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(can_map_strings(sys.argv[1], sys.argv[2]))
    else:
        print("Incomplete Input")
