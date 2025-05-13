from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            # 응답 방식에 대한 지시
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            # 질문
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)

print(response.output_text)