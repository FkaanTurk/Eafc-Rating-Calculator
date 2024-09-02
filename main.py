import streamlit as st

# Constants
st.title("Welcome to Eafc Rating Calculator")
st.write("## Put the Ratings of Your Players")

max_rated_cards = 11  # Define the maximum number of rated cards you want to allow
rated_cards = []  # List to store information about each rated card

another_rated = True  # Initialize with True to enter the loop
index = 1  # Start with the first rated card

while another_rated and index <= max_rated_cards:
    rating = st.number_input(f"What's the **rating** for card **{index}**?", 0, 99, key=f"rating_{index}", placeholder="Type a number...", step=None)
    how_many = st.number_input(f"**How many** of card **{index}**?", 0, 11, value=1, key=f"how_many_{index}", placeholder="Type a number...", step=None)
    rated_cards.append({"rating": rating, "how_many": how_many})

    # Ask if there is another rated card, except for the last allowed card
    if index < max_rated_cards:
        another_rated = st.toggle(f"Do you have another rated card after card {index}?", value=False, key=f"another_rated_{index}")

    index += 1  # Increment the index for the next card

else:
    st.write("### All done!")

# Calculate the total of all ratings
total_ratings = sum(card["rating"] * card["how_many"] for card in rated_cards)

# Calculate the average by dividing the sum by 11
average_rating = total_ratings / 11


st.write(f"## The average rating is:  {average_rating:.3f}")
