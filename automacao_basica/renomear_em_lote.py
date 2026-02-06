import os

PASTA = "arquivos"

for i, arquivo in enumerate(os.listdir(PASTA), start=1):
    extensao = os.path.splitext(arquivo)[1]
    novo_nome = f"arquivo_{i}{extensao}"

    os.rename(
        os.path.join(PASTA, arquivo),
        os.path.join(PASTA, novo_nome)
    )

print("Arquivos renomeados.")