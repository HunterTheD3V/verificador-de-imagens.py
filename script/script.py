# dependencias
import os
import requests
import webbrowser
import time  
import atexit  

# Função para gerar um arquivo único
def get_unique_filename(base_name, extension):
    i = 1
    new_filename = f"{base_name}{extension}"
    while os.path.exists(new_filename):
        new_filename = f"{base_name}-{i}{extension}"
        i += 1
    return new_filename

# Arquivo com os links
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Gera a base do arquivo de saída HTML
output_html_base = "visualizar_imagem"
output_html = get_unique_filename(output_html_base, ".html")
output_txt = "links_validos.txt"
valid_urls = []

print("⏳ Testando links...")

# Testa os links
for i, url in enumerate(urls):
    try:
        # Primeiro verifica se o link é responsivo
        res = requests.head(url, timeout=5)
        if res.status_code == 200:
            # Se responder, tenta baixar a imagem pra ver se ela carrega
            img_res = requests.get(url, timeout=5)
            if img_res.status_code == 200 and img_res.headers.get('content-type', '').startswith('image/'):
                valid_urls.append(url)
                print(f"[✔️] {i+1}: {url}")
            else:
                print(f"[❌] {i+1}: {url} (Não é uma imagem válida)")
        else:
            print(f"[❌] {i+1}: {url} (Status {res.status_code})")
    except Exception as e:
        print(f"[⚠️] {i+1}: {url} (Erro: {e})")
    
    time.sleep(0.5)  # Delay de 500ms entre cada requisição pra não tomar rate limit, necessário se estiver puxando imagens de uma cdn mais rigorosa

# Cria uma página HTML com os links válidos
try:
        # Verifica se o arquivo de links válidos existe e tem conteúdo, caso contrário ele aborta a operação
    if os.path.exists(output_txt) and not valid_urls and os.path.getsize(output_txt) == 0:
        raise Exception("Nenhum link válido encontrado para gerar o HTML! :(")
    
    with open(output_html, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Verificador de imagens</title><author>Hunter</author></head><body>\n")
        f.write("<h1>Imagens  Geradas</h1>\n")
        for url in valid_urls:
            f.write(f'<img src="{url}" style="max-width:300px; margin:10px;">\n')
        f.write("</body></html>")
    print(f"✅ HTML salvo em: {output_html}")
except Exception as e:
    print(f"Erro ao salvar o HTML: {e}")

# Salva os links válidos em um .txt numerado do 1 em diante
try:
    with open(output_txt, "w", encoding="utf-8") as f:
        for idx, url in enumerate(valid_urls, 1):
            f.write(f"{idx}: {url}\n")
    print(f"📝 Links válidos salvos em: {output_txt}")
except Exception as e:
    print(f"Erro ao salvar o arquivo de texto: {e}")

# Verifica se o arquivo .txt foi realmente criado
if os.path.exists(output_txt):
    print(f"Arquivo de links válidos encontrado: {output_txt}")
else:
    print("O arquivo de links válidos não foi criado.")

webbrowser.open(f"file://{os.path.abspath(output_html)}")

# Função pra limpar o arquivo de links válidos - necessário se quiser evitar acúmulo de cache
def limpar_arquivo():
    if os.path.exists(output_txt):
        os.remove(output_txt)
        print("🧹 Arquivo links_validos.txt foi limpo!")
