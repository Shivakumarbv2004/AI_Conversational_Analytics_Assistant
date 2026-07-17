from app.services.data_loader import DataLoader
from app.config import DATASET_PATH

class AnalyticsService:
    """
    Base Analytics Service.
    Loads the dataset once and shares it across all analytics modules.
    """

    def __init__(self):
        loader = DataLoader()
        self.df = loader.load_data(DATASET_PATH)