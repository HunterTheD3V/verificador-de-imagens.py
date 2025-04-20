import os
import time
import requests
import webbrowser

# Arquivo com os links
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Pasta para salvar HTML com imagens válidas
output_html = "visualizar_imagem.html"
output_txt = "links_validos.txt"
valid_urls = []

print("⏳ Testando links...")

# Testa os links com delay
for i, url in enumerate(urls):
    try:
        res = requests.head(url, timeout=5)
        if res.status_code == 200:
            valid_urls.append(url)
            print(f"[✔️] {i+1}: {url}")
        else:
            print(f"[❌] {i+1}: {url} (Status {res.status_code})")
    except Exception as e:
        print(f"[⚠️] {i+1}: {url} (Erro: {e})")
    
    delay(1000)  # espera 1 segundo antes do próximo request

# Cria uma página HTML com os links válidos
with open(output_html, "w", encoding="utf-8") as f:
    f.write("<html><head><title>Imagens SFW</title></head><body>\n")
    f.write("<h1>Imagens SFW Válidas</h1>\n")
    for url in valid_urls:
        f.write(f'<img src="{url}" style="max-width:300px; margin:10px;">\n')
    f.write("</body></html>")

# Salva os links válidos em um .txt numerado do 1 em diante
with open(output_txt, "w", encoding="utf-8") as f:
    for idx, url in enumerate(valid_urls, 1):
        f.write(f"{idx}: {url}\n")

print(f"\n✅ {len(valid_urls)} imagens válidas salvas em: {output_html}")
print(f"📝 Links válidos também foram salvos em: {output_txt}")
webbrowser.open(f"file://{os.path.abspath(output_html)}")
