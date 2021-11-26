import argparse
import os
import sys

WIN = 3
TIE = 1


def validate_args(arguments):
    input_file = arguments.input
    if not os.path.exists(input_file):
        return f'File {input_file} does not exist. Exiting...'


def calculate_scores(all_scores):
    scores_table = {}
    for team_scores in all_scores:
        score = team_scores.split(', ')
        team1, team1_score = get_team_and_score(score[0])
        team2, team2_score = get_team_and_score(score[1])

        if team1 not in scores_table:
            scores_table[team1] = 0
        if team2 not in scores_table:
            scores_table[team2] = 0

        if team2_score == team1_score:
            scores_table[team1] = scores_table[team1] + TIE
            scores_table[team2] = scores_table[team2] + TIE
        elif team1_score > team2_score:
            scores_table[team1] = scores_table[team1] + WIN
        else:
            scores_table[team2] = scores_table[team2] + WIN

    return {val[0]: val[1] for val in
            sorted(scores_table.items(),
                   key=lambda x: (-x[1], x[0]))}


def get_team_and_score(score):
    team_name = score[0: score.rfind(' ')]
    team_score = int(score[score.rfind(' ') + 1:])
    return team_name, team_score


def main():
    parser = argparse.ArgumentParser(description='Process some scores')
    parser.add_argument('--input', type=str, dest='input',
                        help='Input file with scores')
    args = parser.parse_args()

    if len(sys.argv) != 3:
        print('Type "python scores.py -h" for options')
        sys.exit(0)

    error_msg = validate_args(args)
    if error_msg:
        print(error_msg)
    else:
        with open(args.input, 'r') as scores_file:
            results = calculate_scores(scores_file.readlines())
            count = 1
            for k, v in results.items():
                print(f'{count}. {k}, {v} pts')
                count += 1


if __name__ == "__main__":
    main()
