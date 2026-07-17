from app.analytics.sales import SalesAnalytics
from app.analytics.products import ProductAnalytics
from app.analytics.branches import BranchAnalytics
from app.analytics.customers import CustomerAnalytics
from app.analytics.payments import PaymentAnalytics


class DashboardAnalytics:

    def __init__(self):

        self.sales = SalesAnalytics()
        self.products = ProductAnalytics()
        self.branches = BranchAnalytics()
        self.customers = CustomerAnalytics()
        self.payments = PaymentAnalytics()

    def get_dashboard(self):

        return {

            "total_sales":
                self.sales.get_total_sales(),

            "transactions":
                self.sales.get_total_transactions(),

            "quantity":
                self.sales.get_total_quantity(),

            "average_sale":
                self.sales.get_average_sale(),

            "average_rating":
                self.customers.average_rating(),

            "best_product":
                self.products.best_product().to_dict(),

            "best_branch":
                self.branches.best_branch().to_dict(),

            "best_city":
                self.branches.best_city().to_dict(),

            "payment_method":
                self.payments.most_used_payment().to_dict()
        }