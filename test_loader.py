from app.services.data_loader import DataLoader
from app.config import DATASET_PATH

loader = DataLoader()

df = loader.load_data(DATASET_PATH)

print(df.head())

print(df.info())

print(df.describe())