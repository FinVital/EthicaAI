import openai

# Initialize OpenAI with your API key
openai.api_key = "openAI"

def generate_insights(dilemma):
    prompt = f"Given the following ethical dilemma:\n\n{dilemma}\n\nProvide actionable insights and recommendations based on different moral philosophies and stakeholder perspectives."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that provides ethical insights and recommendations."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()