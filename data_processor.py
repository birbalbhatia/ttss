"""
Data processing module with various performance issues.
This module demonstrates common performance anti-patterns.
"""
import time
import json


def process_data_inefficiently(data_list):
    """Process data using inefficient patterns."""
    result = []
    
    # Issue 1: Inefficient list concatenation in loop
    for item in data_list:
        result = result + [item * 2]  # Creates new list each time
    
    return result


def find_duplicates_slow(data_list):
    """Find duplicates using nested loops - O(n²) complexity."""
    duplicates = []
    
    # Issue 2: Nested loop causing quadratic time complexity
    for i in range(len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i] == data_list[j] and data_list[i] not in duplicates:
                duplicates.append(data_list[i])
    
    return duplicates


def filter_and_transform_data(data_list, threshold):
    """Filter and transform data inefficiently."""
    # Issue 3: Multiple passes over data instead of single pass
    filtered_data = []
    for item in data_list:
        if item > threshold:
            filtered_data.append(item)
    
    transformed_data = []
    for item in filtered_data:
        transformed_data.append(item ** 2)
    
    return transformed_data


def compute_statistics(numbers):
    """Compute statistics with redundant calculations."""
    # Issue 4: Redundant calculations - sorting multiple times
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    median = sorted_nums[len(numbers) // 2]
    
    # Sorting again for no reason
    sorted_nums_2 = sorted(numbers)
    minimum = sorted_nums_2[0]
    maximum = sorted_nums_2[-1]
    
    return {
        'mean': mean,
        'median': median,
        'min': minimum,
        'max': maximum
    }


def process_json_data(json_string):
    """Process JSON data with inefficient string operations."""
    # Issue 5: Repeated JSON parsing
    data = json.loads(json_string)
    
    result = {}
    if 'users' in json.loads(json_string):
        result['user_count'] = len(json.loads(json_string)['users'])
    
    if 'products' in json.loads(json_string):
        result['product_count'] = len(json.loads(json_string)['products'])
    
    return result


def search_in_list(data_list, target):
    """Search for items in a list inefficiently."""
    # Issue 6: Linear search when better data structures exist
    found_items = []
    
    for item in data_list:
        if item == target:
            found_items.append(item)
    
    return found_items


class DataCache:
    """Cache implementation with no eviction policy."""
    
    def __init__(self):
        # Issue 7: Unbounded cache can lead to memory issues
        self.cache = {}
    
    def get(self, key):
        """Get value from cache."""
        return self.cache.get(key)
    
    def set(self, key, value):
        """Set value in cache without any size limits."""
        self.cache[key] = value
    
    def clear(self):
        """Clear the cache."""
        self.cache = {}


def generate_report(data_items):
    """Generate a report using string concatenation in loop."""
    # Issue 8: String concatenation in loop is inefficient
    report = ""
    
    for item in data_items:
        report = report + f"Item: {item['name']}, Value: {item['value']}\n"
    
    return report


def calculate_factorial_recursive(n):
    """Calculate factorial using naive recursion."""
    # Issue 9: No memoization, causes redundant calculations
    if n <= 1:
        return 1
    return n * calculate_factorial_recursive(n - 1)


def process_large_file(filename):
    """Read entire file into memory at once."""
    # Issue 10: Loading entire file into memory
    with open(filename, 'r') as f:
        content = f.read()
    
    # Process all at once
    lines = content.split('\n')
    processed = []
    for line in lines:
        if line.strip():
            processed.append(line.upper())
    
    return processed


if __name__ == "__main__":
    # Example usage demonstrating the performance issues
    print("Running inefficient data processing examples...")
    
    # Test 1: Inefficient list operations
    data = list(range(1000))
    start = time.time()
    result = process_data_inefficiently(data)
    print(f"Process data: {time.time() - start:.4f}s")
    
    # Test 2: Duplicate detection with O(n²)
    data_with_dupes = [1, 2, 3, 4, 2, 5, 3, 6, 1]
    start = time.time()
    dupes = find_duplicates_slow(data_with_dupes)
    print(f"Find duplicates: {time.time() - start:.4f}s")
    
    # Test 3: Multiple passes over data
    data = list(range(100))
    start = time.time()
    filtered = filter_and_transform_data(data, 50)
    print(f"Filter and transform: {time.time() - start:.4f}s")
    
    # Test 4: Redundant sorting
    numbers = [5, 2, 8, 1, 9, 3, 7]
    start = time.time()
    stats = compute_statistics(numbers)
    print(f"Compute statistics: {time.time() - start:.4f}s")
    print(f"Statistics: {stats}")
