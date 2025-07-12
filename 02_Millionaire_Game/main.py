questions = [
    ["What is the name of our planet?", "Sun", "Mars", "Earth", 3],
    ["The capital of India?", "Delhi", "Mumbai", "Lucknow", 1],
    ["Which gas do humans need to breathe?", "Carbon Dioxide", "Oxygen", "Nitrogen", 2],
    ["How many continents are there?", "5", "6", "7", 3],
    ["Who invented the light bulb?", "Newton", "Edison", "Einstein", 2],
    ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", 2],
    ["What is the boiling point of water?", "90°C", "100°C", "110°C", 2],
    ["Which is the smallest prime number?", "0", "1", "2", 3],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Saturn", 2],
    ["Who wrote the national anthem of India?", "Rabindranath Tagore", "Mahatma Gandhi", "Subhash Chandra Bose", 1],
]

prize = [100, 200, 300, 400, 500, 600, 700, 800, 900, 10000]
total_earned = 0

print("🔰 Welcome to the Quiz Game 🔰\n")

for i, ques in enumerate(questions):
    print(f"Q{i+1}. {ques[0]}")
    print(f"1. {ques[1]}")
    print(f"2. {ques[2]}")
    print(f"3. {ques[3]}")
    
    try:
        ans = int(input("👉 Enter your answer (1/2/3): "))
    except ValueError:
        print("❌ Invalid input! Exiting game.")
        break

    if ans == ques[4]:
        print("✅ Correct Answer!\n")
        total_earned = prize[i]
    else:
        print("❌ Wrong Answer. Better luck next time!")
        break

print(f"\n🏆 You earned ₹{total_earned}")
print("Thanks for playing!")
