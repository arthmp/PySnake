# 🐍 PySnake

### Descrição do Projeto

Este projeto é um jogo da cobrinha simples implementado em Python utilizando a biblioteca `curses`. Ele foi criado com o objetivo de praticar conceitos fundamentais de programação.
---

### 🎥 Vídeo de Exemplo

https://github.com/user-attachments/assets/a2b55b18-6b89-4529-8e52-e8a65d113db6

---

### 🔨 Funcionalidades do projeto

- **Movimentação da Cobrinha**: Controle a cobrinha usando as setas do teclado para coletar frutas e aumentar seu tamanho.
- **Pontuação Dinâmica**: A cada fruta coletada, sua pontuação aumenta em 1.
- **Dificuldades Selecionáveis**: Escolha entre cinco níveis de dificuldade, alterando a velocidade do jogo.
- **Detecção de Colisões**:
  - Borda: O jogo termina quando a cobrinha colide com as bordas.
  - Corpo: O jogo termina se a cobrinha colidir com ela mesma.
  - Frutas: A cobrinha cresce ao consumir uma fruta.

---

### 📁 Acesso ao projeto

Para acessar o código do projeto, faça o download do arquivo [**pysnake.py**](https://github.com/arthmp/PySnake/blob/main/pysnake.py)  e siga as instruções abaixo para executá-lo.

---

### 🛠 Abrir e rodar o projeto

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Instale a biblioteca `curses` (já integrada no Python para sistemas Linux/Mac. Para Windows, será necessário usar `windows-curses` com o comando `pip install windows-curses`).
3. Execute o arquivo `pysnake.py` no terminal utilizando o comando:

   ```bash
   python pysnake.py
   ```

4. Escolha o nível de dificuldade ao iniciar o jogo.
5. Controle a cobrinha utilizando as teclas de seta para coletar frutas e evitar colisões.

---

### ✅ Técnicas e tecnologias utilizadas

- **Python 3**
- **Biblioteca curses** para renderização no terminal e manipulação de eventos.
