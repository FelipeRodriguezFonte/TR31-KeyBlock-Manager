#!/usr/bin/env python3
"""
TR-31 Key Block Manager - Versión Completa
Una interfaz gráfica moderna para trabajar con TR-31 key blocks
"""

import customtkinter as ctk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import psec.tr31 as tr31
from tkinter import messagebox
import traceback

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Diccionario completo de Key Usage
KEY_USAGE_OPTIONS = {
    "B0": "BDK - Base Derivation Key",
    "B1": "Initial DUKPT Key",
    "B2": "Base Key Variant",
    "C0": "CVK - Card Verification Key",
    "D0": "Data Encryption (Symmetric)",
    "D1": "Data Encryption (Asymmetric)",
    "D2": "Data Encryption (Decimalization Table)",
    "E0": "EMV/Chip Issuer Master Key",
    "E1": "EMV/Chip Issuer Master Key (ICC)",
    "E2": "EMV/Chip Issuer Master Key (SMI)",
    "E3": "EMV/Chip Issuer Master Key (SMC)",
    "E4": "EMV/Chip Issuer Master Key (DAC)",
    "E5": "EMV/Chip Issuer Master Key (DN)",
    "E6": "EMV/Chip Issuer Master Key (APP)",
    "I0": "Initialization Vector (IV)",
    "K0": "Key Encryption/Wrapping",
    "K1": "TR-31 KBPK",
    "K2": "TR-34 Asymmetric KBPK",
    "K3": "Asymmetric Key for Key Agreement",
    "M0": "ISO 16609 MAC Algorithm 1",
    "M1": "ISO 9797-1 MAC Algorithm 1",
    "M2": "ISO 9797-1 MAC Algorithm 2",
    "M3": "ISO 9797-1 MAC Algorithm 3",
    "M4": "ISO 9797-1 MAC Algorithm 4",
    "M5": "ISO 9797-1 MAC Algorithm 5",
    "M6": "ISO 9797-1 MAC Algorithm 6",
    "M7": "HMAC",
    "M8": "ISO 9797-1 MAC Algorithm 6",
    "P0": "PIN Encryption",
    "P1": "PIN Generation Key (ANSI X9.132)",
    "S0": "Asymmetric Signature",
    "S1": "Asymmetric Signature with CA",
    "S2": "Asymmetric Signature (no hash)",
    "V0": "PIN Verification (KPV, PVV)",
    "V1": "PIN Verification (PVV, CVV)",
    "V2": "CVV Card Verification",
    "00": "Key Usage Not Available",
}

# Version ID options
VERSION_OPTIONS = {
    "D": "AES Key Derivation (Recomendado)",
    "B": "TDES Key Derivation (Recomendado)",
    "A": "TDES Key Variant (Deprecated)",
    "C": "TDES Key Variant"
}

# Algorithm options
ALGORITHM_OPTIONS = {
    "A": "AES",
    "T": "Triple DES (TDES)",
    "D": "DES (No Recomendado)",
    "R": "RSA"
}

# Mode options
MODE_OPTIONS = {
    "B": "Both - Cifrar y Descifrar",
    "E": "Encrypt - Solo Cifrar",
    "D": "Decrypt - Solo Descifrar",
    "C": "Both - Generar y Verificar",
    "G": "Generate - Solo Generar",
    "V": "Verify - Solo Verificar",
    "X": "Key Derivation - Derivación",
    "Y": "Create Variant - Crear Variante"
}

# Exportability options
EXPORT_OPTIONS = {
    "E": "Exportable",
    "N": "Not Exportable - No Exportable",
    "S": "Sensitive - Solo bajo KEK"
}

