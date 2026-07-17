from fastapi import APIRouter
from fastapi import HTTPException

from app.analytics.dashboard import DashboardAnalytics
from app.analytics.sales import SalesAnalytics
from app.analytics.products import ProductAnalytics
from app.analytics.customers import CustomerAnalytics
from app.analytics.branches import BranchAnalytics
from app.analytics.payments import PaymentAnalytics
from app.analytics.trends import TrendAnalytics

from app.utils.helper import dataframe_to_dict

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

sales = SalesAnalytics()
products = ProductAnalytics()
customers = CustomerAnalytics()
branches = BranchAnalytics()
payments = PaymentAnalytics()
trends = TrendAnalytics()
dashboard = DashboardAnalytics()


@router.get("/dashboard")
def dashboard_data():

    return dashboard.get_dashboard()


@router.get("/sales")
def sales_data():

    return {

        "total_sales": sales.get_total_sales(),

        "average_sale": sales.get_average_sale(),

        "transactions": sales.get_total_transactions(),

        "monthly_sales":

        dataframe_to_dict(

            sales.monthly_sales()

        )

    }


@router.get("/products")
def product_data():

    return dataframe_to_dict(

        products.sales_by_product()

    )


@router.get("/customers")
def customer_data():

    return {

        "customer_distribution":

        dataframe_to_dict(

            customers.customer_type()

        ),

        "member_vs_normal":

        dataframe_to_dict(

            customers.member_vs_normal()

        )

    }


@router.get("/branches")
def branch_data():

    return {

        "sales_by_branch":

        dataframe_to_dict(

            branches.sales_by_branch()

        ),

        "sales_by_city":

        dataframe_to_dict(

            branches.sales_by_city()

        )

    }


@router.get("/payments")
def payment_data():

    return dataframe_to_dict(

        payments.sales_by_payment()

    )


@router.get("/trends")
def trend_data():

    return {

        "monthly":

        dataframe_to_dict(

            trends.monthly_trend()

        ),

        "weekday":

        dataframe_to_dict(

            trends.weekday_trend()

        ),

        "hourly":

        dataframe_to_dict(

            trends.hourly_trend()

        )

    }