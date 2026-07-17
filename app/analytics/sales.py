from app.services.analytics_service import AnalyticsService


class SalesAnalytics(AnalyticsService):

    def get_total_sales(self):
        return round(self.df["sales"].sum(), 2)

    def get_average_sale(self):
        return round(self.df["sales"].mean(), 2)

    def get_total_transactions(self):
        return len(self.df)

    def get_total_quantity(self):
        return int(self.df["quantity"].sum())

    def get_max_sale(self):
        return round(self.df["sales"].max(), 2)

    def get_min_sale(self):
        return round(self.df["sales"].min(), 2)

    def monthly_sales(self):
        monthly = (
            self.df
            .groupby(self.df["date"].dt.to_period("M"))["sales"]
            .sum()
            .reset_index()
        )

        monthly["date"] = monthly["date"].astype(str)

        return monthly

    def daily_sales(self):
        daily = (
            self.df
            .groupby("date")["sales"]
            .sum()
            .reset_index()
        )

        return daily

    def top_sales_days(self, top_n=10):

        daily = (
            self.df.groupby("date")["sales"]
            .sum()
            .sort_values(ascending=False)
            .head(top_n)
            .reset_index()
        )

        return daily