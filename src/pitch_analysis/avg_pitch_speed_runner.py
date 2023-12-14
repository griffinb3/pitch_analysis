from avg_pitch_speed import PitchAnalysis



# get our file
# blob = bucket.blob(blob_name='2021_mlb_pitch_file_2.xlsx').download_as_string()
# with open('local_dataset.xlsx', 'wb') as f:
# f.write(blob)


def display_results(pitch_type, analysis):
    team_speed_list = analysis.avg_pitch_speed(pitch_type)

    # team_speed_list.to_csv('velo_results.csv', index=False)

    print(f"\nAverage Speed for {pitch_type} by Team (descending order):")
    for team, speed in team_speed_list.items():
        print(f"{team}: {speed:.2f} mph")


top_pitches_data = ()

def display_top_pitches(attribute1, attribute2, pitch_type, analysis):
    top_pitches_data = analysis.top_pitches(attribute1, attribute2, pitch_type)


    if top_pitches_data is not None:
        print(f"\nPitches with the highest sum of standard deviations above the mean:")
        print(top_pitches_data)

    return top_pitches_data


if __name__ == "__main__":
    FILE_PATH = r'../../../../../../2021_mlb_pitch_speed_2.xlsx'
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

top_pitches_data.to_csv('stan_dev_results.csv', index=False)