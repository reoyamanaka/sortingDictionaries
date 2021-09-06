from typing import List, Dict


def customBubbleSort(ar: List[Dict], key: str, ascending = True) -> None:
    for i in range(len(ar)):
        for j in range(len(ar) - i - 1):
            if ascending:
                if ar[j][key] > ar[j + 1][key]:
                    temp = ar[j + 1]
                    ar[j + 1] = ar[j]
                    ar[j] = temp
            else:
                if ar[j][key] < ar[j + 1][key]:
                    temp = ar[j + 1]
                    ar[j + 1] = ar[j]
                    ar[j] = temp
    return None