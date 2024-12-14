import streamlit as st
import io

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

def interpret_value(value):
    if value % 9 == 1:
        return "Leadership and creativity"
    elif value % 9 == 2:
        return "Balance and harmony"
    else:
        return "Spirituality and wisdom"

# Streamlit app
st.title("🔢 Letter Value Calculator")
st.markdown("<h3 style='text-align: center; color: blue;'>Calculate the numeric value of your name or any word!</h3>", unsafe_allow_html=True)

# Display your name's numeric value
my_name = "YourName"  # Replace "YourName" with your actual name
my_name_value = calculate_letter_value(my_name)
st.subheader(f"The numeric value of your name '{my_name}' is: {my_name_value}")

# Input field for the user
word = st.text_input("Enter a word to calculate its value:", "")

# Initialize session state for name history
if 'name_history' not in st.session_state:
    st.session_state['name_history'] = []

if word:
    word_value = calculate_letter_value(word)
    st.session_state['name_history'].append((word, word_value))
    st.write(f"The value of the word '{word}' is: {word_value}")

    # Display letter-by-letter breakdown
    breakdown = [(letter, calculate_letter_value(letter)) for letter in word.upper()]
    st.write("Letter breakdown:")
    for letter, value in breakdown:
        st.write(f"{letter}: {value}")

    # Provide interpretation
    meaning = interpret_value(word_value)
    st.write(f"Meaning: {meaning}")

# Display previous calculations
st.markdown("### Previous Calculations")
for name, value in st.session_state['name_history']:
    st.write(f"{name}: {value}")

# Add report download functionality
if st.button("Download Report"):
    report = io.StringIO()
    report.write("Name Value Report\n\n")
    for name, value in st.session_state['name_history']:
        report.write(f"{name}: {value}\n")
    st.download_button("Download", report.getvalue(), "report.txt")

st.markdown("### Instructions")
st.markdown(
    "1. Enter a word into the input box.\n"
    "2. The application will calculate the sum of the letter digit values based on the given mapping.\n"
    "3. The breakdown and interpretation will be displayed.\n"
    "4. You can download the history of calculations as a report.\n"
    "5. Non-alphabetic characters are ignored."
)
