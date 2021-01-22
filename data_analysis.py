import pandas as pd
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv(r"C:\Users\Kate\Documents\Folders\CSE 310\data_analysis\nmprior_2016.csv")
    df["state_name"] = df["state_name"].astype("str")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].astype("str")
    
    print("\nWhich question would you like answered [enter 'q' to quit]?")
    print("1) What state had the most fatal accidents involving non-motorists in 2016?")
    print("2) What circumstances most commonly involved non-motorists in a fatal accident in 2016?\n")

    while True:
        choice = input("Enter 1, 2, or q: ")
        if choice == "q":
            exit()
        elif choice == "1":
            show_accidents_by_state(df)
            print("NOTE: This data comes from the US Department of Transportation Traffic Fatality Records nmprior_2016 data set. Not all states will be represented.\n")
        elif choice == "2":
            show_accidents_by_non_motorist_circumstance(df)
            print("NOTE: This data comes from the US Department of Transportation Traffic Fatality Records nmprior_2016 data set. Not all states will be represented.\n")
        else:
            print("Invalid Entry")

# Counts the number of accidents by counting the number of instances of each state.
# There is one case number for each instance.
def count_accidents_by_state(df):

    accidents_by_state_df = df["state_name"].value_counts()
    return accidents_by_state_df

# Displays a bar graph of the number of accidents in each state.
def show_accidents_by_state(df):

    accidents_by_state_df = count_accidents_by_state(df)
    
    print(accidents_by_state_df)
    
    accidents_by_state_df.plot(kind="bar", x="state_name", legend=None)
    plt.title("Number of Fatal Non-motorist Accidents By State")
    plt.xlabel(None)
    plt.ylabel("Number of Fatal Non-motorist Accidents")
    plt.tight_layout()
    
    plt.show()

# Counts the number of accidents by counting the number of instances of each circumstance.
# There is one case number for each instance.
def count_accidents_by_non_motorist_circumstance(df):

    accidents_by_circumstance_df = df["non_motorist_action_circumstances_name"].value_counts()
    return accidents_by_circumstance_df

# Displays a bar graph of the number of accidents for each circumstance.
def show_accidents_by_non_motorist_circumstance(df):

    df = rename_non_motorist_action_circumstances_name_column(df)
    accidents_by_circumstance_df = count_accidents_by_non_motorist_circumstance(df)
    
    print(accidents_by_circumstance_df)
    
    accidents_by_circumstance_df.plot(kind="bar", x="non_motorist_action_circumstances_name", legend=None, color="darkorange")
    plt.title("Number of Fatal Non-motorist Accidents By Non-motorist Circumstance At Time Involved In Accident", wrap=True)
    plt.xlabel("Non-motorist Circumstance At Time Involved In Accident")
    plt.ylabel("Number of Fatal Non-motorist Accidents")
    plt.tight_layout()
    
    plt.show()

# Some names were too long to fit on the graph.
def rename_non_motorist_action_circumstances_name_column(df):

    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Going to or from School (K-12)"], "To/From School")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Waiting to Cross Roadway"], "Waiting to Cross Road")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Crossing Roadway"], "Crossing Road")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Movement Along Roadway with Traffic (In or Adjacent to Travel Lane)"], "Moving With Traffic")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Crossing Roadway"], "Crossing Road")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["In Roadway-Other (Working, Playing, etc.)"], "In Road")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Adjacent to Roadway (e.g., Shoulder, Median)"], "Adjacent to Road")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Working in Trafficway (Incident Response)"], "Working in Traffic")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Entering/Exiting a Parked or Stopped Vehicle"], "In/Out of Stopped Car")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Disabled Vehicle Related (Working on, Pushing, Leaving/Approaching)"], "With Disabled Car")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Movement Along Roadway Against Traffic (In or Adjacent to Travel Lane)"], "Moving Against Traffic")
    df["non_motorist_action_circumstances_name"] = df["non_motorist_action_circumstances_name"].replace(
        ["Movement Along Roadway – Direction Unknown (Since 2012)"], "Along Road")
    return df

if __name__ == "__main__":
    main()