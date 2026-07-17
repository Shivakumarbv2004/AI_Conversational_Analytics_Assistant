from app.services.analytics_service import AnalyticsService


class ProductAnalytics(AnalyticsService):

    def sales_by_product(self):

        return (
            self.df
            .groupby("product_line")["sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def quantity_by_product(self):

        return (
            self.df
            .groupby("product_line")["quantity"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def average_rating(self):

        return (
            self.df
            .groupby("product_line")["rating"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

    def top_products(self, top_n=5):

        return self.sales_by_product().head(top_n)

    def least_products(self, top_n=5):

        return self.sales_by_product().tail(top_n)

    def best_product(self):

        return self.sales_by_product().iloc[0]

    def worst_product(self):

        return self.sales_by_product().iloc[-1]