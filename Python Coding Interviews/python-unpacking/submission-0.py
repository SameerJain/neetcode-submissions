from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    assert len(triplet) == 3, ValueError (f"Expected 3 items, got {len(triplet)}")
    val1,val2,val3 = triplet[0],triplet[1],triplet[2]
    return val1 + val2 + val3


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    assert len(box_dimensions) == 3, ValueError (f"Expected 1 item, got {len(box_dimensions)}")
    val1,val2,val3 = box_dimensions[0],box_dimensions[1],box_dimensions[2]
    return val1 * val2 * val3
    
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
