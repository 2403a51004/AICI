from typing import List, Tuple, Dict

def sum_duplicate_keys(pairs: List[Tuple[str, int]]) -> Dict[str, int]:
    """Sum values for duplicate keys in a list of (str, int) tuples."""
    result: Dict[str, int] = {}
    for key, value in pairs:
        result[key] = result.get(key, 0) + value
    return result

# Example usage
if __name__ == "__main__":
    data = [('a', 1), ('b', 2), ('a', 3)]
    print(sum_duplicate_keys(data))  # Output: {'a': 4, 'b': 2}