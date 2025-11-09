"""
Benchmark script to compare performance of original vs optimized code.
"""
import time
import json
from statistics import mean, stdev

# Import both versions
import data_processor as slow
import data_processor_optimized as fast


def benchmark_function(func, *args, runs=10):
    """Run a function multiple times and return statistics."""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)
    
    return {
        'mean': mean(times),
        'stdev': stdev(times) if len(times) > 1 else 0,
        'min': min(times),
        'max': max(times)
    }


def print_comparison(name, slow_stats, fast_stats):
    """Print comparison of benchmark results."""
    speedup = slow_stats['mean'] / fast_stats['mean']
    print(f"\n{name}:")
    print(f"  Original: {slow_stats['mean']*1000:.3f}ms ± {slow_stats['stdev']*1000:.3f}ms")
    print(f"  Optimized: {fast_stats['mean']*1000:.3f}ms ± {fast_stats['stdev']*1000:.3f}ms")
    print(f"  Speedup: {speedup:.2f}x faster")


def main():
    """Run all benchmarks."""
    print("=" * 60)
    print("Performance Benchmark: Original vs Optimized")
    print("=" * 60)
    
    # Benchmark 1: List processing
    data = list(range(5000))
    slow_stats = benchmark_function(slow.process_data_inefficiently, data, runs=10)
    fast_stats = benchmark_function(fast.process_data_efficiently, data, runs=10)
    print_comparison("Test 1: List Processing (5000 items)", slow_stats, fast_stats)
    
    # Benchmark 2: Duplicate detection
    data_with_dupes = list(range(100)) * 10  # 1000 items with duplicates
    slow_stats = benchmark_function(slow.find_duplicates_slow, data_with_dupes, runs=10)
    fast_stats = benchmark_function(fast.find_duplicates_fast, data_with_dupes, runs=10)
    print_comparison("Test 2: Duplicate Detection (1000 items)", slow_stats, fast_stats)
    
    # Benchmark 3: Filter and transform
    data = list(range(10000))
    threshold = 5000
    slow_stats = benchmark_function(slow.filter_and_transform_data, data, threshold, runs=10)
    fast_stats = benchmark_function(fast.filter_and_transform_data_efficient, data, threshold, runs=10)
    print_comparison("Test 3: Filter & Transform (10000 items)", slow_stats, fast_stats)
    
    # Benchmark 4: Statistics computation
    numbers = list(range(1000))
    slow_stats = benchmark_function(slow.compute_statistics, numbers, runs=10)
    fast_stats = benchmark_function(fast.compute_statistics_optimized, numbers, runs=10)
    print_comparison("Test 4: Statistics Computation (1000 numbers)", slow_stats, fast_stats)
    
    # Benchmark 5: JSON processing
    json_data = json.dumps({
        'users': [{'id': i, 'name': f'User{i}'} for i in range(100)],
        'products': [{'id': i, 'name': f'Product{i}'} for i in range(200)]
    })
    slow_stats = benchmark_function(slow.process_json_data, json_data, runs=10)
    fast_stats = benchmark_function(fast.process_json_data_efficient, json_data, runs=10)
    print_comparison("Test 5: JSON Processing", slow_stats, fast_stats)
    
    # Benchmark 6: Report generation
    report_data = [{'name': f'Item{i}', 'value': i} for i in range(1000)]
    slow_stats = benchmark_function(slow.generate_report, report_data, runs=10)
    fast_stats = benchmark_function(fast.generate_report_efficient, report_data, runs=10)
    print_comparison("Test 6: Report Generation (1000 items)", slow_stats, fast_stats)
    
    # Benchmark 7: Factorial calculation (memoization benefit)
    print("\nTest 7: Factorial Calculation with Memoization")
    # Clear cache first
    fast.calculate_factorial_memoized.cache_clear()
    
    # First run - cache miss
    start = time.perf_counter()
    for i in range(10, 20):
        slow.calculate_factorial_recursive(i)
    slow_time = time.perf_counter() - start
    
    # Optimized version with memoization
    start = time.perf_counter()
    for i in range(10, 20):
        fast.calculate_factorial_memoized(i)
    fast_time_first = time.perf_counter() - start
    
    # Second run - cache hit
    start = time.perf_counter()
    for i in range(10, 20):
        fast.calculate_factorial_memoized(i)
    fast_time_cached = time.perf_counter() - start
    
    print(f"  Original (no cache): {slow_time*1000:.3f}ms")
    print(f"  Optimized (first run): {fast_time_first*1000:.3f}ms")
    print(f"  Optimized (cached): {fast_time_cached*1000:.3f}ms")
    print(f"  Speedup: {slow_time/fast_time_cached:.2f}x faster with cache")
    
    print("\n" + "=" * 60)
    print("Benchmark Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
