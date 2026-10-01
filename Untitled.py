from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Netflix Customer Insights", page_icon="N", layout="wide")

st.markdown(
	"""
	<style>
		.stApp { background: #101010; color: #f5f5f1; }
		[data-testid="stHeader"] { background: rgba(16, 16, 16, 0.96); }
		[data-testid="stAppViewContainer"] { background: #101010; }
		h1, h2, h3, p, label { color: #f5f5f1 !important; }
		h1 { border-left: 7px solid #e50914; padding-left: 16px; }
		[data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
			gap: 1.5rem;
		}
	</style>
	""",
	unsafe_allow_html=True,
)

data_path = Path(__file__).with_name("Netflix_100_Customers_Dataset.csv")
netflix = pd.read_csv(data_path)
netflix["Rating"] = pd.to_numeric(netflix["Rating"], errors="coerce")
netflix["Monthly_Revenue"] = pd.to_numeric(netflix["Monthly_Revenue"], errors="coerce")

st.title("Netflix Customer Insights")

plt.rcParams.update(
	{
		"figure.facecolor": "#181818",
		"axes.facecolor": "#181818",
		"axes.edgecolor": "#555555",
		"axes.labelcolor": "#f5f5f1",
		"text.color": "#f5f5f1",
		"xtick.color": "#f5f5f1",
		"ytick.color": "#f5f5f1",
		"font.family": "sans-serif",
	}
)

left, right = st.columns(2)

with left:
	revenue_by_region = netflix.groupby("Region")["Monthly_Revenue"].sum().sort_values(ascending=False)
	figure, axis = plt.subplots(figsize=(7, 4.5))
	revenue_by_region.plot(kind="bar", ax=axis, color="#e50914", width=0.68)
	axis.set_title("Region-wise Revenue", loc="left", color="#f5f5f1", pad=16, fontsize=15)
	axis.set_xlabel("")
	axis.set_ylabel("Monthly revenue")
	axis.spines[["top", "right"]].set_visible(False)
	axis.grid(axis="y", color="#444444", linewidth=0.6, alpha=0.55)
	axis.set_axisbelow(True)
	plt.xticks(rotation=0)
	figure.tight_layout()
	st.pyplot(figure, use_container_width=True)
	plt.close(figure)

with right:
	rating_by_plan = netflix.groupby("Subscription_Plan")["Rating"].sum().sort_values(ascending=False)
	figure, axis = plt.subplots(figsize=(7, 4.5))
	rating_by_plan.plot(
		kind="pie",
		ax=axis,
		colors=["#e50914", "#f5f5f1", "#777777"],
		autopct="%1.0f%%",
		startangle=90,
		wedgeprops={"edgecolor": "#181818", "linewidth": 2},
		textprops={"color": "#f5f5f1", "fontsize": 10},
	)
	axis.set_title("Subscription Plan-wise Rating", loc="left", color="#f5f5f1", pad=16, fontsize=15)
	axis.set_ylabel("")
	figure.tight_layout()
	st.pyplot(figure, use_container_width=True)
	plt.close(figure)

left, right = st.columns(2)

with left:
	rating_counts = netflix["Rating"].value_counts().sort_index()
	figure, axis = plt.subplots(figsize=(7, 4.5))
	rating_counts.plot(kind="bar", ax=axis, color="#e50914", width=0.68)
	axis.set_title("Rating Distribution", loc="left", color="#f5f5f1", pad=16, fontsize=15)
	axis.set_xlabel("Rating")
	axis.set_ylabel("Customers")
	axis.spines[["top", "right"]].set_visible(False)
	axis.grid(axis="y", color="#444444", linewidth=0.6, alpha=0.55)
	axis.set_axisbelow(True)
	plt.xticks(rotation=0)
	figure.tight_layout()
	st.pyplot(figure, use_container_width=True)
	plt.close(figure)

with right:
	revenue_by_category = netflix.groupby("Category")["Monthly_Revenue"].sum().sort_values(ascending=False)
	figure, axis = plt.subplots(figsize=(7, 4.5))
	revenue_by_category.plot(
		kind="pie",
		ax=axis,
		colors=["#e50914", "#f5f5f1", "#777777", "#b20710", "#444444", "#d9d9d9"],
		autopct="%1.0f%%",
		startangle=90,
		wedgeprops={"edgecolor": "#181818", "linewidth": 2},
		textprops={"color": "#f5f5f1", "fontsize": 9},
	)
	axis.set_title("Category-wise Revenue", loc="left", color="#f5f5f1", pad=16, fontsize=15)
	axis.set_ylabel("")
	figure.tight_layout()
	st.pyplot(figure, use_container_width=True)
	plt.close(figure)
# In[ ]:




