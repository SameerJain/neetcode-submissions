from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str | None:
    max_val = float('-inf')
    max_name = None
    for name, score in scores:
        if score > max_val:
            max_val = score
            max_name = name
    return max_name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
