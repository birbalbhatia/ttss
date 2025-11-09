"""
Optimized data processing module with performance improvements.
This module demonstrates best practices for efficient code.
"""
import json
from functools import lru_cache
from collections import Counter, OrderedDict


def process_data_efficiently(data_list):
    """Process data using efficient list comprehension."""
    # Improvement 1: Use list comprehension instead of repeated concatenation
    # Time complexity: O(n) instead of O(n²)
    return [item * 2 for item in data_list]


def find_duplicates_fast(data_list):
    """Find duplicates using Counter - O(n) complexity."""
    # Improvement 2: Use Counter for O(n) time complexity
    counts = Counter(data_list)
    return [item for item, count in counts.items() if count > 1]


def filter_and_transform_data_efficient(data_list, threshold):
    """Filter and transform data in a single pass."""
    # Improvement 3: Single pass with generator expression
    return [item ** 2 for item in data_list if item > threshold]


def compute_statistics_optimized(numbers):
    """Compute statistics efficiently with single sort."""
    # Improvement 4: Sort once and reuse
    sorted_nums = sorted(numbers)
    n = len(numbers)
    
    # Calculate median correctly for both odd and even length lists
    if n % 2 == 0:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median = sorted_nums[n // 2]
    
    return {
        'mean': sum(numbers) / n,
        'median': median,
        'min': sorted_nums[0],
        'max': sorted_nums[-1]
    }


def process_json_data_efficient(json_string):
    """Process JSON data efficiently by parsing once."""
    # Improvement 5: Parse JSON once and reuse
    data = json.loads(json_string)
    
    return {
        'user_count': len(data.get('users', [])),
        'product_count': len(data.get('products', []))
    }


def search_in_set(data_set, target):
    """Search using set for O(1) lookup."""
    # Improvement 6: Use set for O(1) lookup instead of O(n) list search
    return target in data_set


class DataCacheOptimized:
    """Cache implementation with LRU eviction policy using OrderedDict."""
    
    def __init__(self, max_size=1000):
        # Improvement 7: Bounded cache with size limit using OrderedDict for O(1) operations
        self.max_size = max_size
        self.cache = OrderedDict()
    
    def get(self, key):
        """Get value from cache and update access order."""
        if key in self.cache:
            # Move to end to mark as recently used (O(1) operation)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        """Set value in cache with LRU eviction."""
        if key in self.cache:
            # Update existing key and move to end (O(1) operation)
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.max_size:
            # Evict least recently used item (first item, O(1) operation)
            self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def clear(self):
        """Clear the cache."""
        self.cache.clear()


def generate_report_efficient(data_items):
    """Generate report using list join for efficiency."""
    # Improvement 8: Use list and join instead of string concatenation
    lines = [f"Item: {item['name']}, Value: {item['value']}" 
             for item in data_items]
    return '\n'.join(lines)


@lru_cache(maxsize=128)
def calculate_factorial_memoized(n):
    """Calculate factorial with memoization."""
    # Improvement 9: Use lru_cache for automatic memoization
    if n <= 1:
        return 1
    return n * calculate_factorial_memoized(n - 1)


def process_large_file_streaming(filename):
    """Process file line by line to minimize memory usage."""
    # Improvement 10: Stream file processing instead of loading all at once
    processed = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                processed.append(line.upper())
    return processed


# Alternative generator version for even better memory efficiency
def process_large_file_generator(filename):
    """Process file using generator for minimal memory footprint."""
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line.upper()


if __name__ == "__main__":
    import time
    
    print("Running optimized data processing examples...")
    
    # Test 1: Efficient list operations
    data = list(range(1000))
    start = time.time()
    result = process_data_efficiently(data)
    print(f"Process data (optimized): {time.time() - start:.4f}s")
    
    # Test 2: Fast duplicate detection
    data_with_dupes = [1, 2, 3, 4, 2, 5, 3, 6, 1]
    start = time.time()
    dupes = find_duplicates_fast(data_with_dupes)
    print(f"Find duplicates (optimized): {time.time() - start:.4f}s")
    
    # Test 3: Single-pass filtering
    data = list(range(100))
    start = time.time()
    filtered = filter_and_transform_data_efficient(data, 50)
    print(f"Filter and transform (optimized): {time.time() - start:.4f}s")
    
    # Test 4: Efficient statistics
    numbers = [5, 2, 8, 1, 9, 3, 7]
    start = time.time()
    stats = compute_statistics_optimized(numbers)
    print(f"Compute statistics (optimized): {time.time() - start:.4f}s")
    print(f"Statistics: {stats}")
