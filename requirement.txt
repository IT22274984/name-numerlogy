import streamlit as st

def calculate_letter_value(word):
    letter_values = {
        1: "AIJYQ",
        2: "BKR",
        3: "CGLS",
        4: "DMT",
        5: "ENXH",
        6: "UVW",
        7: "OZ",
        8: "FP",
    }

    # Create a dictionary for easy lookup
    value_dict = {}
    for value, letters in letter_values.items():
        for letter in letters:
            value_dict[letter] = value

    # Calculate the sum of the word's letters
    total_value = 0
    for letter in word.upper():
        total_value += value_dict.get(letter, 0)  # Default to 0 if the letter is not in the map

    return total_value

# Streamlit app
st.title("Letter Value Calculator")

# Input field for the user
word = st.text_input("Enter a word to calculate its value:", "")

if word:
    word_value = calculate_letter_value(word)
    st.write(f"The value of the word '{word}' is: {word_value}")

st.markdown("### Instructions")
st.markdown(
    "1. Enter a word into the input box.\n"
    "2. The application will calculate the sum of the letter digit values based on the given mapping.\n"
    "3. Non-alphabetic characters are ignored."
)
