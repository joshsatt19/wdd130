import pytest
from hotdog import get_todays_sales_total, append_sales_to_file, read_all_sales, calculate_stats

def test_calculate_stats():
    sales = [20, 50, 65]
    stats = calculate_stats(sales)
    assert stats == {"average": 45, "max": 65, "min": 20}

pytest.main()