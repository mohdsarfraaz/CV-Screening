import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

def render_results(results):
    df = pd.DataFrame(results).sort_values(by="Score (%)", ascending=False).reset_index(drop=True)
    df.index += 1

    # Download links
    def make_download_link(file_path):
        try:
            with open(file_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            fname = file_path.split("/")[-1]
            return f'<a href="data:application/octet-stream;base64,{b64}" download="{fname}">📂 Download</a>'
        except Exception as e:
            return f"❌ {e}"

    df["Download Resume"] = [make_download_link(p) for p in df["File Path"]]
    df.drop(columns=["File Path"], inplace=True)

    st.subheader("📊 Candidate Screening Results")
    st.dataframe(df)

    # Metrics
    col1,col2,col3 = st.columns(3)
    with col1: st.metric("Total Resumes", len(df))
    with col2: st.metric("Qualified", (df["Qualified"]=="✅ Yes").sum())
    with col3: st.metric("Unqualified", (df["Qualified"]=="❌ No").sum())

    # Score Distribution
    fig, ax = plt.subplots()
    df["Score (%)"].astype(float).plot(kind="hist", bins=10, ax=ax)
    ax.set_xlabel("Match Score (%)")
    st.pyplot(fig)
