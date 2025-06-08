quiz = {
    "Pergunta 1": {
        "pergunta": "Qual minha materia favorita?",
        "opcoes": ["A) dev. web", "B) lab. programacao", "C) banco de dados", "D) artes visuais digitais"],
        "resposta": "B"
    },
    "Pergunta 2": {
        "pergunta": "Qual meu professor favorito?",
        "opcoes": ["A) Claudete", "B) Abreu", "C) Agostinho", "D) Mamede"],
        "resposta": "C"
    },
    "Pergunta 3": {
        "pergunta": "Qual minha linguagem favorita?",
        "opcoes": ["A) Python", "B) C", "C) Java script", "D) HTML"],
        "resposta": "A"
    }
}
acertos = 0
for chave, valor in quiz.items():
    print("\n" + chave)
    print(valor["pergunta"])
    for opcao in valor["opcoes"]:
        print(opcao)
    resposta = input("Digite a letra da resposta correta: ").upper()
    if resposta == valor["resposta"]:
        print("Correto!")
        acertos += 1
    else:
        print("Errado!")
        print("Resposta certa:", valor["resposta"])
print("Fim do quiz!")
print("Você fez", acertos, "acertos")