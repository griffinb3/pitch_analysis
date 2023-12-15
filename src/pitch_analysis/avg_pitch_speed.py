# Load the data from the Excel file

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
                self.df[(self.df['team_name'] == name) & (self.df['pitch_type_name'] == pitch_type)][
                    'avg_speed'].mean())

        team_speed_dict = dict(sorted(zip(self.team_list, pitch_list), key=lambda x: x[1], reverse=True))
        return team_speed_dict

    # Load the data from the Excel file


# Group data by team and pitch type, calculate average pitch velocity and spin rate
# This was the initial code that I created. I asked ChatGPT to make it generic
"""def group_by_teams():
    for name in df['team_name'].unique():
        if name not in team_list:
            team_list.append(name)
    return team_list


class AveragePitchSpeed:
    @staticmethod
    def avg_fb_speed():
        # currently have the data sorted by team right now
        # want to find a way to get all the pitches that are fastballs from that team
        speed_df_fb = df['avg_speed']
        fb_list = []
        for name in team_list:
            if df['pitch_type_name'] == '4-seamer':
                fb_list.append(speed_df_fb)
        avg_fb_speed = sum(fb_list) / len(fb_list)
        team_speed_fb = {name: avg_fb_speed}
        return team_speed_fb

    @staticmethod
    def avg_ch_speed():
        speed_df_ch = df['avg_speed']
        ch_list = []
        for name in team_list:
            if df['pitch_type_name'] == 'Changeup':
                ch_list.append(speed_df_ch)
        avg_ch_speed = sum(ch_list) / len(ch_list)
        team_speed_ch = {name: avg_ch_speed}
        return team_speed_ch

    @staticmethod
    def avg_cb_speed():
        speed_df_cb = df['avg_speed']
        cb_list = []
        for name in team_list:
            if df['pitch_type_name'] == 'Curveball':
                cb_list.append(speed_df_cb)
        avg_cb_speed = sum(cb_list) / len(cb_list)
        team_speed_cb = {name: avg_cb_speed}
        return team_speed_cb

    @staticmethod
    def avg_cut_speed():
        speed_df_cut = df['avg_speed']
        cut_list = []
        for name in team_list:
            if df['pitch_type_name'] == 'Cutter':
                cut_list.append(speed_df_cut)
        avg_cut_speed = sum(cut_list) / len(cut_list)
        team_speed_cut = {name: avg_cut_speed}
        return team_speed_cut

    @staticmethod
    def avg_sink_speed():
        speed_df_sink = df['avg_speed']
        sink_list = []
        for name in team_list:
            if df['pitch_type_name'] == 'Sinker':
                sink_list.append(speed_df_sink)
        avg_sink_speed = sum(sink_list) / len(sink_list)
        team_speed_sink = {name: avg_sink_speed}
        return team_speed_sink

    @staticmethod
    def avg_sld_speed():
        speed_df_sld = df['avg_speed']
        sld_list = []
        for name in team_list:
            if df['pitch_type_name'] == 'Slider':
                sld_list.append(speed_df_sld)
        avg_sld_speed = sum(sld_list) / len(sld_list)
        team_speed_sld = {name: avg_sld_speed}
        return team_speed_sld 
        
"""



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