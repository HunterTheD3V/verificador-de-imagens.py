# verificador-de-imagens.py 🖼🔧
um script que verifica links de imagens, testa se os links estão funcionando e filtra os links das imagens que funcionam, e as organiza para você visualizar em uma página. feito em python 🐍🖼️

## Como funciona 🤔
- Cole seus links de arquivos de imagem válidos no arquivo `urls.txt`, seguindo a formatação padrão (um em baixo do outro, sem markdown, sem formatação especial, apenas a separação de linha com a tecla ENTER)
- Inicialize o script. Após isso, ele iniciará a verificação dos links e retornará quais links são válidos e estão funcionando.
- Após o fim dos testes, você será redirecionado para uma página com as imagens válidas que foram verificadas e testadas, organizadas em HTML.

## Como instalar ⚙
- **Clone o repositório**

Em seu terminal (vscode terminal, powershell, prompt de comando, windows terminal, shell linux, linux terminal, entre outros), digite o comando:
```bash
git clone https://github.com/HunterTheD3V/verificador-de-imagens.py
```
*Ou caso se preferir: clique em clonar repositório e siga os procedimentos de clonagem de repositório padrão do github.*



- **Instale as dependências**

Em seu terminal/console, digite:
```bash
pip install requests
```
*Além disso, certifique-se que você possui Python instalado, ou que sua workspace/environment tenha suporte ao interpretador python.*

### Botando pra funcionar 🚀
- Após concluir todas as etapas de instalação, você já pode:
  - configurar imagens: no seu `urls.txt`, você já pode começar a inserir os links de imagens que você deseja (lembre-se de inserir links de imagens válidos)
  - inicializar o verificador de imagens: em seu terminal, digite:
    ```py
    python script.py
    ```
  - e pronto, só deixar o bicho trabalhar 😎


### Notas finais 📋
- O verificador de imagem **retornará** problemas se seu link **não for de imagem**
- O verificador organizará as imagens em uma grid (grade de imagens) para que você consiga visualizar quais imagens foram possíveis verificar
- É possível verificar se a imagem é um `Trojan` com este verificador, visto que imagens válidas, que possuem trojan, retornam erros imediatos.

### Inspiração ✨
Feito baseado em uma engine de aprendizado para IAs, que separava links de imagens para treinar a IA para filtrar imagens maliciosas (NSFW e trojans).

Como muitos links sofreram alterações e não poderiam ser abertos de forma casual, eu criei esse script para testar quais imagens estão funcionando, e auxiliar nas atualizações futuras da engine filtradora para IAs. E, de quebra, descobri que eu podia ir um pouco além com um simples verificador.

❤ Feito por **HunterTheD3V**, em suas etapas iniciais de aprendizado em python 🚀👾
