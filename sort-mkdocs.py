#!/usr/bin/env python3
import sys


def section_idxs_to_lines(section):
    """Changes a tuple holding line idxs (start_idx, end_idx) to lines (strat_line, end_line)"""
    return (section[0] + 1, section[1] + 1)


def check_sections_order(sections):
    for section in sections:
        if section[1] < section[0]:
            section = section_idxs_to_lines(section)
            print("End marker has to be placed after a start marker")
            print(f"End marker at {section[0]}, start marker at {section[1]}")
            exit(1)


def check_sections_overlap(sections):
    for i in range(1, len(sections)):
        previous_end = sections[i - 1][1]
        next_start = sections[i][0]
        if next_start < previous_end:
            print("Sections to sort can't overlap")
            section_a = section_idxs_to_lines(sections[i - 1])
            section_b = section_idxs_to_lines(sections[i])
            print(f"Section {section_a} overlaps with {section_b}")
            exit(1)


def main():
    """Sorts sections of a file marked by special markers passed as arguments
    Usage:
        <executable> [file-name] "[start-marker]" "[end-marker]"
    """
    file_path="mkdocs.yml"
    start_marker="#pre-commit-sort-start"
    end_marker="#pre-commit-sort-end"
    # Read args
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]
    if len(sys.argv) >= 3:
        start_marker = sys.argv[2]
    if len(sys.argv) >= 4:
        end_marker = sys.argv[3]

    # Find sections in file
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    start_lines = [idx for idx, s in enumerate(lines) if start_marker in s]
    end_lines = [idx for idx, s in enumerate(lines) if end_marker in s]
    sections_to_sort = list(zip(start_lines, end_lines))

    # Input validation
    if not len(start_lines) > 0:
        print(f'No start markers found in the file. Expected marker: "{start_marker}"')
        exit(1)
    if len(start_lines) != len(end_lines):
        print(
            f"Number of start markers (lines: {start_lines}) does not equal number of end markers (lines: {end_lines})"
        )
        exit(1)
    check_sections_order(sections_to_sort)
    check_sections_overlap(sections_to_sort)

    # Sorting
    changed = False
    for start_idx, end_idx in zip(start_lines, end_lines):
        to_sort = lines[start_idx + 1 : end_idx]
        to_sort.sort()
        if lines[start_idx + 1 : end_idx] != to_sort:
            changed = True
        lines[start_idx + 1 : end_idx] = to_sort

    # Write changes
    if changed:
        with open(file_path, "w") as file:
            file.writelines([line + "\n" for line in lines])
        exit(1)
    exit(0)

    


if __name__ == "__main__":
    main()
