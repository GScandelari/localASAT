# Admin Tool Author Service (ASAT)

**Admin Tool Author Service (ASAT)** é uma aplicação GUI (Interface Gráfica de Usuário) criada com **PySimpleGUI** para gerenciar informações de Journals, Articles e Authors. O aplicativo permite ao usuário pesquisar e gerenciar informações desses itens, além de configurar APIs e chaves de acesso.

## Estrutura do Projeto

A aplicação foi dividida em módulos para melhorar a organização e manutenção do código:

```
LocalAS/
├── main.py          # Arquivo principal com o loop de eventos
├── windows.py       # Contém funções de criação de telas
├── utils.py         # Funções auxiliares, como logging
└── logs/            # Pasta de logs
```

## Funcionalidades

1. **Tela Principal (Home)**:
   - Contém botões para **Journal**, **Article** e **Author**.
   - Menu suspenso com opções:
     - **Settings** (Configurações):
       - **APIs** e **Keys**: Abre uma tela de configurações específicas.
     - **Profile** (Perfil):
       - **Edit Profile**: Abre uma tela para edição de nome de usuário e e-mail.
       - **Close**: Solicita confirmação antes de fechar a aplicação.

2. **Journals, Articles e Authors**:
   - Cada botão abre uma tela de gerenciamento específica.
   - Função **Search** em cada tela:
     - Para **Authors**, a pesquisa pode ser feita por **First Name**, **Last Name**, **Email** ou **User ID**.

3. **Logs de Ação**:
   - Todas as ações do usuário são registradas em `logs/log.txt`, incluindo data, hora e detalhes da ação tomada.

4. **Fechar Aplicação**:
   - A opção **Close** no menu **Profile** solicita confirmação antes de encerrar a aplicação.

## Pré-requisitos

- **Python 3.7+**
- **PySimpleGUI**: instale com `pip install PySimpleGUI`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd LocalAS
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o programa:
   ```bash
   python main.py
   ```
2. Navegue pelo menu para acessar as diferentes funcionalidades.
3. Todas as ações do usuário serão registradas no arquivo `logs/log.txt`.

## Estrutura de Arquivo e Funções

### `main.py`

Controla a lógica principal e o loop de eventos, interagindo com os módulos de telas (`windows.py`) e funções auxiliares (`utils.py`).

### `windows.py`

Contém funções para criar telas distintas da aplicação:
- `main_screen()`: Cria a tela principal.
- `settings_screen(option)`: Cria a tela de configurações.
- `profile_screen()`: Cria a tela de edição de perfil.
- `content_screen(content_type)`: Cria as telas de Journal, Article e Author, com recursos de busca.
- `confirm_close()`: Confirma o fechamento da aplicação.

### `utils.py`

Inclui funções auxiliares:
- `log_action(action)`: Registra ações no arquivo `logs/log.txt` com data e hora.

## Exemplo de Log

Abaixo está um exemplo de log de ações que pode ser gerado:

```
2024-10-28 15:45:12 - Screen opened: Home - Admin Tool Author Service (ASAT)
2024-10-28 15:46:00 - Screen opened: Settings for APIs
2024-10-28 15:47:05 - Action taken: Back to Home
2024-10-28 15:48:45 - Screen opened: Author Management
2024-10-28 15:49:30 - Search action in Author Management by Last Name with term: Smith
2024-10-28 15:50:15 - Action taken: Close Application
```

## Contribuindo

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas mudanças:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Faça push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

