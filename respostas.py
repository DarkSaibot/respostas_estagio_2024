'''
Resposta 1


O valor final da variável SOMA será 91.

Explicação:

O código define três variáveis:

INDICE: um inteiro com valor 13.
SOMA: um inteiro com valor inicial 0.
K: um inteiro com valor inicial 0.
O loop while é executado enquanto K for menor que INDICE.

Dentro do loop, K é incrementado em 1 e SOMA é atualizado com a soma de si mesmo e de K.

O loop termina quando K é igual a INDICE, ou seja, 13.

O valor final de SOMA é a soma de todos os valores de K de 1 a 13.

Essa soma pode ser calculada usando a fórmula da soma de uma progressão aritmética:

SOMA = n * (a1 + an) / 2
Onde:

n é o número de termos (13).
a1 é o primeiro termo (1).
an é o último termo (13).
Substituindo os valores na fórmula, obtemos:

SOMA = 13 * (1 + 13) / 2 = 13 * 14 / 2 = 91
Portanto, o valor final da variável SOMA será 91.
'''

#Resposta 2


def fibonacci(n):
  """
  Função que calcula a sequência de Fibonacci até o n-ésimo termo.

  Argumentos:
    n (int): Número de termos da sequência a serem calculados.

  Retorno:
    Lista com os n primeiros termos da sequência de Fibonacci.
  """
  if n <= 1:
    return [0] * n
  else:
    fib_seq = [0, 1]
    for i in range(2, n):
      fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

def main():
  """
  Função principal que solicita o número ao usuário e verifica se ele pertence à sequência de Fibonacci.
  """
  numero = int(input("Digite um número: "))
  fib_seq = fibonacci(numero + 1)
  if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci!")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()

#Resposta 3

#a) 1, 3, 5, 7, ___

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  ultimo_numero = sequencia[-1]
  return ultimo_numero + 2

proximo_numero = proximo_numero([1, 3, 5, 7])
print(f"a) O próximo elemento é: {proximo_numero}")


#b) 2, 4, 8, 16, 32, 64, ____

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  ultimo_numero = sequencia[-1]
  return ultimo_numero * 2

proximo_numero = proximo_numero([2, 4, 8, 16, 32, 64])
print(f"b) O próximo elemento é: {proximo_numero}")


#c) 0, 1, 4, 9, 16, 25, 36, ____

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  ultimo_numero = sequencia[-1]
  return ultimo_numero + (len(sequencia) + 1) ** 2

proximo_numero = proximo_numero([0, 1, 4, 9, 16, 25, 36])
print(f"c) O próximo elemento é: {proximo_numero}")


#d) 4, 16, 36, 64, ____

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  ultimo_numero = sequencia[-1]
  return ultimo_numero + (len(sequencia) + 1) ** 2

proximo_numero = proximo_numero([4, 16, 36, 64])
print(f"d) O próximo elemento é: {proximo_numero}")


#e) 1, 1, 2, 3, 5, 8, ____

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  return sum(sequencia[-2:])

proximo_numero = proximo_numero([1, 1, 2, 3, 5, 8])
print(f"e) O próximo elemento é: {proximo_numero}")


#f) 2,10, 12, 16, 17, 18, 19, ____

def proximo_numero(sequencia):
  """
  Função para calcular o próximo número da sequência.

  Argumentos:
    sequencia: Uma lista de números.

  Retorna:
    O próximo número da sequência.
  """
  ultimo_numero = sequencia[-1]
  if ultimo_numero == 19:
    return 2
  else:
    return ultimo_numero + 1

proximo_numero = proximo_numero([2, 10, 12, 16, 17, 18, 19])
print(f"f) O próximo elemento é: {proximo_numero}")



#Resposta4

def descobrir_interruptores(interruptores):
  """
  Descobre qual interruptor controla qual lâmpada usando apenas duas idas à sala das lâmpadas.

  Argumentos:
    interruptores: Uma lista de três interruptores.

  Retorno:
    Uma lista de três strings, onde cada string é o nome da lâmpada que o interruptor correspondente controla.
  """

  # Ligue o interruptor 1 por 1 minuto e depois desligue-o.
  interruptores[0].ligar()
  time.sleep(60)
  interruptores[0].desligar()

  # Vá para a sala das lâmpadas e verifique as lâmpadas:
  #   - Se a lâmpada 1 estiver acesa, o interruptor 1 a controla.
  #   - Se a lâmpada 1 estiver quente, o interruptor 2 a controla.
  #   - Se a lâmpada 1 estiver fria, o interruptor 3 a controla.

  if lampadas[0].acesa:
    controle_lampada_1 = "interruptor 1"
  elif lampadas[0].quente:
    controle_lampada_1 = "interruptor 2"
  else:
    controle_lampada_1 = "interruptor 3"

  # Ligue o interruptor 2 e vá para a sala das lâmpadas.
  interruptores[1].ligar()
  time.sleep(10)

  # Verifique a lâmpada 2:
  #   - Se a lâmpada 2 estiver acesa, o interruptor 2 a controla.
  #   - Se a lâmpada 2 estiver apagada, o interruptor 3 a controla.

  if lampadas[1].acesa:
    controle_lampada_2 = "interruptor 2"
  else:
    controle_lampada_2 = "interruptor 3"

  # O interruptor 3 controla a lâmpada que não foi acesa por nenhum dos outros interruptores.
  controle_lampada_3 = "interruptor 3" if controle_lampada_1 != "interruptor 3" else "interruptor 2"

  return [controle_lampada_1, controle_lampada_2, controle_lampada_3]

# Simulação dos interruptores e lâmpadas
interruptores = [Interruptor(), Interruptor(), Interruptor()]
lampadas = [Lâmpada(), Lâmpada(), Lâmpada()]

# Descubra qual interruptor controla qual lâmpada
controle_lampadas = descobrir_interruptores(interruptores)

# Imprima os resultados
print(f"Lâmpada 1: {controle_lampadas[0]}")
print(f"Lâmpada 2: {controle_lampadas[1]}")
print(f"Lâmpada 3: {controle_lampadas[2]}")


#Resposta5

def inverter_string(texto):
  """
  Função que inverte os caracteres de uma string.

  Argumentos:
    texto: String a ser invertida.

  Retorno:
    String com os caracteres invertidos.
  """
  i = len(texto) - 1
  invertido = ""
  while i >= 0:
    invertido += texto[i]
    i -= 1
  return invertido

# Exemplo de uso
texto = "Olá, mundo!"
texto_invertido = inverter_string(texto)
print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")

