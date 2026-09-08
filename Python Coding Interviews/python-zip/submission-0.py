from typing import List, Dict


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    student_map_score = {}
    for name, score in zip(names, scores):     
        student_map_score[name] = score
    return student_map_score


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
