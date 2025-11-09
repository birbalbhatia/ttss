# Performance Optimization Guide

This repository demonstrates common performance issues in Python code and their optimized solutions.

## Overview

The codebase includes:
- `data_processor.py` - Original code with performance issues
- `data_processor_optimized.py` - Optimized version with improvements
- `benchmark.py` - Performance comparison benchmarks

## Performance Issues Identified

### 1. Inefficient List Concatenation in Loop

**Problem:** Using `result = result + [item]` in a loop creates a new list each iteration.

```python
# Slow - O(n²) time complexity
result = []
for item in data_list:
    result = result + [item * 2]  # Creates new list each time
```

**Solution:** Use list comprehension or `.append()` method.

```python
# Fast - O(n) time complexity
result = [item * 2 for item in data_list]
```

**Impact:** ~100x faster for large lists (5000+ items)

---

### 2. Nested Loops for Duplicate Detection

**Problem:** Using nested loops results in O(n²) time complexity.

```python
# Slow - O(n²)
for i in range(len(data_list)):
    for j in range(i + 1, len(data_list)):
        if data_list[i] == data_list[j]:
            duplicates.append(data_list[i])
```

**Solution:** Use `Counter` from collections for O(n) time complexity.

```python
# Fast - O(n)
from collections import Counter
counts = Counter(data_list)
duplicates = [item for item, count in counts.items() if count > 1]
```

**Impact:** ~1000x faster for lists with 1000+ items

---

### 3. Multiple Passes Over Data

**Problem:** Iterating over the same data multiple times.

```python
# Slow - Two separate loops
filtered_data = []
for item in data_list:
    if item > threshold:
        filtered_data.append(item)

transformed_data = []
for item in filtered_data:
    transformed_data.append(item ** 2)
```

**Solution:** Combine operations in a single pass.

```python
# Fast - Single pass with list comprehension
result = [item ** 2 for item in data_list if item > threshold]
```

**Impact:** ~2x faster, better memory efficiency

---

### 4. Redundant Calculations

**Problem:** Sorting the same data multiple times.

```python
# Slow - Sorts 3 times
sorted_nums = sorted(numbers)
median = sorted_nums[len(numbers) // 2]
sorted_nums_2 = sorted(numbers)  # Redundant!
minimum = sorted_nums_2[0]
sorted_nums_3 = sorted(numbers)  # Redundant!
maximum = sorted_nums_3[-1]
```

**Solution:** Sort once and reuse the result.

```python
# Fast - Sort once
sorted_nums = sorted(numbers)
median = sorted_nums[n // 2]
minimum = sorted_nums[0]
maximum = sorted_nums[-1]
```

**Impact:** ~3x faster

---

### 5. Repeated JSON Parsing

**Problem:** Parsing the same JSON string multiple times.

```python
# Slow - Parses JSON 4 times
data = json.loads(json_string)
if 'users' in json.loads(json_string):
    result['user_count'] = len(json.loads(json_string)['users'])
```

**Solution:** Parse once and reuse the result.

```python
# Fast - Parse once
data = json.loads(json_string)
result = {
    'user_count': len(data.get('users', [])),
    'product_count': len(data.get('products', []))
}
```

**Impact:** ~4x faster

---

### 6. Linear Search Instead of Hash Lookup

**Problem:** Using list for lookups when set/dict would be O(1).

```python
# Slow - O(n) for each search
found_items = []
for item in data_list:
    if item == target:
        found_items.append(item)
```

**Solution:** Use set for O(1) lookup.

```python
# Fast - O(1) lookup
def search_in_set(data_set, target):
    return target in data_set
```

**Impact:** ~100x faster for large datasets

---

### 7. Unbounded Cache Memory Growth

**Problem:** Cache without size limits can consume all available memory.

```python
# Problem - Unbounded growth
class DataCache:
    def __init__(self):
        self.cache = {}  # No size limit!
    
    def set(self, key, value):
        self.cache[key] = value
```

**Solution:** Implement LRU eviction policy with size limits.

```python
# Solution - Bounded cache with LRU
class DataCacheOptimized:
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.cache = {}
        self.access_order = []
    
    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            oldest = self.access_order.pop(0)
            del self.cache[oldest]
        self.cache[key] = value
```

**Impact:** Prevents memory exhaustion in long-running applications

---

### 8. String Concatenation in Loop

**Problem:** String concatenation creates new string objects each iteration.

```python
# Slow - Creates new string each iteration
report = ""
for item in data_items:
    report = report + f"Item: {item['name']}\n"
```

**Solution:** Use list and join for O(n) instead of O(n²).

```python
# Fast - O(n) time complexity
lines = [f"Item: {item['name']}" for item in data_items]
report = '\n'.join(lines)
```

**Impact:** ~50x faster for 1000+ items

---

### 9. Missing Memoization for Recursive Functions

**Problem:** Recursive functions recalculate the same values repeatedly.

```python
# Slow - No memoization
def calculate_factorial(n):
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)
```

**Solution:** Use `@lru_cache` decorator for automatic memoization.

```python
# Fast - With memoization
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_factorial_memoized(n):
    if n <= 1:
        return 1
    return n * calculate_factorial_memoized(n - 1)
```

**Impact:** ~100x faster for repeated calculations

---

### 10. Loading Entire File into Memory

**Problem:** Reading large files entirely into memory at once.

```python
# Slow - Loads entire file into memory
with open(filename, 'r') as f:
    content = f.read()
    lines = content.split('\n')
    # Process all lines
```

**Solution:** Process file line by line (streaming).

```python
# Fast - Streaming with minimal memory
def process_large_file_streaming(filename):
    processed = []
    with open(filename, 'r') as f:
        for line in f:
            # Process one line at a time
            processed.append(line.strip().upper())
    return processed

# Even better - Use generator for lazy evaluation
def process_large_file_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().upper()
```

**Impact:** Can handle files 100x larger with same memory footprint

---

## Running the Benchmarks

To see the performance improvements in action:

```bash
python benchmark.py
```

This will run comprehensive benchmarks comparing the original and optimized implementations.

## Expected Results

Based on testing, you should see significant speedups:

- List Processing: ~100x faster
- Duplicate Detection: ~1000x faster  
- Filter & Transform: ~2x faster
- Statistics: ~3x faster
- JSON Processing: ~4x faster
- Report Generation: ~50x faster
- Factorial (with caching): ~100x faster

## Key Takeaways

1. **Choose the right data structure** - Sets/dicts for lookups, lists for ordered data
2. **Avoid nested loops** - Look for O(n) algorithms instead of O(n²)
3. **Minimize passes over data** - Combine operations when possible
4. **Cache expensive operations** - Use memoization for recursive functions
5. **Stream large data** - Don't load everything into memory at once
6. **Use built-in functions** - Python's built-ins are optimized in C
7. **Profile before optimizing** - Measure to find real bottlenecks
8. **Consider memory vs speed tradeoffs** - Sometimes caching trades memory for speed

## Best Practices

- Use list comprehensions instead of loops for transformations
- Use `collections` module (Counter, defaultdict, deque) appropriately
- Leverage `functools` for caching and function optimization
- Profile code with `cProfile` to find actual bottlenecks
- Write benchmarks to measure improvements objectively
- Consider algorithmic complexity (Big O notation) when designing solutions
