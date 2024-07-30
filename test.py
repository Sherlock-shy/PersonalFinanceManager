import csv
import unittest
from unittest.mock import mock_open, patch
from financeManager import lloydsFin

class TestLloydsFin(unittest.TestCase):
    def setUp(self):
        self.transactions = []
        self.total = 0.0

    def test_lloydsFin(self):
        test_cases = [
            {
                "name": "Test Case 1",
                "input": ("test.csv", "January"),
                "expected_output": ([('01/01/2022', 'NX BUS CONTACTLESS', 'transport', 2.5)], 2.5),
                "mock_file_content": 'Transaction Date,Transaction Description,Debit Amount\n01/01/2022,NX BUS CONTACTLESS,2.5\n'
            },
            {
                "name": "Test Case 2",
                "input": ("test.csv", "February"),
                "expected_output": ([('02/01/2022', 'http://taobao.com', 'shopping', 50.0)], 50.0),
                "mock_file_content": 'Transaction Date,Transaction Description,Debit Amount\n02/01/2022,http://taobao.com,50.0\n'
            },
            {
                "name": "Test Case 3",
                "input": ("test.csv", "March"),
                "expected_output": ([('03/01/2022', 'UBER EATS', 'food', 15.0)], 15.0),
                "mock_file_content": 'Transaction Date,Transaction Description,Debit Amount\n03/01/2022,UBER EATS,15.0\n'
            },
            {
                "name": "Test Case 4",
                "input": ("test.csv", "April"),
                "expected_output": ([('04/01/2022', 'BT INTERNET', 'internet bills', 30.0)], 30.0),
                "mock_file_content": 'Transaction Date,Transaction Description,Debit Amount\n04/01/2022,BT INTERNET,30.0\n'
            },
            {
                "name": "Test Case 5",
                "input": ("test.csv", "May"),
                "expected_output": ([('05/01/2022', 'OTHER', 'other', 10.0)], 10.0),
                "mock_file_content": 'Transaction Date,Transaction Description,Debit Amount\n05/01/2022,OTHER,10.0\n'
            },
        ]

        for test in test_cases:
            with self.subTest(test['name']):
                with patch('builtins.open', mock_open(read_data=test['mock_file_content'])) as mock_file:
                    result = lloydsFin(*test['input'])
                    self.assertEqual(result, test['expected_output'])
                    mock_file.assert_called_once_with(test['input'][0], mode='r')

if __name__ == '__main__':
    unittest.main()