# Presets
PRESETS = {
    "AES Data Encryption": {"version": "D", "usage": "D0", "algo": "A", "mode": "B", "vernum": "00", "export": "E"},
    "TDES Data Encryption": {"version": "B", "usage": "D0", "algo": "T", "mode": "B", "vernum": "00", "export": "E"},
    "PIN Encryption (AES)": {"version": "D", "usage": "P0", "algo": "A", "mode": "E", "vernum": "00", "export": "N"},
    "PIN Encryption (TDES)": {"version": "B", "usage": "P0", "algo": "T", "mode": "E", "vernum": "00", "export": "N"},
    "MAC Generation (HMAC)": {"version": "D", "usage": "M7", "algo": "A", "mode": "G", "vernum": "00", "export": "E"},
    "MAC Generation (TDES)": {"version": "B", "usage": "M1", "algo": "T", "mode": "C", "vernum": "00", "export": "E"},
    "CVV/CVK": {"version": "B", "usage": "C0", "algo": "T", "mode": "C", "vernum": "00", "export": "N"},
    "Key Wrapping (AES)": {"version": "D", "usage": "K0", "algo": "A", "mode": "B", "vernum": "00", "export": "E"},
    "DUKPT BDK": {"version": "B", "usage": "B0", "algo": "T", "mode": "X", "vernum": "00", "export": "S"},
}


