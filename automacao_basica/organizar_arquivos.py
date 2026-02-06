import os
import shutil

PASTA_ORIGEM = "downloads"

EXTENSOES = {
    "pdfs": [".pdf"],
    "imagens": [".jpg", ".png", ".jpeg"],
    "planilhas": [".csv", ".xlsx"]
}

for arquivo in os.listdir(PASTA_ORIGEM):
    for pasta, extensoes in EXTENSOES.items():
        if arquivo.lower().endswith(tuple(extensoes)):
            destino = os.path.join(PASTA_ORIGEM, pasta)
            os.makedirs(destino, exist_ok=True)

            shutil.move(
                os.path.join(PASTA_ORIGEM, arquivo),
                os.path.join(destino, arquivo)
            )

print("Arquivos organizados com sucesso.")
