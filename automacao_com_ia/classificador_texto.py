def classificar(texto):
    texto = texto.lower()

    if "erro" in texto or "problema" in texto:
        return "Suporte Técnico"
    elif "pagamento" in texto or "fatura" in texto:
        return "Financeiro"
    elif "contrato" in texto:
        return "Jurídico"
    else:
        return "Geral"

mensagem = input("Digite a mensagem:\n")
categoria = classificar(mensagem)

print(f"Categoria identificada: {categoria}")