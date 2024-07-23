def longest_seq():
    #input the row and column
    row, column = map(int, input().split())

    #represents the smallest possible number
    max_seq = float('-inf')

    for _ in range(row):
        row_data = input()
        start = row_data.find('#')
        if start < 0:
            continue
        end = row_data.find('.', start)
        max_seq = max(max_seq, end - start)

    print(max_seq)

test_cases = int(input())
for _ in range(test_cases):
    longest_seq()