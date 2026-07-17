from app.analytics.sales import SalesAnalytics
from app.analytics.products import ProductAnalytics
from app.analytics.customers import CustomerAnalytics
from app.analytics.branches import BranchAnalytics
from app.analytics.payments import PaymentAnalytics
from app.analytics.trends import TrendAnalytics
from app.analytics.dashboard import DashboardAnalytics


class AnalyticsEngine:

    def __init__(self):

        self.sales = SalesAnalytics()
        self.products = ProductAnalytics()
        self.customers = CustomerAnalytics()
        self.branches = BranchAnalytics()
        self.payments = PaymentAnalytics()
        self.trends = TrendAnalytics()
        self.dashboard = DashboardAnalytics()

    def execute(self, tool):

        if tool == "total_sales":
            return self.sales.get_total_sales()

        elif tool == "average_sale":
            return self.sales.get_average_sale()

        elif tool == "transactions":
            return self.sales.get_total_transactions()

        elif tool == "quantity":
            return self.sales.get_total_quantity()

        elif tool == "top_products":
            return self.products.top_products()

        elif tool == "least_products":
            return self.products.least_products()

        elif tool == "sales_by_product":
            return self.products.sales_by_product()

        elif tool == "quantity_by_product":
            return self.products.quantity_by_product()

        elif tool == "customer_distribution":
            return self.customers.customer_type()

        elif tool == "gender_distribution":
            return self.customers.gender_distribution()

        elif tool == "sales_by_gender":
            return self.customers.sales_by_gender()

        elif tool == "member_vs_normal":
            return self.customers.member_vs_normal()

        elif tool == "payment_distribution":
            return self.payments.payment_distribution()

        elif tool == "sales_by_payment":
            return self.payments.sales_by_payment()

        elif tool == "sales_by_branch":
            return self.branches.sales_by_branch()

        elif tool == "sales_by_city":
            return self.branches.sales_by_city()

        elif tool == "monthly_trend":
            return self.trends.monthly_trend()

        elif tool == "weekday_trend":
            return self.trends.weekday_trend()

        elif tool == "hourly_trend":
            return self.trends.hourly_trend()

        elif tool == "dashboard":
            return self.dashboard.get_dashboard()

        else:
            raise ValueError(f"Unknown tool: {tool}")