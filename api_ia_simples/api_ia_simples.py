from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API de automação com IA rodando"}

@app.post("/classificar")
def classificar_texto(texto: str):
    texto = texto.lower()

    if "erro" in texto:
        categoria = "Suporte"
    elif "pagamento" in texto:
        categoria = "Financeiro"
    else:
        categoria = "Geral"

    return {"categoria": categoria}
