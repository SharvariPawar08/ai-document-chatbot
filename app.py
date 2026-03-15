document = '''
Artificial Intelligence is transforming industries.
Machine learning allows computers to learn from data.
Generative AI can create text, images, and more.
'''

question = "What does machine learning do?"

if "machine learning" in question.lower():
    answer = "Machine learning allows computers to learn from data."
else:
    answer = "Answer not found in document."

print("Question:", question)
print("Answer:", answer)