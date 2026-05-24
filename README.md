 ⚠️ Multi-OS Error Generator Pro

Ferramenta avançada para simulação de diálogos de sistema e engenharia social ética.

## 📂 Conteúdo

- **`win_generator.py`**: Versão Pro. Suporta múltiplos tipos de botões, ícones nativos e captura o retorno da resposta do usuário.
- **`linux_msg.py`**: Wrapper modular para diálogos GTK/KDE via Tkinter.

## ✨ Novidades v3.0 (Ultimate)
- **Ações Condicionais**: Execute comandos do Windows se o usuário clicar em "Sim".
- **Botão Agendar**: Novo modo de diálogo customizado para simular agendamentos.
- **Notification Beta**: Envio de notificações Toast nativas via PowerShell.
- **Interface em Abas**: Melhor organização para criadores de ferramentas.

## 🚀 Instalação e Uso

### Windows
O gerador principal requer a biblioteca `customtkinter`:
```bash
pip install customtkinter
```
Execute o gerador:
```bash
python win_generator.py
```

### Linux & macOS
Estes scripts utilizam o `tkinter` padrão do Python, que geralmente já está instalado.
```bash
# No Linux
python linux_msg.py

# No macOS
python macos_msg.py
```

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **CustomTkinter** (UI Moderna)
- **Ctypes** (Integração com API do Windows)
- **Tkinter** (Mensagens Cross-platform)
