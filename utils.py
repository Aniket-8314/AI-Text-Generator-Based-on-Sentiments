from textblob import TextBlob
from transformers import pipeline
import re

# Lazy model cache
generators = {}

def get_generator(model_name="openai-community/gpt2-medium"):
    """Load and cache text-generation pipeline."""
    global generators
    if model_name not in generators:
        generators[model_name] = pipeline(
            "text-generation",
            model=model_name,
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=50256,
        )
    return generators[model_name]

def get_sentiment(text: str) -> str:
    """Classify text sentiment as positive, negative, or neutral."""
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def clean_text(text: str) -> str:
    """Remove extra whitespace and repeated characters."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(.)\1{3,}', r'\1', text)
    return text.strip()

def generate_text(prompt: str, sentiment: str, max_length: int = 150, model_name: str = "openai-community/gpt2-medium") -> str:
    """Generate sentiment-aligned text with tuned sampling."""
    model = get_generator(model_name)

    # Create a natural prefix based on sentiment
    prefix = f"A {sentiment} paragraph about {prompt}:\n"

    out = model(prefix, max_new_tokens=max_length)
    text = out[0]["generated_text"]

    # Remove the prefix repetition
    text = text.replace(prefix, "").strip()
    text = clean_text(text)

    # End at the first sentence if very long
    # if "." in text:
    #     text = text.split(".")[0] + "."

    return text
