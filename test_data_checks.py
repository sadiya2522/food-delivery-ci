import unittest
from data_checks import load_dataset, validate_dataset

class TestFoodDeliveryDataset(unittest.TestCase):

    def test_dataset_validation(self):
        self.assertTrue(validate_dataset())

    def test_dataset_not_empty(self):
        df = load_dataset()
        self.assertGreater(len(df), 0)

    def test_customer_type_exists(self):
        df = load_dataset()
        self.assertIn("Customer Type", df.columns)
        self.assertTrue(df["Customer Type"].notna().all())

if __name__ == "__main__":
    unittest.main()
