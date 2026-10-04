print("================================")
print("        SPAM DETECTOR")
print("================================")

message = input("Enter your message: ")

spam_words = [
    "win",
    "winner",
    "free",
    "prize",
    "lottery",
    "cash",
    "offer",
    "claim",
    "urgent",
    "congratulations",
    "click",
    "discount"
]

words = message.lower().split()

found_words = []

for word in words:
    word = word.strip(".,!?")

    if word in spam_words:
        found_words.append(word)

print("\nYour Message:")
print(message)

if len(found_words) >= 2:
    print("\nResult: SPAM 🚨")
    print("Spam words detected:", ", ".join(found_words))

elif len(found_words) == 1:
    print("\nResult: POSSIBLE SPAM ⚠️")
    print("Spam word detected:", found_words[0])

else:
    print("\nResult: NOT SPAM ✅")
    print("No common spam words detected.")