"""
Name: AustralianVoting.py

Purpose: Determine winner out of a choice based voting system

Date: 07/25/18

Author: Zhang.G
"""

import sys
from collections import Counter


def vote_result(num_candidates, start, end):
    votes = [line.split(" ") for line in all_data[start:end]]
    choice = [int(line[0]) for line in votes]
    removed = []

    for n in range(num_candidates):

        count = Counter()
        candidate_list = [i for i in range(1, num_candidates + 1) if i not in removed]
        for vote in choice:
            count[vote] += 1

        max_value = max(count.values())

        if sum([count[key] for key in count if count[key] == max_value]) == end-start:
            return [key - 1 for key in count if count[key] == max_value]

        elif max_value/len(choice) <= 0.5:
            if len(count) == len(candidate_list):
                min_value = min(count.values())
                [removed.append(key) for key in count if count[key] == min_value]
            else:
                [removed.append(key) for key in candidate_list if key not in count]

            for k in range(len(choice)):
                counter = 0
                while choice[k] in removed:
                    choice[k] = int(votes[k][counter])
                    counter += 1

        else:
            return sorted([key - 1 for key in count if count[key] == max_value])


def main():
    global all_data
    all_data = sys.stdin.read().split('\n')
    all_data.append('')
    split_cases = [i for i, j in enumerate(all_data) if j == '']

    for n in range(int(all_data[0])):
        case = int(split_cases[n]) + 2
        num_candidates = int(all_data[case - 1])
        candidate_names = all_data[case:case + num_candidates]

        results = vote_result(num_candidates, case + num_candidates, split_cases[n + 1])
        results = sorted(results)

        [print(candidate_names[candidate]) for candidate in results]

        if n + 1 != int(all_data[0]):
            print('')


if __name__ == "__main__":
    main()
