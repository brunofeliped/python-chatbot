import os


def processar_resposta(resposta, nome):
    if resposta == "1":
        print(f"{os.linesep}{nome}. 'Je pense, donc je suis' é a frase original, escrita em francês, do filósofo René Descartes (1596-1650). Ela resume o pensamento e o método de Descartes, para quem tudo tem início na dúvida.{os.linesep}")
    elif resposta == "2":
        print(f"{os.linesep}{nome}. Francisco Canhos é o nome do homem que, na década de 40, desenvolveu o primeiro chuveiro elétrico seguro em Jaú/SP (Brasil). O aparelho vinha sendo desenvolvido desde os anos 30, mas apresentava riscos de curto-circuito.{os.linesep}")
    elif resposta == "3":
        print(f"{os.linesep}{nome}. O Vaticano, sede da igreja católica, tem apenas 44 hectares (0,44 km2). A Rússia, localizada em dois continentes (Ásia e Europa), tem 17 milhões de km2.{os.linesep}")
    elif resposta == "4":
        print(f"{os.linesep}{nome}. Dom Quixote, de Miguel de Cervantes, é um clássico da literatura espanhola. A obra foi escrita em duas partes, uma em 1605, e a outra em 1615.{os.linesep}")
    elif resposta == "0":
        print(f"{os.linesep}{nome}. Obrigado !!!{os.linesep}")
    else:
        print(f"Digite uma opção válida !!!{os.linesep}")


def start():
    # Abertura ChatBot
    print("Olá! Bem-vindo ao ChatBot !!!")
    nome = input("Digite seu nome: ")

    while True:
        # Menu de Opções / Processamento de Respostas
        print(50*"-")
        resposta = input(
            f"{nome} o que gostaria de saber hoje?{os.linesep}[1] - De quem é a famosa frase Penso, logo existo?{os.linesep}[2] - De onde é a invenção do chuveiro elétrico?{os.linesep}[3] - Quais o menor e o maior país do mundo?{os.linesep}[4] - Qual o livro mais vendido no mundo a seguir à Bíblia?{os.linesep}[0] - Sair{os.linesep}")
        processar_resposta(resposta, nome)
        
        if resposta == "0":
            break

if __name__ == "__main__":
    start()
