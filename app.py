import streamlit as st
import random

# Define the Tarot deck
tarot_deck = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor',
              'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune',
              'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star',
              'The Moon', 'The Sun', 'Judgment', 'The World']

# Shuffle the Tarot deck
random.shuffle(tarot_deck)

# Set up the Streamlit app
st.title("Tarot Game")
st.write("Welcome to the Tarot game! Click the button below to draw a card from the deck.")

# Create a button to draw a card
if st.button("Draw a Card"):
    # Draw a card from the top of the deck
    card = tarot_deck.pop(0)
    
    # Show the name of the card
    st.write(f"You drew the {card} card!")
    
    # Show the image of the card (you'll need to have the card images saved locally)
    st.image(f"tarot_cards/{card.lower().replace(' ', '_')}.jpg")

This code creates a simple Tarot game in Streamlit that displays the name and image of a randomly drawn card from the Tarot deck each time the "Draw a Card" button is clicked. You'll need to have the Tarot card images saved locally in a folder called tarot_cards for the images to display properly.

