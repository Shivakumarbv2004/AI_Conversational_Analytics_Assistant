from app.services.analytics_service import AnalyticsService


class BranchAnalytics(AnalyticsService):

    def sales_by_branch(self):

        return (
            self.df
            .groupby("branch")["sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def sales_by_city(self):

        return (
            self.df
            .groupby("city")["sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def best_branch(self):

        return self.sales_by_branch().iloc[0]

    def best_city(self):

        return self.sales_by_city().iloc[0]

    def branch_transactions(self):

        return (
            self.df
            .groupby("branch")
            .size()
            .reset_index(name="transactions")
        )