class TR31App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("TR-31 Key Block Manager")
        self.geometry("1300x950")  # Aumentado de 850 a 950
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Título
        ctk.CTkLabel(
            main_frame,
            text="🔐 TR-31 Key Block Manager - Versión Completa",
            font=ctk.CTkFont(size=24, weight="bold")
        ).grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # TabView
        self.tabview = ctk.CTkTabview(main_frame)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.tabview.add("🔍 Validar")
        self.tabview.add("📋 Decodificar")
        self.tabview.add("✨ Generar")
        
        self.setup_validate_tab()
        self.setup_decode_tab()
        self.setup_generate_tab()
        
        # Tema
        theme_frame = ctk.CTkFrame(main_frame)
        theme_frame.grid(row=2, column=0, padx=20, pady=(10, 20))
        
        ctk.CTkSegmentedButton(
            theme_frame,
            values=["🌙 Oscuro", "☀️ Claro", "💻 Sistema"],
            command=self.change_theme
        ).pack()
    
    def change_theme(self, value):
        mode = {"🌙 Oscuro": "dark", "☀️ Claro": "light", "💻 Sistema": "system"}
        ctk.set_appearance_mode(mode[value])
    
    def setup_validate_tab(self):
        tab = self.tabview.tab("🔍 Validar")
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(2, weight=1)
        
        # Info
        ctk.CTkLabel(
            tab,
            text="Valida un TR-31 key block y extrae la clave protegida",
            font=ctk.CTkFont(size=14)
        ).grid(row=0, column=0, padx=20, pady=20)
        
        # Inputs
        input_frame = ctk.CTkFrame(tab)
        input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(input_frame, text="KBPK (hex):", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=20, pady=10, sticky="w")
        self.val_kbpk = ctk.CTkEntry(input_frame)
        self.val_kbpk.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        
        ctk.CTkLabel(input_frame, text="TR-31 Key Block:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=20, pady=10, sticky="w")
        self.val_kb = ctk.CTkEntry(input_frame)
        self.val_kb.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        
        ctk.CTkButton(
            input_frame,
            text="🔓 Validar",
            command=self.validate_fn,
            height=35
        ).grid(row=2, column=0, columnspan=2, pady=15)
        
        # Resultado con más espacio
        self.val_result = ctk.CTkTextbox(tab, font=ctk.CTkFont(family="Courier", size=12))
        self.val_result.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    
    def setup_decode_tab(self):
        tab = self.tabview.tab("📋 Decodificar")
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(2, weight=1)
        
        ctk.CTkLabel(
            tab,
            text="Decodifica la cabecera de un TR-31 key block",
            font=ctk.CTkFont(size=14)
        ).grid(row=0, column=0, padx=20, pady=20)
        
        input_frame = ctk.CTkFrame(tab)
        input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(input_frame, text="Cabecera/Key Block:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=20, pady=10, sticky="w")
        self.dec_header = ctk.CTkEntry(input_frame)
        self.dec_header.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        
        ctk.CTkButton(
            input_frame,
            text="🔍 Decodificar",
            command=self.decode_fn,
            height=35
        ).grid(row=1, column=0, columnspan=2, pady=15)
        
        self.dec_result = ctk.CTkTextbox(tab, font=ctk.CTkFont(family="Courier", size=12))
        self.dec_result.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    
    def setup_generate_tab(self):
        tab = self.tabview.tab("✨ Generar")
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(3, weight=2)  # Más peso para el área de resultados
        
        # Info
        ctk.CTkLabel(
            tab,
            text="Genera un TR-31 key block. Selecciona un preset o configura manualmente.",
            font=ctk.CTkFont(size=14)
        ).grid(row=0, column=0, padx=20, pady=15)
        
        # Container principal - reducido un poco en altura
        container = ctk.CTkFrame(tab)
        container.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        
        # Izquierda: Presets y Claves
        left = ctk.CTkFrame(container)
        left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(left, text="⚡ Preset", font=ctk.CTkFont(size=13, weight="bold")).pack(pady=5)
        self.preset_var = ctk.StringVar(value="Seleccionar...")
        ctk.CTkOptionMenu(
            left,
            variable=self.preset_var,
            values=["Seleccionar..."] + list(PRESETS.keys()),
            command=self.load_preset
        ).pack(padx=10, pady=5, fill="x")
        
        ctk.CTkLabel(left, text="🔑 KBPK (hex)", font=ctk.CTkFont(size=13, weight="bold")).pack(pady=(15, 2))
        ctk.CTkLabel(left, text="Clave que protege el TR-31", 
                    font=ctk.CTkFont(size=10), text_color="gray").pack()
        self.gen_kbpk = ctk.CTkEntry(left, height=35)
        self.gen_kbpk.pack(padx=10, pady=5, fill="x")
        
        ctk.CTkLabel(left, text="🔑 Clave a proteger (hex)", font=ctk.CTkFont(size=13, weight="bold")).pack(pady=(15, 2))
        ctk.CTkLabel(left, text="Clave que será encriptada", 
                    font=ctk.CTkFont(size=10), text_color="gray").pack()
        self.gen_key = ctk.CTkEntry(left, height=35)
        self.gen_key.pack(padx=10, pady=5, fill="x")
        
        # Derecha: Parámetros
        right = ctk.CTkFrame(container)
        right.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(right, text="📋 Parámetros TR-31", font=ctk.CTkFont(size=13, weight="bold")).pack(pady=5)
        
        params = ctk.CTkScrollableFrame(right, height=280)  # Altura fija menor
        params.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Version ID
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Version ID:", width=120).pack(side="left", padx=5)
        
        version_opts = [f"{k} - {v}" for k, v in VERSION_OPTIONS.items()]
        self.gen_version_var = ctk.StringVar(value="D - AES Key Derivation (Recomendado)")
        self.gen_version = ctk.CTkOptionMenu(row, variable=self.gen_version_var, 
                                              values=version_opts, width=300)
        self.gen_version.pack(side="left", padx=5, fill="x", expand=True)
        
        # Key Usage
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Key Usage:", width=120).pack(side="left", padx=5)
        
        usage_opts = [f"{k} - {v}" for k, v in KEY_USAGE_OPTIONS.items()]
        self.gen_usage_var = ctk.StringVar(value="D0 - Data Encryption (Symmetric)")
        self.gen_usage = ctk.CTkOptionMenu(row, variable=self.gen_usage_var, 
                                           values=usage_opts, width=300)
        self.gen_usage.pack(side="left", padx=5, fill="x", expand=True)
        
        # Algorithm
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Algorithm:", width=120).pack(side="left", padx=5)
        
        algo_opts = [f"{k} - {v}" for k, v in ALGORITHM_OPTIONS.items()]
        self.gen_algo_var = ctk.StringVar(value="A - AES")
        self.gen_algo = ctk.CTkOptionMenu(row, variable=self.gen_algo_var, 
                                          values=algo_opts, width=300)
        self.gen_algo.pack(side="left", padx=5, fill="x", expand=True)
        
        # Mode
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Mode of Use:", width=120).pack(side="left", padx=5)
        
        mode_opts = [f"{k} - {v}" for k, v in MODE_OPTIONS.items()]
        self.gen_mode_var = ctk.StringVar(value="B - Both - Cifrar y Descifrar")
        self.gen_mode = ctk.CTkOptionMenu(row, variable=self.gen_mode_var, 
                                          values=mode_opts, width=300)
        self.gen_mode.pack(side="left", padx=5, fill="x", expand=True)
        
        # Version Num
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Version Num:", width=120).pack(side="left", padx=5)
        self.gen_vernum = ctk.CTkEntry(row, width=80)
        self.gen_vernum.insert(0, "00")
        self.gen_vernum.pack(side="left", padx=5)
        ctk.CTkLabel(row, text="(Usualmente 00)", 
                    font=ctk.CTkFont(size=10), text_color="gray").pack(side="left", padx=5)
        
        # Exportability
        row = ctk.CTkFrame(params, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text="Exportability:", width=120).pack(side="left", padx=5)
        
        export_opts = [f"{k} - {v}" for k, v in EXPORT_OPTIONS.items()]
        self.gen_export_var = ctk.StringVar(value="E - Exportable")
        self.gen_export = ctk.CTkOptionMenu(row, variable=self.gen_export_var, 
                                            values=export_opts, width=300)
        self.gen_export.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón generar
        ctk.CTkButton(
            tab,
            text="✨ Generar TR-31 Key Block",
            command=self.generate_fn,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=2, column=0, pady=10)
        
        # Resultado - MUCHO MÁS ESPACIO
        result_frame = ctk.CTkFrame(tab)
        result_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure(1, weight=1)
        
        header = ctk.CTkFrame(result_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=(10, 0))
        
        ctk.CTkLabel(header, text="🎉 Resultado", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkButton(header, text="📋 Copiar", command=self.copy_result, width=100).pack(side="right")
        
        # Textbox con scroll automático y altura expandible
        self.gen_result = ctk.CTkTextbox(
            result_frame, 
            font=ctk.CTkFont(family="Courier", size=11), 
            wrap="none"
        )
        self.gen_result.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="nsew")
    
    def load_preset(self, name):
        if name == "Seleccionar...":
            return
        p = PRESETS[name]
        
        # Establecer los valores con descripción completa
        self.gen_version_var.set(f"{p['version']} - {VERSION_OPTIONS[p['version']]}")
        self.gen_usage_var.set(f"{p['usage']} - {KEY_USAGE_OPTIONS[p['usage']]}")
        self.gen_algo_var.set(f"{p['algo']} - {ALGORITHM_OPTIONS[p['algo']]}")
        self.gen_mode_var.set(f"{p['mode']} - {MODE_OPTIONS[p['mode']]}")
        self.gen_export_var.set(f"{p['export']} - {EXPORT_OPTIONS[p['export']]}")
        
        self.gen_vernum.delete(0, "end")
        self.gen_vernum.insert(0, p["vernum"])
        
        self.gen_kbpk.focus()
        messagebox.showinfo("Preset Cargado", f"Configuración: {name}\n\nAhora introduce las claves.")
    
    def copy_result(self):
        text = self.gen_result.get("1.0", "end")
        for line in text.split("\n"):
            if "TR-31 Key Block:" in line:
                kb = text.split(line)[1].split("\n")[1].strip()
                if kb:
                    win = ctk.CTkToplevel(self)
                    win.title("Copiar")
                    win.geometry("700x150")
                    ctk.CTkLabel(win, text="Selecciona y copia (Cmd+C / Ctrl+C):").pack(pady=10)
                    entry = ctk.CTkEntry(win, width=650)
                    entry.pack(pady=10)
                    entry.insert(0, kb)
                    entry.select_range(0, "end")
                    entry.focus()
                    ctk.CTkButton(win, text="Cerrar", command=win.destroy).pack(pady=10)
                    return
        messagebox.showwarning("No encontrado", "No hay key block para copiar")
    
    def validate_fn(self):
        try:
            self.val_result.delete("1.0", "end")
            kbpk_hex = self.val_kbpk.get().strip().replace(" ", "")
            kb_hex = self.val_kb.get().strip().replace(" ", "")
            
            if not kbpk_hex or not kb_hex:
                messagebox.showwarning("Vacío", "Completa todos los campos")
                return
            
            kbpk = bytes.fromhex(kbpk_hex)
            kb = tr31.KeyBlock(kbpk=kbpk)
            key = kb.unwrap(kb_hex)
            
            result = f"""✅ VALIDACIÓN EXITOSA
{'='*70}

📋 CABECERA
{'-'*70}
Version ID:     {kb.header.version_id}
Key Usage:      {kb.header.key_usage} - {KEY_USAGE_OPTIONS.get(kb.header.key_usage, 'Unknown')}
Algorithm:      {kb.header.algorithm}
Mode of Use:    {kb.header.mode_of_use}
Version Num:    {kb.header.version_num}
Exportability:  {kb.header.exportability}

🔑 RESULTADO
{'-'*70}
Clave Extraída: {key.hex().upper()}
"""
            self.val_result.insert("1.0", result)
        except Exception as e:
            self.val_result.insert("1.0", f"❌ ERROR\n\n{str(e)}\n\n{traceback.format_exc()}")
            messagebox.showerror("Error", str(e))
    
    def decode_fn(self):
        try:
            self.dec_result.delete("1.0", "end")
            h_input = self.dec_header.get().strip().replace(" ", "")
            
            if not h_input:
                messagebox.showwarning("Vacío", "Introduce una cabecera")
                return
            
            h = tr31.Header()
            h.load(h_input)
            
            result = f"""📋 CABECERA DECODIFICADA
{'='*70}

Version ID:     {h.version_id}
Key Usage:      {h.key_usage} - {KEY_USAGE_OPTIONS.get(h.key_usage, 'Unknown')}
Algorithm:      {h.algorithm}
Mode of Use:    {h.mode_of_use}
Version Num:    {h.version_num}
Exportability:  {h.exportability}

Cabecera:       {str(h)}
Longitud:       {len(str(h))} caracteres
"""
            self.dec_result.insert("1.0", result)
        except Exception as e:
            self.dec_result.insert("1.0", f"❌ ERROR\n\n{str(e)}\n\n{traceback.format_exc()}")
            messagebox.showerror("Error", str(e))
    
    def generate_fn(self):
        try:
            self.gen_result.delete("1.0", "end")
            kbpk_hex = self.gen_kbpk.get().strip().replace(" ", "")
            key_hex = self.gen_key.get().strip().replace(" ", "")
            
            if not kbpk_hex or not key_hex:
                messagebox.showwarning("Vacío", "Completa KBPK y la clave")
                return
            
            kbpk = bytes.fromhex(kbpk_hex)
            key = bytes.fromhex(key_hex)
            
            # Extraer códigos de los valores seleccionados
            version = self.gen_version_var.get().split(" - ")[0]
            usage = self.gen_usage_var.get().split(" - ")[0]
            algo = self.gen_algo_var.get().split(" - ")[0]
            mode = self.gen_mode_var.get().split(" - ")[0]
            export = self.gen_export_var.get().split(" - ")[0]
            
            h = tr31.Header(
                version_id=version,
                key_usage=usage,
                algorithm=algo,
                mode_of_use=mode,
                version_num=self.gen_vernum.get().strip(),
                exportability=export
            )
            
            kb = tr31.KeyBlock(kbpk=kbpk, header=h)
            keyblock = kb.wrap(key=key)
            
            result = f"""✅ KEY BLOCK GENERADO
{'='*80}

📋 CABECERA
{'-'*80}
Version ID:     {version} - {VERSION_OPTIONS[version]}
Key Usage:      {usage} - {KEY_USAGE_OPTIONS.get(usage, 'Unknown')}
Algorithm:      {algo} - {ALGORITHM_OPTIONS[algo]}
Mode of Use:    {mode} - {MODE_OPTIONS[mode]}
Version Num:    {h.version_num}
Exportability:  {export} - {EXPORT_OPTIONS[export]}

🎉 RESULTADO
{'-'*80}
TR-31 Key Block:
{keyblock.upper()}

📏 INFO
{'-'*80}
Longitud: {len(keyblock)} caracteres
"""
            self.gen_result.insert("1.0", result)
        except Exception as e:
            self.gen_result.insert("1.0", f"❌ ERROR\n\n{str(e)}\n\n{traceback.format_exc()}")
            messagebox.showerror("Error", str(e))


def main():
    app = TR31App()
    app.mainloop()


if __name__ == "__main__":
    main()
