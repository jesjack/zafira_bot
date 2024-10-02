from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def gen_code(request):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Responde únicamente con el código de Python necesario para cumplir con la solicitud. En caso de no poder formular con código escribe tu respuesta dentro de una función print().\n\nEj:\nUser: Primeros 10 números primos.\nRes: ```python\ndef es_primo(num):\n    if num < 2:\n        return False\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            return False\n    return True\n\ndef primeros_primos(n):\n    primos = []\n    num = 2\n    while len(primos) < n:\n        if es_primo(num):\n            primos.append(num)\n        num += 1\n    return primos\n\n# Mostrar los primeros 10 números primos\nprint(primeros_primos(10))\n```\n\bLas librerías se instalan automáticamente."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": request
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    pre_code = response.choices[0].message.content
    pre_code = pre_code.replace("```python\n", "")
    return pre_code.replace("\n```", "")