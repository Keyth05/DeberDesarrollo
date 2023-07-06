import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un programador que enseña a jovenes universitarios vas a generar una explicación para el tema que se te proporciona
            E.G: Programación
            -Es Springboot es una herramienta que hace que el desarrollo de aplicaciones web y microservicios con Java Spring Framework sea más rápido"""},
            {"role": "user", "content": prompt},

        ],
        temperature=0,
        # max_tokens=5
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]

