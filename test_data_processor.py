"""
Unit tests for data processing modules.
Tests verify that optimized versions produce the same results as original.
"""
import unittest
import json
from data_processor import (
    process_data_inefficiently,
    find_duplicates_slow,
    filter_and_transform_data,
    compute_statistics,
    process_json_data,
    generate_report,
    calculate_factorial_recursive,
)
from data_processor_optimized import (
    process_data_efficiently,
    find_duplicates_fast,
    filter_and_transform_data_efficient,
    compute_statistics_optimized,
    process_json_data_efficient,
    generate_report_efficient,
    calculate_factorial_memoized,
)


class TestDataProcessing(unittest.TestCase):
    """Test that optimized functions produce same results as originals."""
    
    def test_process_data(self):
        """Test list processing produces same results."""
        data = list(range(100))
        result_slow = process_data_inefficiently(data)
        result_fast = process_data_efficiently(data)
        self.assertEqual(result_slow, result_fast)
    
    def test_find_duplicates(self):
        """Test duplicate detection produces same results."""
        data = [1, 2, 3, 2, 4, 3, 5, 1]
        result_slow = set(find_duplicates_slow(data))
        result_fast = set(find_duplicates_fast(data))
        self.assertEqual(result_slow, result_fast)
    
    def test_filter_and_transform(self):
        """Test filter and transform produces same results."""
        data = list(range(50))
        threshold = 25
        result_slow = filter_and_transform_data(data, threshold)
        result_fast = filter_and_transform_data_efficient(data, threshold)
        self.assertEqual(result_slow, result_fast)
    
    def test_compute_statistics(self):
        """Test statistics computation produces same results."""
        numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        result_slow = compute_statistics(numbers)
        result_fast = compute_statistics_optimized(numbers)
        self.assertEqual(result_slow, result_fast)
    
    def test_process_json(self):
        """Test JSON processing produces same results."""
        json_data = json.dumps({
            'users': [{'id': i} for i in range(10)],
            'products': [{'id': i} for i in range(20)]
        })
        result_slow = process_json_data(json_data)
        result_fast = process_json_data_efficient(json_data)
        self.assertEqual(result_slow, result_fast)
    
    def test_generate_report(self):
        """Test report generation produces same results."""
        data = [{'name': f'Item{i}', 'value': i} for i in range(10)]
        result_slow = generate_report(data)
        result_fast = generate_report_efficient(data)
        self.assertEqual(result_slow.strip(), result_fast.strip())
    
    def test_factorial(self):
        """Test factorial calculation produces same results."""
        for n in range(1, 10):
            result_slow = calculate_factorial_recursive(n)
            calculate_factorial_memoized.cache_clear()
            result_fast = calculate_factorial_memoized(n)
            self.assertEqual(result_slow, result_fast)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for both implementations."""
    
    def test_empty_list(self):
        """Test handling of empty lists."""
        result = process_data_efficiently([])
        self.assertEqual(result, [])
    
    def test_single_item(self):
        """Test handling of single item lists."""
        result = process_data_efficiently([5])
        self.assertEqual(result, [10])
    
    def test_no_duplicates(self):
        """Test duplicate detection with no duplicates."""
        data = [1, 2, 3, 4, 5]
        result = find_duplicates_fast(data)
        self.assertEqual(result, [])
    
    def test_all_duplicates(self):
        """Test duplicate detection with all duplicates."""
        data = [1, 1, 1, 1]
        result = find_duplicates_fast(data)
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()
