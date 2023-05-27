def get_ascii(word):
  for letra in word:
    print(f"Letra: {letra}")
    print(f"Representación en binario: {bin(ord(letra))}")
    print(f"Código ASCII: {ord(letra)}")
    print("")