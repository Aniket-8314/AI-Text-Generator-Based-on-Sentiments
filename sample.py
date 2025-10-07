from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")

prompt = "Write a positive message about learning from mistakes."

result = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.7,       # lower = more focused
    top_p=0.9,             # limits sampling to top 90% probability
    repetition_penalty=1.2,# penalizes repeated tokens
    do_sample=True,        # enables probabilistic sampling
    pad_token_id=50256     # GPT-2 needs this to avoid warnings
)

print(result[0]["generated_text"])
