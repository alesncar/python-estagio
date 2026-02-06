def resumir_texto(texto):
    frases = texto.split(".")
    resumo = frases[:2]
    return ".".join(resumo).strip() + "."

texto = input("Cole o texto para resumir:\n")
print("\nResumo gerado:")
print(resumir_texto(texto))