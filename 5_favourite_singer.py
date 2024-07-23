def max_duplicate_number(playlist):
    frequency = {}
    for num in playlist:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    max_duplicate = [num for num, count in frequency.items() if count == max_count]

    return len(max_duplicate)

songs = int(input())

playlist = list(input().split())

print(max_duplicate_number(playlist))