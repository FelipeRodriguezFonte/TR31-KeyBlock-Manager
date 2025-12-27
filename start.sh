#!/bin/bash
# TR-31 Key Block Manager - Launcher para Linux/macOS

echo "🔐 TR-31 Key Block Manager"
echo "======================================"
echo ""

# Verificar que existe tr31_gui.py
if [ ! -f "tr31_gui.py" ]; then
    echo "❌ ERROR: tr31_gui.py no encontrado"
    echo "Por favor ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

# Verificar versión de Python
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python $PYTHON_VERSION detectado"

# Verificar si existe un entorno virtual
if [ -d "venv" ]; then
    echo "📦 Activando entorno virtual..."
    source venv/bin/activate
else
    echo "⚠️  No se encontró entorno virtual"
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Entorno virtual creado"
fi

# Verificar e instalar dependencias
echo "📋 Verificando dependencias..."
pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ ERROR: No se pudieron instalar las dependencias"
    exit 1
fi

echo "✅ Dependencias instaladas"
echo ""
echo "🚀 Iniciando TR-31 Manager..."
echo ""

# Ejecutar la aplicación
python tr31_gui.py

# Guardar el código de salida
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ La aplicación terminó con errores"
    exit $EXIT_CODE
fi

exit 0
