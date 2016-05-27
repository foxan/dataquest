import pandas as pd

def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ["submission_time", "upvotes", "url", "headline"]
    print("Data is loaded.")
    return df

if __name__ == "__main__":
    # This will call load_data if you run the script from the command line.
    hn = load_data()
    print(hn.head(3))