import os
"""
A simple, rule-based expert system for identifying colors between blue green and red.

This script uses a knowledge base and an inference engine to deduce a color
based on user's answers to a series of questions.
"""
# Knowledge Base for Color Identification
knowledge_base = {
    "color": {
        "red": {
            "questions": [
                "Is it warm?",
                "Is it the color of a ripe tomato?",
                "Is it the color of fire?"
            ]
        },
        "blue": {
            "questions": [
                "Is it cool?",
                "Is it the color of the sky?",
                "Is it the color of the ocean?"
            ]
        },
        "green": {
            "questions": [
                "Is it the color of grass?",
                "Is it the color of a leaf?"
            ]
        },
        "other": {
            "questions": [
                "Is it a color that is not red, blue, or green?",
                "Is it the color of a banana?"
            ]
        }
    }
}

# function for reasoning through questions answered by the user
def ask_question(question):
    response = input(question + " (yes/no): ")
    return response.lower() == "yes"

# Inference engine function for color identification
def run_inference_engine():
    for color, data in knowledge_base["color"].items():
        if all(ask_question(q) for q in data["questions"]):
            print(f"The color is {color}.")
            store_color(color)
            return
    print("Sorry, I couldn't determine the color.")
    print("Please try again.")

def main():
    print("Welcome to the Color Expert System!")
    while True:
        run_inference_engine()
        if ask_question("Do you want to see all stored colors?"):
            colors = retrieve_colors()
            print("Stored colors:", ", ".join(colors) if colors else "No colors stored yet.")
        if not ask_question("Do you want to try again?"):
            break
    print("Thank you for using the Color Expert System!")

# Function to store the identified color
def store_color(color):
    with open("colors.txt", "a") as file:
        file.write(color + "\n")

# Function to retrieve stored colors
def retrieve_colors():
    if not os.path.exists("colors.txt"):
        return []
    with open("colors.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    main()
