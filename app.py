from flask import Flask, render_template, request
from utils import get_sentiment, generate_text,get_generator

app = Flask(__name__)

# Preload the model once when Flask starts
get_generator()

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    detected_sentiment = None
    prompt = ''
    selected_sentiment = 'auto'
    selected_model = 'openai-community/gpt2-medium'
    length = 200

    if request.method == 'POST':
        prompt = request.form.get('prompt', '').strip()
        selected_sentiment = request.form.get('sentiment', 'auto')
        selected_model = request.form.get('model', 'openai-community/gpt2-medium')
        try:
            length = int(request.form.get('length', 200))
        except ValueError:
            length = 200

        if prompt:
            detected_sentiment = get_sentiment(prompt)
            final_sentiment = detected_sentiment if selected_sentiment == 'auto' else selected_sentiment
            output = generate_text(prompt, final_sentiment, max_length=length, model_name=selected_model)

    return render_template(
        'index.html',
        output=output,
        prompt=prompt,
        sentiment=detected_sentiment,
        selected_sentiment=selected_sentiment,
        selected_model=selected_model,
        length=length
    )

if __name__ == '__main__':
    app.run(debug=True)
