import pandas as pd
from dataprep_for_king_county import *
import json


def run_prep(path:str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = drop_bedroom_outlier(df)
    df = replace_basement_questionmark(df)
    df = recalculate_basement(df)
    df = fill_nan_with_zero(df)
    df = create_last_change(df)
    df = create_distance_to_citycenter(df)
    df = create_distance_to_waterfront(df)
    df = drop_needless_columns(df)
    return df


def get_sample(df:pd.DataFrame, n:int) -> dict:
    seed = 18
    sample_dict = df.sample(n, random_state=seed).to_dict('index')
    return sample_dict


def print_sample_json(house_list):
    list_5features = ['id', 'bedrooms', 'sqft_living', 'center_distance', 'price']
    for house in sample.values():
        house = {key: house[key] for key in list_5features}
        house = json.dumps(house)
        print(house)

def print_curl_post(house_list):
    list_5features = ['id', 'bedrooms', 'sqft_living', 'center_distance', 'price']
    for house in sample.values():
        house = {key: house[key] for key in list_5features}
        house = json.dumps(house)
        print(f"curl -X POST http://localhost:8100/houses -H \"Content-Type: application/json\" -d '{house}'")

if __name__ == "__main__":
    df = run_prep("./data/King_County_House_prices_dataset.csv")
    sample = get_sample(df,4)
    print_sample_json(sample)
    print_curl_post(sample)