# Load the data from the Excel file
from abc import abstractmethod
from google.cloud import storage
import pandas as pd


class PitchAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)  # Read data from Excel file
        self.team_list = self.group_by_teams()

    def group_by_teams(self):
        teams = self.df['team_name'].unique()
        return list(teams)

    def avg_pitch_speed(self, pitch_type):
        pitch_list = []
        # For each team in the league, calculate average speed for the pitch given
        for name in self.team_list:
            pitch_list.append(
                self.df[(self.df['team_name'] == name) & (self.df['pitch_type_name'] == pitch_type)]['avg_speed'].mean())

        team_speed_dict = dict(sorted(zip(self.team_list, pitch_list), key=lambda x: x[1], reverse=True))
        return team_speed_dict

    def top_pitches(self, attribute1, attribute2, pitch_type):
        for attribute in [attribute1, attribute2]:
            if attribute not in self.df.columns:
                print(f"Invalid attribute: {attribute}. Please enter a valid attribute.")
                return

        # Calculate Mean and Standard Deviation for each attribute
        mean_value1 = self.df[attribute1].mean()
        std_dev1 = self.df[attribute1].std()
        mean_value2 = self.df[attribute2].mean()
        std_dev2 = self.df[attribute2].std()

        # Filter pitches by pitch given previously
        pitch_df = self.df[self.df['pitch_type_name'] == pitch_type].copy()

        # Calculate standard deviations above the mean for each pitch
        pitch_df['StdDevs1'] = (pitch_df[attribute1] - mean_value1) / std_dev1
        pitch_df['StdDevs2'] = (pitch_df[attribute2] - mean_value2) / std_dev2

        # Sum of standard deviations above the mean for both attributes
        pitch_df['SumStdDevs'] = pitch_df['StdDevs1'] + pitch_df['StdDevs2']

        # Find players with the highest values
        top_players = pitch_df.nlargest(20, 'SumStdDevs')

        return top_players[[' first_name', 'last_name', attribute1, attribute2, 'SumStdDevs']]
