#!/usr/bin/env python3
"""
Quick demonstration of performance improvements.
Run this to see side-by-side comparisons of slow vs fast code.
"""
import time
import json
from data_processor import (
    process_data_inefficiently,
    find_duplicates_slow,
    filter_and_transform_data,
    process_json_data,
    generate_report,
)
from data_processor_optimized import (
    process_data_efficiently,
    find_duplicates_fast,
    filter_and_transform_data_efficient,
    process_json_data_efficient,
    generate_report_efficient,
)


def time_function(func, *args):
    """Time a function call and return duration in milliseconds."""
    start = time.perf_counter()
    result = func(*args)
    duration = (time.perf_counter() - start) * 1000
    return result, duration


def print_comparison(test_name, slow_time, fast_time):
    """Print a formatted comparison."""
    if fast_time > 0:
        speedup = slow_time / fast_time
        ratio = int(speedup)
    else:
        speedup = float('inf')
        ratio = bar_width
    
    bar_width = 50
    # Cap the ratio to prevent extremely long strings
    slow_bar = '█' * min(bar_width, ratio)
    fast_bar = '█' * bar_width
    
    print(f"\n{test_name}")
    print(f"  Original:  {slow_bar} {slow_time:.3f}ms")
    print(f"  Optimized: {fast_bar} {fast_time:.3f}ms")
    print(f"  → {speedup:.1f}x FASTER! 🚀")


def main():
    """Run visual demonstrations."""
    print("=" * 70)
    print(" " * 15 + "PERFORMANCE OPTIMIZATION DEMO")
    print("=" * 70)
    
    # Test 1: List processing
    print("\n📊 Test 1: Processing 5000 items")
    data = list(range(5000))
    _, slow_time = time_function(process_data_inefficiently, data)
    _, fast_time = time_function(process_data_efficiently, data)
    print_comparison("List Processing", slow_time, fast_time)
    
    # Test 2: Finding duplicates
    print("\n📊 Test 2: Finding duplicates in 1000 items")
    data = list(range(100)) * 10
    _, slow_time = time_function(find_duplicates_slow, data)
    _, fast_time = time_function(find_duplicates_fast, data)
    print_comparison("Duplicate Detection", slow_time, fast_time)
    
    # Test 3: Filter and transform
    print("\n📊 Test 3: Filter and transform 10000 items")
    data = list(range(10000))
    _, slow_time = time_function(filter_and_transform_data, data, 5000)
    _, fast_time = time_function(filter_and_transform_data_efficient, data, 5000)
    print_comparison("Filter & Transform", slow_time, fast_time)
    
    # Test 4: JSON processing
    print("\n📊 Test 4: Processing JSON data")
    json_data = json.dumps({
        'users': [{'id': i, 'name': f'User{i}'} for i in range(100)],
        'products': [{'id': i, 'name': f'Product{i}'} for i in range(200)]
    })
    _, slow_time = time_function(process_json_data, json_data)
    _, fast_time = time_function(process_json_data_efficient, json_data)
    print_comparison("JSON Processing", slow_time, fast_time)
    
    # Test 5: Report generation
    print("\n📊 Test 5: Generating report for 1000 items")
    data = [{'name': f'Item{i}', 'value': i} for i in range(1000)]
    _, slow_time = time_function(generate_report, data)
    _, fast_time = time_function(generate_report_efficient, data)
    print_comparison("Report Generation", slow_time, fast_time)
    
    print("\n" + "=" * 70)
    print(" " * 20 + "✨ OPTIMIZATION COMPLETE ✨")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  • Choose the right algorithm (O(n) vs O(n²))")
    print("  • Use appropriate data structures (set/dict vs list)")
    print("  • Minimize redundant calculations")
    print("  • Combine operations into single passes")
    print("  • Use Python's optimized built-in functions")
    print("\nRun 'python benchmark.py' for detailed statistics!")
    print()


if __name__ == "__main__":
    main()
