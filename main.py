import sys
from typing import Dict


def can_map_strings(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
    	# length of first string is longer
    	# than that of the second one so there
    	# will be no possible mapping between them
        return False

    # mapper store every character with its mapped value 
    mapper: Dict[str, str] = {}

    for i in range(len(s1)):
        if s1[i] not in mapper:
            # if the character is new
            # add it to our mapper
            mapper[s1[i]] = s2[i]
        else:
            if mapper[s1[i]] != s2[i]:
                # if the character is already in our mapper
        	# and it has a value that is different from
        	# the current character, that means there
    		# will be no possible mapping
                return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(can_map_strings(sys.argv[1], sys.argv[2]))
    else:
        print("Incomplete Input")
