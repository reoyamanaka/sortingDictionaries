from typing import List, Dict


sampleList = [{"minTemp": 4, "maxTemp": 10},{"minTemp": -4, "maxTemp": 18}, {"minTemp": 4, "maxTemp": 10}, {"minTemp": 2, "maxTemp": 12}]

def bubbleSort(ar: List[Dict], key: str) -> None:
    for i in range(len(ar)):
        for j in range(len(ar) - i - 1):
            if ar[j][key] > ar[j + 1][key]:
                temp = ar[j + 1]
                ar[j + 1] = ar[j]
                ar[j] = temp
    return None

bubbleSort(sampleList, "minTemp")

print(sampleList)
