from tokenizers import ByteLevelBPETokenizer

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Some sample text to "train" on (Rhythm of English and Urdu)
data = [
    "The essence of the book is captured in its rhythm.",
    "کتاب کا جوہر اس کے تال میں قید ہے۔",
    "Translation is not just words, it is soul.",
    "ترجمہ صرف الفاظ نہیں، یہ روح ہے۔"
]

# Save these to a temporary file
with open("temp_text.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

# Train the tokenizer
tokenizer.train(files=["temp_text.txt"], vocab_size=1000, min_frequency=2)

# Test it
output = tokenizer.encode("The soul of the book.")
print(f"Tokens: {output.tokens}")
print(f"IDs: {output.ids}")
