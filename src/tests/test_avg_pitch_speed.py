import unittest
from src.pitch_analysis.avg_pitch_speed import *


class TestPitchAnalysis(unittest.TestCase):
    def setUp(self):
        # Create an instance of PitchAnalysis for testing
        self.analysis = PitchAnalysis(r'C:\Users\griffyb3\cs128\Test Data.xlsx')

    def test_group_by_teams(self):
        # Call the method being tested
        result = self.analysis.group_by_teams()

        # Assert the expected result
        self.assertCountEqual(result, ['Foresters', 'Blues', 'Saints'])

    def test_avg_pitch_speed(self):
        # Call the method being tested
        result = self.analysis.avg_pitch_speed('4-Seamer')

        # Assert the expected result
        expected_result = {'Blues': 100.0, 'Foresters': 90.0, 'Saints': 70.0}
        self.assertDictEqual(result, expected_result)

    def test_top_pitches(self):
        # Assuming you have a pitch_df containing the result of the method
        attribute1 = 'avg_speed'
        attribute2 = 'Spin Rate'
        pitch_type = '4-Seamer'
        pitch_df = self.analysis.top_pitches(attribute1, attribute2, pitch_type)

        # Test if the result is a DataFrame
        self.assertIsInstance(pitch_df, pd.DataFrame)

        # Test if the DataFrame has the expected columns
        expected_columns = [' first_name', 'last_name', attribute1, attribute2, 'SumStdDevs']
        for column in expected_columns:
            self.assertIn(column, pitch_df.columns)

        # For example, you can check if the number of rows is correct
        self.assertEqual(len(pitch_df), 3)

        # For example, you can check if the player names match the expected result
        self.assertEqual(pitch_df.iloc[0][' first_name'], 'Homie')
        self.assertEqual(pitch_df.iloc[0]['last_name'], 'Buelher')




if __name__ == '__main__':
    unittest.main()
