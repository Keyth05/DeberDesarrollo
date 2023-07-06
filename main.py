from typing import Union

import uvicorn
from fastapi import FastAPI
from uce.ai.prueba import Document, inference

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/inference')
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }


if __name__ == '__main__':
    uvicorn.run(app, host= '128.0.0.1', port=9049)
