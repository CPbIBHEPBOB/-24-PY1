import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)


        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILENAME}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':

    task()


    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
