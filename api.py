from fastapi import FastAPI
from modules import decoder
from modules import encoder


app = FastAPI()


@app.post("/v1/encoder")
def encode_text(text: str = "Testing sentence!"):
    return encoder.encoder(text)

@app.post("/v1/decoder")
def decode_text(text: str = "\\n—weird—\\nTisetng seetncne!\\n—weird—\\nsentence Testing"):
    return decoder.decoder(text)
