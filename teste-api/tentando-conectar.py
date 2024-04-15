import requests

response = requests.get("https://gold-anemone-wig.cyclic.app/receitas/todas")

if response.status_code == 200:
    receitas = response.json()

    for receita in receitas:
        print("\n Nome da Receita:", receita["receita"])
        print("\n Tipo:", receita["tipo"])
        print("\n Ingredientes:", receita["ingredientes"])
        print("\n Modo de Preparo:", receita["modo_preparo"])
        print("\nLink da Imagem:", receita["link_imagem"])
        print("-" * 50)  # Linha separadora entre as receitas
else:
    print("Erro ao obter as receitas:", response.status_code)
