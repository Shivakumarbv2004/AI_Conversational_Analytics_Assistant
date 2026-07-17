from app.services.analytics_service import AnalyticsService


class TrendAnalytics(AnalyticsService):

    def monthly_trend(self):

        monthly = (
            self.df
            .groupby(self.df["date"].dt.to_period("M"))["sales"]
            .sum()
            .reset_index()
        )

        monthly["date"] = monthly["date"].astype(str)

        return monthly

    def weekday_trend(self):

        df = self.df.copy()

        df["weekday"] = df["date"].dt.day_name()

        return (
            df
            .groupby("weekday")["sales"]
            .sum()
            .reset_index()
        )

    def hourly_trend(self):

        df = self.df.copy()

        df["hour"] = df["time"].str[:2]

        return (
            df
            .groupby("hour")["sales"]
            .sum()
            .reset_index()
        )