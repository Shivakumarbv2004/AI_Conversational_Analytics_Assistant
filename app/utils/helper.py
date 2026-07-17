import json
import pandas as pd


def dataframe_to_dict(data):

    if isinstance(data, pd.DataFrame):
        return data.to_dict(orient="records")

    if isinstance(data, pd.Series):
        return data.to_dict()

    return data


def pretty_json(data):

    return json.dumps(
        data,
        indent=4,
        default=str
    )