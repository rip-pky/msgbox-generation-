import customtkinter as ctk
import ctypes
import subprocess
import platform

# Configuração visual para manter o padrão moderno
def check_os_fallback():
    if platform.system() != "Windows":
        root = ctk.CTk()
        root.withdraw()
        from tkinter import messagebox
        messagebox.showerror("Erro de Compatibilidade", 
                             f"Este script foi feito para Windows, mas você está no {platform.system()}.")
        exit()

check_os_fallback()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WindowsErrorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("WinError Ultimate v3.0")
        self.geometry("600x750")
        self.resizable(False, False)

        # Cabeçalho
        ctk.CTkLabel(self, text="System Interaction Suite (Windows)", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)

        # Sistema de Abas
        self.tabview = ctk.CTkTabview(self, width=550, height=550)
        self.tabview.pack(padx=20, pady=10)
        
        self.tab_msg = self.tabview.add("Mensagem Nativa")
        self.tab_custom = self.tabview.add("Botões Custom")
        self.tab_notify = self.tabview.add("Notificações Beta")
        self.tab_settings = self.tabview.add("Aparência")

        self.setup_native_tab()
        self.setup_custom_tab()
        self.setup_notify_tab()
        self.setup_settings_tab()

    def setup_native_tab(self):
        self.title_entry = ctk.CTkEntry(self.tab_msg, placeholder_text="Título...", width=450)
        self.title_entry.pack(pady=10)

        self.msg_text = ctk.CTkTextbox(self.tab_msg, height=100, width=450)
        self.msg_text.insert("0.0", "Erro crítico no sistema.")
        self.msg_text.pack(pady=10)

        self.icon_var = ctk.StringVar(value="Crítico (Erro)")
        ctk.CTkOptionMenu(self.tab_msg, values=["Crítico (Erro)", "Interrogação", "Exclamação", "Informação"], 
                          variable=self.icon_var, width=450).pack(pady=5)

        self.btn_type_var = ctk.StringVar(value="Apenas OK")
        ctk.CTkOptionMenu(self.tab_msg, values=["Apenas OK", "OK e Cancelar", "Abortar, Repetir e Ignorar", 
                                                "Sim, Não e Cancelar", "Sim e Não", "Repetir e Cancelar"], 
                          variable=self.btn_type_var, width=450).pack(pady=5)

        # Opções de Comportamento do Diálogo
        extra_frame = ctk.CTkFrame(self.tab_msg, fg_color="transparent")
        extra_frame.pack(pady=10, fill="x", padx=45)

        self.modal_var = ctk.StringVar(value="Aplicação")
        ctk.CTkOptionMenu(extra_frame, values=["Aplicação", "Sistema", "Tarefa"], 
                          variable=self.modal_var, width=140).grid(row=0, column=0, padx=5)

        self.def_btn_var = ctk.StringVar(value="Botão 1 (Foco)")
        ctk.CTkOptionMenu(extra_frame, values=["Botão 1 (Foco)", "Botão 2 (Foco)", "Botão 3 (Foco)"], 
                          variable=self.def_btn_var, width=140).grid(row=0, column=1, padx=5)

        self.topmost_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(extra_frame, text="Sempre no Topo", variable=self.topmost_var).grid(row=0, column=2, padx=5)

        ctk.CTkLabel(self.tab_msg, text="Comando ao clicar 'Sim/OK':").pack(pady=(10,0))
        self.action_entry = ctk.CTkEntry(self.tab_msg, placeholder_text="Ex: start chrome.exe", width=450)
        self.action_entry.pack(pady=5)

        ctk.CTkButton(self.tab_msg, text="LANÇAR NATIVO", command=self.trigger_message, fg_color="#d32f2f").pack(pady=15)

        self.result_label = ctk.CTkLabel(self, text="Aguardando interação...", text_color="gray")
        self.result_label.pack(side="bottom", pady=10)

    def setup_custom_tab(self):
        ctk.CTkLabel(self.tab_custom, text="Diálogo com botão 'Agendar'", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        self.custom_msg = ctk.CTkEntry(self.tab_custom, placeholder_text="Mensagem...", width=450)
        self.custom_msg.insert(0, "Uma atualização foi agendada.")
        self.custom_msg.pack(pady=10)
        
        ctk.CTkButton(self.tab_custom, text="SIMULAR AGENDAMENTO", command=self.show_custom_dialog, fg_color="#1f538d").pack(pady=20)

    def setup_notify_tab(self):
        self.notify_title = ctk.CTkEntry(self.tab_notify, placeholder_text="Título...", width=450)
        self.notify_title.insert(0, "Segurança")
        self.notify_title.pack(pady=5)
        
        self.notify_body = ctk.CTkEntry(self.tab_notify, placeholder_text="Mensagem...", width=450)
        self.notify_body.insert(0, "Clique para limpar ameaças.")
        self.notify_body.pack(pady=5)
        
        ctk.CTkButton(self.tab_notify, text="ENVIAR TOAST", command=self.send_toast, fg_color="#FF9800").pack(pady=20)

    def setup_settings_tab(self):
        ctk.CTkLabel(self.tab_settings, text="Configurações de Interface", font=ctk.CTkFont(weight="bold")).pack(pady=20)
        ctk.CTkLabel(self.tab_settings, text="Modo de Aparência:").pack(pady=5)
        ctk.CTkSegmentedButton(self.tab_settings, values=["light", "dark", "system"], 
                               command=ctk.set_appearance_mode).pack(pady=10)

    def send_toast(self):
        title, msg = self.notify_title.get(), self.notify_body.get()
        ps = f'[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms");$i=New-Object System.Windows.Forms.NotifyIcon;$i.Icon=[System.Drawing.SystemIcons]::Information;$i.BalloonTipText="{msg}";$i.BalloonTipTitle="{title}";$i.Visible=$True;$i.ShowBalloonTip(10000)'
        subprocess.run(["powershell", "-Command", ps])

    def show_custom_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.geometry("400x200")
        dialog.attributes("-topmost", True)
        ctk.CTkLabel(dialog, text=self.custom_msg.get(), wraplength=350).pack(pady=30)
        f = ctk.CTkFrame(dialog, fg_color="transparent")
        f.pack(side="bottom", pady=20)
        ctk.CTkButton(f, text="Agora", width=100, command=dialog.destroy).pack(side="left", padx=5)
        ctk.CTkButton(f, text="Agendar", width=100, fg_color="gray", command=dialog.destroy).pack(side="left", padx=5)

    def trigger_message(self):
        title = self.title_entry.get() or "Erro"
        msg = self.msg_text.get("0.0", "end").strip()
        
        icons = {
            "Crítico (Erro)": 0x10,
            "Interrogação": 0x20,
            "Exclamação (Aviso)": 0x30,
            "Exclamação": 0x30,
            "Informação": 0x40
        }
        
        buttons = {
            "Apenas OK": 0x00,
            "OK e Cancelar": 0x01,
            "Abortar, Repetir e Ignorar": 0x02,
            "Sim, Não e Cancelar": 0x03,
            "Sim e Não": 0x04,
            "Repetir e Cancelar": 0x05
        }

        responses = {
            1: "OK", 2: "Cancelar", 3: "Abortar", 4: "Repetir",
            5: "Ignorar", 6: "Sim", 7: "Não"
        }

        flags = icons.get(self.icon_var.get(), 0x10) | buttons.get(self.btn_type_var.get(), 0x00)
        
        result_code = ctypes.windll.user32.MessageBoxW(0, msg, title, flags)
        
        user_choice = responses.get(result_code, "Desconhecido")
        self.result_label.configure(text=f"Última Resposta: {user_choice}")

        if user_choice in ["OK", "Sim"] and self.action_entry.get():
            try:
                subprocess.Popen(self.action_entry.get(), shell=True)
            except Exception as e:
                print(f"Erro: {e}")

if __name__ == "__main__":
    app = WindowsErrorApp()
    app.mainloop()