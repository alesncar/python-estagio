from datetime import datetime

def log(mensagem):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("log.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{agora}] {mensagem}\n")

    print("Log registrado.")

log("Sistema iniciado")
