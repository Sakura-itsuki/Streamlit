import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSVグラフ可視化", layout="centered")
st.title("📊 CSVファイル グラフ可視化アプリ")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("✅ データのプレビュー")
    st.dataframe(df.head())

    st.subheader("📈 グラフの設定")

    # 数値列のみ抽出
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns

    if len(numeric_columns) >= 2:
        x_col = st.selectbox("X軸に使用するカラム", numeric_columns)
        y_col = st.selectbox("Y軸に使用するカラム", numeric_columns)
        chart_type = st.radio("グラフの種類", ["散布図", "棒グラフ", "折れ線グラフ"])

        fig, ax = plt.subplots()
        if chart_type == "散布図":
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        elif chart_type == "棒グラフ":
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        elif chart_type == "折れ線グラフ":
            sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)

        st.subheader("📊 統計情報")
        st.write(df[[x_col, y_col]].describe())
    else:
        st.warning("数値カラムが2つ以上あるCSVファイルをご利用ください。")

else:
    st.info("左のサイドバーからCSVファイルをアップロードしてください。")
