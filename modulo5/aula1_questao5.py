import emoji
print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")
f = input("Digite uma frase e ela será emojizada: ")
print("Frase emojizada:")
print(emoji.emojize(f))