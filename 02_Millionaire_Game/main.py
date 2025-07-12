import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Millionaire Quiz Game",
    page_icon="🏆",
    layout="wide",
)

# --- Data ---
questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", 2],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", 2],
    ["What is the chemical symbol for water?", "O2", "H2O", "CO2", 2],
    ["How many continents are there?", "5", "6", "7", 3],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", 3],
    ["Which country is home to the kangaroo?", "New Zealand", "Australia", "South Africa", 2],
    ["What is the boiling point of water at sea level?", "90°C", "100°C", "110°C", 2]
]

prize_money = [
    100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000
]

# --- Session State Initialization ---
def initialize_state():
    """Initializes or resets the game state."""
    st.session_state.current_question = 0
    st.session_state.total_winnings = 0
    st.session_state.game_over = False

if 'current_question' not in st.session_state:
    initialize_state()

# --- UI Functions ---
def display_question():
    """Displays the current question and answer options."""
    question_data = questions[st.session_state.current_question]
    question_text, option1, option2, option3, _ = question_data
    
    st.header(f"Question {st.session_state.current_question + 1}")
    st.subheader(question_text)

    # Create columns for the answer buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(f"A: {option1}", use_container_width=True):
            handle_answer(1)
    with col2:
        if st.button(f"B: {option2}", use_container_width=True):
            handle_answer(2)
    with col3:
        if st.button(f"C: {option3}", use_container_width=True):
            handle_answer(3)

def display_game_over():
    """Displays the game over message and the final score."""
    st.error("❌ Wrong Answer! Game Over.")
    st.balloons()
    st.success(f"You have won: ₹{st.session_state.total_winnings:,.0f}")
    if st.button("Play Again", use_container_width=True):
        initialize_state()
        st.rerun()

def display_win_message():
    """Displays a message when the user wins the entire game."""
    st.balloons()
    st.success("🎉 Congratulations! You have answered all questions correctly!")
    st.header(f"Total Winnings: ₹{st.session_state.total_winnings:,.0f}")
    if st.button("Play Again", use_container_width=True):
        initialize_state()
        st.rerun()

# --- Game Logic ---
def handle_answer(selected_option):
    """Checks the selected answer and updates the game state."""
    question_data = questions[st.session_state.current_question]
    correct_answer_index = question_data[4]

    if selected_option == correct_answer_index:
        st.session_state.total_winnings = prize_money[st.session_state.current_question]
        st.session_state.current_question += 1
        st.toast("✅ Correct!", icon="🎉")
        
        # Check if the user has won the game
        if st.session_state.current_question >= len(questions):
            st.session_state.game_over = True
            
    else:
        st.session_state.game_over = True
    
    st.rerun()

# --- Main App ---
st.title("🏆 Who Wants to Be a Millionaire?")
st.markdown("---")

# --- Sidebar with Prize Money ---
with st.sidebar:
    st.header("Prize Money")
    for i, prize in reversed(list(enumerate(prize_money))):
        level = len(prize_money) - i
        # Highlight the current prize level
        if level == len(prize_money) - st.session_state.current_question:
            st.markdown(f"**> Level {level}: ₹{prize:,.0f}**")
        else:
            st.markdown(f"Level {level}: ₹{prize:,.0f}")

# --- Main Game Area ---
if st.session_state.game_over:
    if st.session_state.current_question >= len(questions):
        display_win_message()
    else:
        display_game_over()
else:
    display_question()
