from app.services.analytics_service import AnalyticsService


class CustomerAnalytics(AnalyticsService):

    def customer_type(self):

        return (
            self.df
            .groupby("customer_type")
            .size()
            .reset_index(name="count")
        )

    def gender_distribution(self):

        return (
            self.df
            .groupby("gender")
            .size()
            .reset_index(name="count")
        )

    def sales_by_gender(self):

        return (
            self.df
            .groupby("gender")["sales"]
            .sum()
            .reset_index()
        )

    def member_vs_normal(self):

        return (
            self.df
            .groupby("customer_type")["sales"]
            .sum()
            .reset_index()
        )

    def average_rating(self):

        return round(
            self.df["rating"].mean(),
            2
        )