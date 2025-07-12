# Who Wants to Be a Millionaire - Streamlit Quiz Game

An interactive, web-based quiz game inspired by "Who Wants to Be a Millionaire," built with Python and Streamlit.

## Live Demo

You can play the game live at the following link:
[https://pythonmill-game.streamlit.app/](https://pythonmill-game.streamlit.app/)

## Description

This project is a web-based quiz game where the user answers a series of multiple-choice questions in an interactive interface. For each correct answer, the user wins a progressively higher amount of prize money. The game ends if the user provides a wrong answer.

## How to Run Locally

1.  Make sure you have Python and Streamlit installed. If you don't have Streamlit, install it using pip:
    ```bash
    pip install streamlit
    ```
2.  Navigate to the `02_Millionaire_Game` directory in your terminal.
3.  Run the application:
    ```bash
    streamlit run main.py
    ```
4.  The game will open in a new tab in your web browser.

## Features

-   **Interactive Web Interface:** A clean and modern UI built with Streamlit.
-   **Multiple-Choice Questions:** A set of questions on various topics.
-   **Prize Ladder:** A sidebar displays the prize money for each question level.
-   **Session State Management:** The game remembers your progress during a session.
-   **Instant Feedback:** Get immediate feedback on whether your answer was correct or not.

## Technology Used

-   Python
-   Streamlit 