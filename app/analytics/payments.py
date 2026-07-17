from app.services.analytics_service import AnalyticsService


class PaymentAnalytics(AnalyticsService):

    def payment_distribution(self):

        return (
            self.df
            .groupby("payment")
            .size()
            .reset_index(name="transactions")
        )

    def sales_by_payment(self):

        return (
            self.df
            .groupby("payment")["sales"]
            .sum()
            .reset_index()
        )

    def most_used_payment(self):

        return (
            self.payment_distribution()
            .sort_values("transactions", ascending=False)
            .iloc[0]
        )