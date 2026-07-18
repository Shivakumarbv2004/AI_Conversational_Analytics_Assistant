import pandas as pd
import numpy as np
import random
import os

def generate_saas_dataset(num_records=5000):
    np.random.seed(42)
    random.seed(42)

    data = {
        "Customer ID": [f"CUST-{str(i).zfill(5)}" for i in range(1, num_records + 1)],
        "Company Size": np.random.choice(["Startup", "SMB", "Mid-Market", "Enterprise"], num_records, p=[0.4, 0.35, 0.15, 0.1]),
        "Industry": np.random.choice(["Healthcare", "Finance", "E-commerce", "Education", "Real Estate", "Technology"], num_records),
        "Subscription Tier": np.random.choice(["Basic", "Pro", "Enterprise"], num_records, p=[0.5, 0.35, 0.15]),
        "Acquisition Channel": np.random.choice(["Organic Search", "Paid Ads", "Referral", "LinkedIn", "Direct Sales"], num_records),
    }

    df = pd.DataFrame(data)

    # Assign MRR based on tier
    tier_mrr = {"Basic": 49.0, "Pro": 199.0, "Enterprise": 999.0}
    df["MRR"] = df["Subscription Tier"].map(tier_mrr) * np.random.uniform(0.9, 1.2, num_records)
    df["MRR"] = df["MRR"].round(2)

    # Assign CAC (Enterprise costs more to acquire)
    df["CAC"] = df["MRR"] * np.random.uniform(2.0, 5.0, num_records)
    df["CAC"] = df["CAC"].round(2)

    # Tenure (Months)
    df["Tenure Months"] = np.random.randint(1, 60, num_records)

    # Support Tickets
    df["Support Tickets"] = np.random.poisson(lam=df["Tenure Months"] / 10, size=num_records)

    # Churn Risk (Probability)
    # Startups, Basic Tier, and High Support Tickets increase churn risk
    churn_prob = np.zeros(num_records)
    churn_prob += np.where(df["Company Size"] == "Startup", 0.15, 0.05)
    churn_prob += np.where(df["Subscription Tier"] == "Basic", 0.1, 0.02)
    churn_prob += df["Support Tickets"] * 0.02
    churn_prob = np.clip(churn_prob, 0, 0.95)

    # Convert probability to actual Churn (1 = Churned, 0 = Active)
    df["Churned"] = np.random.binomial(1, churn_prob)

    # Save to CSV
    output_path = os.path.join(os.path.dirname(__file__), "data", "saas_subscriptions.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {num_records} records at {output_path}")

if __name__ == "__main__":
    generate_saas_dataset()
