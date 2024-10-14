import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽️",
    layout="wide"
)

df_data = st.session_state ["data"]
clubes = df_data["Club"].value_counts().index
#clubes =df_data["Club"].drop_duplicates().sort_values()
club = st.sidebar.selectbox("Clubes", clubes)

df_filtered = df_data[df_data["Club"]== club].set_index("Name")
st.image(df_filtered.iloc[0]["Club Logo"], )
st.markdown(f"## {club} ##")

columns = ["Age", "Photo", "Flag", "Overall", 'Value', 'Wage', 'Joined', 
           'Height', 'Weight', 'Contract Valid Until', 'Release Clause']

st.dataframe(df_filtered[columns],
            column_config={
                "Overall": st.column_config.ProgressColumn("Overall"),
                "Value": st.column_config.TextColumn(),
                "Wage": st.column_config.TextColumn("Weekly Wage"),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
            }, height=1000)
