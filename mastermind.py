print 'Content-type: text/html'
print ''

import cgi
import random
form = cgi.FieldStorage()

vermelhos = 0
brancos = 0

if "resposta" in form:
    resposta = form.getvalue("resposta")
else:
    resposta = ""
    for i in range(4):
        resposta += str(random.randint(0, 9))

if "jogada" in form:
    jogada = form.getvalue("jogada")
    for key, digit in enumerate(jogada):
        if digit == resposta[key]:
            vermelhos += 1
        else:
            for respostaDigit in resposta:
                if respostaDigit == digit:
                    brancos += 1
                    break
        
else:
    jogada = ""
    
if "rodada" in form:
    rodada = int(form.getvalue("rodada")) + 1
else:
    rodada = 0

if rodada == 0:
    message = "Eu escolhi 4 numeros. Voce consegue advinha-los?"
elif vermelhos == 4:
    message = "Parabéns! Voce acertou em " + str(rodada) + " jogadas. <a href=''>Jogar novamente</a>"
else:    
    message = "Voce tem " + str(vermelhos) + " digitos corretos no lugar correto, e " + str(brancos) + " digitos corretos no lugar errado. Voce teve " + str(rodada) + " jogada(s)."
