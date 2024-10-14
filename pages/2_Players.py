import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.set_page_config(
    page_title="Players",
    page_icon="⚽️",
    layout="wide"
)


df_data = st.session_state ["data"]
#clubes = df_data["Club"].value_counts().index
clubes =df_data["Club"].drop_duplicates().sort_values()
club = st.sidebar.selectbox("Clubes", clubes)

df_players = df_data[df_data["Club"]== club]
#players = df_players["Name"].value_counts().index
players = df_players["Name"].sort_values()
player = st.sidebar.selectbox("Players", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Club:** {player_stats['Club']}")

# Função para limpar o HTML e retornar apenas o texto
def remove_html_tags(cell_value):
    if isinstance(cell_value, str):
        soup = BeautifulSoup(cell_value, 'html.parser')
        return soup.get_text()  # Retorna apenas o texto, sem tags
    return cell_value

# Aplicar a função a uma coluna específica
df_data['Position'] = df_data['Position'].apply(remove_html_tags)
st.markdown(f"**Position:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Age:** {player_stats['Age']}")
col2.markdown(f"**Height:** {player_stats['Height']}") 
col3.markdown(f"**Weight:** {player_stats['Weight']}")

st.divider()
st.subheader(f"Overall - {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f" {player_stats['Value']}")
col2.metric(label="Remuneração semanal", value=f" {player_stats['Wage']}")
col3.metric(label="Cláusula de rescisão", value=f" {player_stats['Release Clause']}")