PALAVRAS_CHAVE = {
    "inserir",
    "buscar",
    "deletar",
    "pre_ordem",
    "em_ordem",
    "pos_ordem"
}

class Normalizer:
    def normalize(self, texto:str):
        texto = texto.replace(",", "")
        texto = texto.replace(".", "")

        tokens = texto.split()

        resultado = []

        for token in tokens:
            if token in PALAVRAS_CHAVE or token.lstrip("-").isdigit():
                resultado.append(token)

        return " ".join(resultado)