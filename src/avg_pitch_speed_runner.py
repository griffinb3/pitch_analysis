from src.avg_pitch_speed import PitchAnalysis


def display_results(pitch_type, analysis):
    team_speed_dict = analysis.avg_pitch_speed(pitch_type)

    print(f"\nAverage Speed for {pitch_type} by Team (descending order):")
    for team, speed in team_speed_dict.items():
        print(f"{team}: {speed:.2f} mph")


def display_top_pitches(attribute1, attribute2, pitch_type, analysis):
    top_pitches_data = analysis.top_pitches(attribute1, attribute2, pitch_type)

    if top_pitches_data is not None:
        print(f"\nPitches with the highest sum of standard deviations above the mean:")
        print(top_pitches_data)


if __name__ == "__main__":
    FILE_PATH = r'C:\Users\griffyb3\cs128\2021_mlb_pitch_file_2.xlsx'
    analysis = PitchAnalysis(FILE_PATH)

    # User input for the desired pitch type
    pitch_input = input("Enter the pitch type (4-Seamer, Cutter, Sinker, Slider, Curveball, Changeup): ")

    # Validate user input
    valid_pitch_types = ['4-Seamer', 'Cutter', 'Sinker', 'Slider', 'Curveball', 'Changeup']
    if pitch_input not in valid_pitch_types:
        print("Invalid pitch type. Please enter a valid pitch type.")
    else:
        display_results(pitch_input, analysis)

    attribute_input1 = input("Enter the first attribute (avg_speed, Spin Rate): ")
    attribute_input2 = input("Enter the second attribute (avg_speed, Spin Rate):  ")

    # Calculate sum of standard deviations above the mean and display top players
    display_top_pitches(attribute_input1, attribute_input2, pitch_input, analysis)
