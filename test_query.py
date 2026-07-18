import sys
from app.analytics.analytics_engine import AnalyticsEngine

engine = AnalyticsEngine()
plan = {
    "group_by": "Industry",
    "agg_column": "MRR",
    "agg_method": "mean"
}

try:
    res = engine.execute(plan)
    print("SUCCESS:")
    print(res)
except Exception as e:
    import traceback
    traceback.print_exc()
