import pandas as pd
import streamlit as st
from PIL import Image
import base64
import os  # Import os module for path manipulation

# Function to convert image to base64
def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")
    return img_base64

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV file into a DataFrame
csv_file_path = os.path.join(current_dir, 'premier_league_player.csv')
df = pd.read_csv(csv_file_path, encoding='latin-1')

# Set Streamlit page configuration
img_path = os.path.join(current_dir, 'premier.png')
img = Image.open(img_path)
st.set_page_config(page_title="Mugare Premier: Document Generation AI", page_icon=img)

# Setting the title
title = "Player dashboard"
# Displaying the title
st.title(title)
# Displaying a horizontal line to separate content
st.markdown("---")
# Creating a sidebar with filter for players
st.sidebar.header("Please Filter Here:")
player = st.sidebar.selectbox(
     "Select player",
     options=df["Player"].unique()
)

# Filter the DataFrame based on the selected player
df_selection = df[df["Player"] == player]

# Display a message if no data is found for the selected player
if df_selection.empty:
    st.error("No data found for the selected player.")
else:
    # Animated GIF path
    anime_gif_path = os.path.join(current_dir, 'imgs', 'liongif.gif')

    # Custom CSS for background image
    background = """
    <style>
    body {
        background-image: url("premierleague.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)

    # Load and display sidebar image with glowing effect
    img_path = os.path.join(current_dir, 'premier.png')  # Update with correct path to your sidebar image
    img_base64 = img_to_base64(img_path)
    st.sidebar.image(anime_gif_path, use_column_width=True)

    st.sidebar.markdown("---")

    # Selecting the stats from the data that will be displayed
    expectedgoals = df_selection["Gls"].sum()
    goals = df_selection["Ast"].sum()
    assists = df_selection["xG"].sum()

    # Displaying player info and premierleague.jpg on the same line
    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Player Info:")
        player_info = df_selection[["Player", "Nation", "Pos", "Squad", "Born"]].iloc[0]
        st.write(player_info)

    with col2:
        lion_gif_path = os.path.join(current_dir, 'imgs', 'lion2gif.gif')
        st.image(lion_gif_path, use_column_width=False, width=500)  # Adjust the width as per your requirement

        # Displaying the selected stats inside columns
        st.subheader("Player Statistics:")
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
             st.subheader("Goals")
             st.subheader(f"{goals}")
        with middle_column:
             st.subheader("Assists")
             st.subheader(f"{assists}")
        with right_column:
             st.subheader("Expected goals")
             st.subheader(f"{expectedgoals}")

        # Custom CSS for glowing effect
        st.markdown(
            """
            <style>
            .cover-glow {
                width: 100%;
                height: auto;
                padding: 3px;
                box-shadow: 
                    0 0 5px #330000,
                    0 0 10px #660000,
                    0 0 15px #990000,
                    0 0 20px #CC0000,
                    0 0 25px #FF0000,
                    0 0 30px #FF3333,
                    0 0 35px #FF6666;
                position: relative;
                z-index: -1;
                border-radius: 30px;  /* Rounded corners */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Load and display sidebar image with glowing effect
        img_path = os.path.join(current_dir, 'imgs', 'premier.png')
        img_base64 = img_to_base64(img_path)
        st.sidebar.markdown(
            f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
            unsafe_allow_html=True,
        )
        st.sidebar.markdown("---")
