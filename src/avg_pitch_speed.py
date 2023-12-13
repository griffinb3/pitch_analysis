# Load the data from the Excel file
from abc import abstractmethod
from google.cloud import storage
import pandas as pd

df = pd.read_excel(r"C:\Users\griffyb3\cs128\2021_mlb_pitch_file.xlsx")

# creates an empty list that is to be filled with team names
team_list = []


# Group data by team and pitch type, calculate average pitch velocity and spin rate
def group_by_teams():
    for name in df['team_name'].unique():
        if name not in team_list:
            team_list.append(name)
    return team_list


class AveragePitchSpeed:

    @staticmethod
    def avg_pitch_speed(pitch_type):
        pitch_list = []
        for name in team_list:
            pitch_list.append(
                df[(df['team_name'] == name) & (df['pitch_type_name'] == pitch_type)]['avg_speed'].mean())

        team_speed_dict = dict(sorted(zip(team_list, pitch_list), key=lambda x: x[1], reverse=True))
        return team_speed_dict

    """"@staticmethod
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
        return team_speed_sld"""

class PitchSpeedDifference:
# want to find the difference in speeds between fastball and changeup
# as well as fastball and curveball + fastball and slider

    @staticmethod
    def compare_fb_ch:
        # adding comments to commit and push
        # want to find the differnece between the fastball velo and changeup velo
        # need to pull the changeup and fastball values for each team out of their values






