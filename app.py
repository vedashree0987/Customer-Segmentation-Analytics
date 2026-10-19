import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# --------------------------------------------------
# 1. Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide"
)

APP_DIR = Path(__file__).resolve().parent
DATA_PATH = APP_DIR / "marketing_campaign.xlsx"

FEATURES = [
    "Income",
    "Recency",
    "Total_Spend",
    "Total_Purchases",
    "NumDealsPurchases",
    "NumWebVisitsMonth",
    "Total_Children",
    "Total_Campaign_Accepted",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",
    "Customer_Tenure_Days"
]


# --------------------------------------------------
# 2. Load data and train the model
# --------------------------------------------------
@st.cache_resource
def train_model():
    data = pd.read_excel(DATA_PATH)
    df = data.copy()

    # Handle missing Income values
    df["Income"] = df["Income"].fillna(
        df["Income"].median()
    )

    # Feature engineering: total spending
    df["Total_Spend"] = (
        df["MntWines"]
        + df["MntFruits"]
        + df["MntMeatProducts"]
        + df["MntFishProducts"]
        + df["MntSweetProducts"]
        + df["MntGoldProds"]
    )

    # Total purchases
    df["Total_Purchases"] = (
        df["NumWebPurchases"]
        + df["NumCatalogPurchases"]
        + df["NumStorePurchases"]
    )

    # Total children
    df["Total_Children"] = (
        df["Kidhome"] + df["Teenhome"]
    )

    # Accepted marketing campaigns
    df["Total_Campaign_Accepted"] = (
        df["AcceptedCmp1"]
        + df["AcceptedCmp2"]
        + df["AcceptedCmp3"]
        + df["AcceptedCmp4"]
        + df["AcceptedCmp5"]
    )

    # Customer tenure
    df["Dt_Customer"] = pd.to_datetime(
        df["Dt_Customer"],
        errors="coerce"
    )

    reference_date = df["Dt_Customer"].max()

    df["Customer_Tenure_Days"] = (
        reference_date - df["Dt_Customer"]
    ).dt.days

    # Select model features
    X = df[FEATURES].replace(
        [np.inf, -np.inf], np.nan
    ).dropna()

    if len(X) < 5:
        raise ValueError(
            "At least five complete customer records "
            "are required to train five clusters."
        )

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train K-Means
    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    # Generate cluster profiles
    profiles = X.copy()
    profiles["KMeans_Cluster"] = labels

    profile_features = [
        "Income",
        "Recency",
        "Total_Spend",
        "Total_Purchases",
        "NumDealsPurchases",
        "NumWebVisitsMonth",
        "Total_Children",
        "Total_Campaign_Accepted",
        "Customer_Tenure_Days"
    ]

    cluster_profiles = (
        profiles.groupby("KMeans_Cluster")[profile_features]
        .mean()
        .round(2)
    )

    return scaler, model, cluster_profiles, len(X)


# --------------------------------------------------
# 3. Dashboard
# --------------------------------------------------
st.title("📊 Customer Segmentation Dashboard")

st.write(
    "Enter customer purchasing and engagement details "
    "to predict a customer segment using K-Means clustering."
)

st.info(
    "The model and scaler are trained directly from "
    "the Excel dataset. No saved model files are loaded."
)

if not DATA_PATH.exists():
    st.error(
        "marketing_campaign.xlsx was not found. "
        "Place it in the same folder as app.py."
    )
    st.stop()

try:
    with st.spinner("Training customer segmentation model..."):
        scaler, model, cluster_profiles, training_rows = train_model()
except Exception as e:
    st.error(f"Could not prepare the model: {e}")
    st.stop()

st.success(
    f"Model ready: 5 clusters trained using "
    f"{training_rows:,} customer records."
)


# --------------------------------------------------
# 4. Customer input form
# --------------------------------------------------
st.divider()
st.subheader("Customer Information")

with st.form("customer_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        income = st.number_input(
            "Income",
            min_value=0.0,
            value=50000.0,
            step=1000.0
        )

        recency = st.number_input(
            "Recency (days since last purchase)",
            min_value=0,
            value=30,
            step=1
        )

        total_spend = st.number_input(
            "Total Spend",
            min_value=0.0,
            value=500.0,
            step=50.0
        )

        total_purchases = st.number_input(
            "Total Purchases",
            min_value=0,
            value=15,
            step=1
        )

    with col2:
        deals = st.number_input(
            "Discount Purchases",
            min_value=0,
            value=3,
            step=1
        )

        web_visits = st.number_input(
            "Website Visits This Month",
            min_value=0,
            value=5,
            step=1
        )

        children = st.number_input(
            "Total Children",
            min_value=0,
            value=1,
            step=1
        )

        campaign_accepted = st.number_input(
            "Total Campaigns Accepted",
            min_value=0,
            max_value=5,
            value=1,
            step=1
        )

    with col3:
        web_purchases = st.number_input(
            "Web Purchases",
            min_value=0,
            value=5,
            step=1
        )

        catalog_purchases = st.number_input(
            "Catalog Purchases",
            min_value=0,
            value=3,
            step=1
        )

        store_purchases = st.number_input(
            "Store Purchases",
            min_value=0,
            value=7,
            step=1
        )

        tenure_days = st.number_input(
            "Customer Tenure (days)",
            min_value=0,
            value=365,
            step=30
        )

    submitted = st.form_submit_button(
        "Predict Customer Segment",
        type="primary"
    )


# --------------------------------------------------
# 5. Predict customer segment
# --------------------------------------------------
if submitted:

    input_values = {
        "Income": income,
        "Recency": recency,
        "Total_Spend": total_spend,
        "Total_Purchases": total_purchases,
        "NumDealsPurchases": deals,
        "NumWebVisitsMonth": web_visits,
        "Total_Children": children,
        "Total_Campaign_Accepted": campaign_accepted,
        "NumWebPurchases": web_purchases,
        "NumCatalogPurchases": catalog_purchases,
        "NumStorePurchases": store_purchases,
        "Customer_Tenure_Days": tenure_days
    }

    input_df = pd.DataFrame(
        [[input_values[feature] for feature in FEATURES]],
        columns=FEATURES
    )

    if not np.isfinite(
        input_df.to_numpy(dtype=float)
    ).all():
        st.error("Please enter valid numeric values.")
        st.stop()

    # Apply the fitted scaler
    scaled_input = scaler.transform(input_df)

    # Predict cluster
    predicted_cluster = int(
        model.predict(scaled_input)[0]
    )

    st.divider()
    st.subheader("Prediction Result")

    st.metric(
        label="Predicted K-Means Cluster",
        value=f"Cluster {predicted_cluster}"
    )

    st.success(
        f"This customer has been assigned to "
        f"Cluster {predicted_cluster}."
    )

    # Display customer inputs
    st.subheader("Customer Input Summary")
    st.dataframe(
        input_df,
        use_container_width=True
    )

    # Display cluster profile
    st.subheader("Average Characteristics of This Cluster")

    if predicted_cluster in cluster_profiles.index:
        st.dataframe(
            cluster_profiles.loc[
                predicted_cluster
            ].to_frame(name="Cluster Average"),
            use_container_width=True
        )
    else:
        st.warning(
            "The cluster profile could not be found."
        )

    st.caption(
        "Cluster numbers are labels, not rankings. "
        "Use the cluster averages to interpret customer behaviour."
    )