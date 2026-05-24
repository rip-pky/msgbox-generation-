import tkinter as tk
import customtkinter as ctk
import os
import platform
from tkinter import messagebox
import os

def show_native_macos_alert(title, message):
    """Usa AppleScript para um visual ainda mais nativo que o Tkinter."""
    script = f'display alert "{title}" message "{message}" as critical buttons {{"OK"}}'
    os.system(f"osascript -e '{script}'")
def check_os_fallback():
    if platform.system() != "Darwin":
        root = ctk.CTk()
        root.withdraw()
        messagebox.showerror("Fallback", f"Use o script de {platform.system()}. macOS não detectado.")
        exit()

def show_tkinter_mac():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("macOS Security", "Unsupported architecture detected.")
    root.destroy()
check_os_fallback()

class MacErrorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("macOS Error Suite")
        self.geometry("600x650")

        ctk.CTkLabel(self, text="AppleScript Alert Generator", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)
        
        self.tabview = ctk.CTkTabview(self, width=550)
        self.tabview.pack(padx=20, pady=10)
        
        self.tab_alert = self.tabview.add("AppleScript")
        self.tab_toast = self.tabview.add("Notifications")

        self.setup_ui()

    def setup_ui(self):
        self.t_entry = ctk.CTkEntry(self.tab_alert, placeholder_text="Título...", width=450)
        self.t_entry.pack(pady=10)
        self.m_entry = ctk.CTkEntry(self.tab_alert, placeholder_text="Corpo...", width=450)
        self.m_entry.pack(pady=10)

        ctk.CTkButton(self.tab_alert, text="LANÇAR ALERT NATIVO", command=self.run_mac).pack(pady=20)
        
        ctk.CTkButton(self.tab_toast, text="NOTIFICAÇÃO AQUA", 
                      command=self.run_toast).pack(pady=20)

        # Botão Agendar para Mac
        ctk.CTkButton(self.tab_alert, text="CUSTOM 'SCHEDULE' BUTTON", 
                      command=self.mac_schedule, fg_color="#333").pack(pady=5)

    def run_mac(self):
        t, m = self.t_entry.get(), self.m_entry.get()
        script = f'display dialog "{m}" with title "{t}" buttons {{"Cancelar", "OK"}} default button "OK"'
        os.system(f"osascript -e '{script}'")

    def run_toast(self):
        t, m = self.t_entry.get(), self.m_entry.get()
        script = f'display notification "{m}" with title "{t}"'
        os.system(f"osascript -e '{script}'")

    def mac_schedule(self):
        win = ctk.CTkToplevel(self)
        ctk.CTkLabel(win, text="Deseja agendar?").pack(pady=20)
        ctk.CTkButton(win, text="Agendar", command=win.destroy).pack()

if __name__ == "__main__":
    # Tenta usar o AppleScript para fidelidade total
    show_native_macos_alert("System Update", "Your Mac requires a restart to finish updates.")
    # show_tkinter_mac() # Alternativa caso prefira o Tkinter
    app = MacErrorApp()
    app.mainloop()