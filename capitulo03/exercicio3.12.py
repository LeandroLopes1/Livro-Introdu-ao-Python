distancia_a_percorrer = float(input("Digite a distância a percorrer: "))
velocidade_media = float(input("Digite a velocidade média: "))
tempo_percorrido = distancia_a_percorrer / velocidade_media
tempo_corrigido = tempo_percorrido * 60
print(f"O tempo para a chegada é: {tempo_corrigido:.2f} minutos")
