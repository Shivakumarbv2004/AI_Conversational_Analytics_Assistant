import pandas as pd
from pathlib import Path

class DataLoader:
    """
    Singleton Data Loader for the Supermarket Sales Dataset.
    Loads the CSV once and reuses it throughout the application.
    """

    _instance = None
    _data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance

    def load_data(self, file_path: str):

        if self._data is None:

            path = Path(file_path)

            if not path.exists():
                raise FileNotFoundError(
                    f"Dataset not found: {file_path}"
                )

            df = pd.read_csv(path)

            self._data = self.preprocess(df)

        return self._data

    def preprocess(self, df: pd.DataFrame):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("%", "percent")
            .str.replace("/", "_")
        )

        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

        numeric_columns = [
            "unit_price",
            "quantity",
            "tax_5percent",
            "sales",
            "cogs",
            "gross_margin_percentage",
            "gross_income",
            "rating"
        ]

        for col in numeric_columns:

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

        df.fillna(0, inplace=True)

        return df

    def get_dataframe(self):

        if self._data is None:
            raise Exception("Dataset not loaded.")

        return self._data