# 📦 Guía de Instalación - TR-31 Key Block Manager

Esta guía te ayudará a instalar y ejecutar TR-31 Key Block Manager en tu sistema.

## 📋 Requisitos del Sistema

- **Sistema Operativo**: Windows 10+, macOS 10.14+, o Linux (Ubuntu 20.04+, Fedora 34+)
- **Python**: 3.8 o superior
- **RAM**: 512 MB mínimo
- **Espacio en disco**: 100 MB

---

## 🪟 Windows

### Paso 1: Instalar Python

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. **IMPORTANTE**: Marca la opción "Add Python to PATH"
3. Completa la instalación

### Paso 2: Verificar la Instalación

Abre PowerShell o CMD y ejecuta:
```cmd
python --version
```

Deberías ver algo como `Python 3.11.x`

### Paso 3: Descargar el Proyecto

```cmd
git clone https://github.com/FelipeRodriguezFonte/TR31-KeyBlock-Manager.git
cd TR31-KeyBlock-Manager
```

O descarga el ZIP desde GitHub y extráelo.

### Paso 4: Instalar Dependencias

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 5: Ejecutar

```cmd
python tr31_gui.py
```

O simplemente:
```cmd
start.bat
```

---

## 🍎 macOS

### Paso 1: Instalar Python

macOS incluye Python, pero es mejor instalar una versión actualizada:

**Opción A: Homebrew (Recomendado)**
```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python@3.11
```

**Opción B: Desde python.org**
1. Descarga desde [python.org](https://www.python.org/downloads/)
2. Ejecuta el instalador .pkg

### Paso 2: Verificar la Instalación

```bash
python3 --version
```

### Paso 3: Descargar el Proyecto

```bash
git clone https://github.com/FelipeRodriguezFonte/TR31-KeyBlock-Manager.git
cd TR31-KeyBlock-Manager
```

### Paso 4: Instalar Dependencias

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 5: Ejecutar

```bash
python tr31_gui.py
```

O simplemente:
```bash
chmod +x start.sh
./start.sh
```

---

## 🐧 Linux

### Paso 1: Instalar Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip tk
```

### Paso 2: Verificar la Instalación

```bash
python3 --version
```

### Paso 3: Descargar el Proyecto

```bash
git clone https://s.com/FelipeRodriguezFonte/TR31-KeyBlock-Manager.git
cd TR31-KeyBlock-Manager
```

### Paso 4: Instalar Dependencias

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 5: Ejecutar

```bash
python tr31_gui.py
```

O simplemente:
```bash
chmod +x start.sh
./start.sh
```

---

## 🔧 Solución de Problemas

### Error: "python: command not found"

**Windows:**
- Reinstala Python marcando "Add to PATH"

**macOS/Linux:**
- Usa `python3` en lugar de `python`

### Error: "No module named 'customtkinter'"

```bash
pip install customtkinter
```

### Error: "No module named 'tkinter'"

**Ubuntu/Debian:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python-tk@3.11
```

### La ventana no se abre

**Linux:** Asegúrate de tener un servidor X o Wayland corriendo

**WSL (Windows Subsystem for Linux):**
- Instala un servidor X como VcXsrv
- O usa WSLg (Windows 11)

### Error: "Permission denied" (macOS/Linux)

```bash
chmod +x start.sh
```

---

## 🎯 Verificar la Instalación

Una vez instalado, deberías ver:

1. Ventana principal con 3 pestañas
2. Título: "🔐 TR-31 Key Block Manager - Versión Completa"
3. Selector de tema en la parte inferior

**Prueba rápida:**
1. Ve a la pestaña "✨ Generar"
2. Selecciona preset "AES Data Encryption"
3. Introduce claves de prueba
4. Clic en "Generar TR-31 Key Block"

---

## 📚 Próximos Pasos

- Lee el [README.md](README.md) para conocer todas las funcionalidades
- Prueba los diferentes presets
- Revisa la documentación de TR-31 en el README

---

## 🆘 ¿Necesitas Ayuda?

Si encuentras problemas:

1. Revisa los [Issues](../../issues) existentes
2. Crea un nuevo issue con:
   - Sistema operativo
   - Versión de Python
   - Mensaje de error completo
   - Pasos que seguiste

---

**¡Disfruta usando TR-31 Key Block Manager!** 🎉
