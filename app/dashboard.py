import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.engine import OSINTEngine
from app.utils import generate_csv_report, generate_excel_report
from app.config import APP_TITLE, APP_ICON

# App layout setup
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")

st.title("🔍 Threat Intelligence Matrix: OSINT Tools Analytical Framework")
st.markdown("""
This production-tier framework provides deep empirical comparisons, scoring vectors, and operational assessment matrices 
for prominent Open-Source Intelligence (OSINT) engines. Developed for SecOps analysts, threat hunters, and security researchers.
""")
st.write("---")

engine = OSINTEngine()
df = engine.get_processed_dataframe()

if df.empty:
    st.error("Engine failure: Asset data source could not be initialized.")
else:
    # Sidebar Filtering Mechanism
    st.sidebar.header("Filter & Parameter Tuning")
    all_use_cases = sorted(list(set([uc.strip() for sublist in engine.raw_data for uc in sublist["use_cases"]])))
    selected_use_case = st.sidebar.selectbox("Filter by Security Use Case", ["All Matrices"] + all_use_cases)
    
    complexity_filter = st.sidebar.multiselect(
        "Deployment Setup Complexity", 
        options=["Low", "Medium", "High"], 
        default=["Low", "Medium", "High"]
    )
    
    # Filter operations
    filtered_df = df[df['installation_complexity'].isin(complexity_filter)]
    if selected_use_case != "All Matrices":
        filtered_df = filtered_df[filtered_df['use_cases'].str.contains(selected_use_case)]

    # Metrics Row
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Tool Profiles Analyzed", len(df))
    m2.metric("Filtered Candidates Matched", len(filtered_df))
    m3.metric("Top Ranked Tool in View", filtered_df.iloc[0]['name'] if not filtered_df.empty else "N/A")

    st.subheader("📊 Empirical Capability & Composite Ranking Table")
    display_cols = ["name", "purpose", "composite_score", "ease_of_use", "accuracy", "performance", "automation", "reporting", "installation_complexity"]
    st.dataframe(filtered_df[display_cols].style.background_gradient(cmap="Blues", subset=["composite_score", "accuracy", "performance"]))

    # Visualizations
    st.write("---")
    st.subheader("📈 Visualization Canvas")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        st.write("#### Composite Threat Intelligence Matrix Score")
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.barplot(x="composite_score", y="name", data=filtered_df, palette="viridis", ax=ax)
        ax.set_xlabel("Composite Score (Max 10.0)")
        ax.set_ylabel("OSINT Platform Identifier")
        st.pyplot(fig)
        
    with col_v2:
        st.write("#### Accuracy Vector vs Execution Performance Profile")
        fig2, ax2 = plt.subplots(figsize=(7, 4.5))
        sns.scatterplot(x="accuracy", y="performance", hue="name", size="composite_score", data=filtered_df, sizes=(100, 400), ax=ax2)
        ax2.set_xlim(4, 11)
        ax2.set_ylim(4, 11)
        ax2.grid(True, linestyle="--", alpha=0.6)
        st.pyplot(fig2)

    # Detailed Inspect View
    st.write("---")
    st.subheader("🕵️ Deep-Dive Granular Intelligence Profiles")
    selected_tool_name = st.selectbox("Select specific engine asset to view complete tactical data", filtered_df["name"].tolist())
    
    if selected_tool_name:
        tool_data = filtered_df[filtered_df["name"] == selected_tool_name].iloc[0]
        t1, t2 = st.columns(2)
        with t1:
            st.markdown(f"**Functional Domain:** `{tool_data['purpose']}`")
            st.markdown(f"**Core Features Incorporated:** \n- {tool_data['features'].replace(', ', '\n- ')}")
            st.markdown(f"**Data Feeds / APIs Collected:** \n- {tool_data['data_sources'].replace(', ', '\n- ')}")
        with t2:
            st.info(f"👍 **Operational Strengths:** \n- {tool_data['advantages'].replace(', ', '\n- ')}")
            st.error(f"⚠️ **Known Limitations & Constraints:** \n- {tool_data['limitations'].replace(', ', '\n- ')}")

    # Report Data Exporter Export Module
    st.write("---")
    st.subheader("💾 Export Compliance & Analytical Reports")
    c1, c2 = st.columns(2)
    
    csv_bytes = generate_csv_report(filtered_df)
    excel_bytes = generate_excel_report(filtered_df)
    
    c1.download_button(
        label="📥 Export Structured Data to CSV format",
        data=csv_bytes,
        file_name="osint_matrix_export.csv",
        mime="text/csv"
    )
    
    c2.download_button(
        label="📥 Export Enterprise Grade Report to Excel",
        data=excel_bytes,
        file_name="osint_matrix_export.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )