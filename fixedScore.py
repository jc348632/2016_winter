"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    prompt = count_score(score)
    print(prompt)
def count_score(score):
    if score < 0 or score > 100:
        prompt = "Invalid score"
    elif score > 50 and score <= 90:
        prompt = "Passable"
    elif score > 90:
        prompt = "Excellent"
    elif score <= 50:
        prompt = "Bad"
    return prompt

main()