@echo off
REM TR-31 Key Block Manager - Launcher para Windows

echo.
echo ====================================
echo  TR-31 Key Block Manager
echo ====================================
echo.

REM Verificar que existe tr31_gui.py
if not exist "tr31_gui.py" (
    echo ERROR: tr31_gui.py no encontrado
    echo Por favor ejecuta este script desde el directorio del proyecto
    pause
    exit /b 1
)

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python 3.8 o superior desde python.org
    pause
    exit /b 1
)

echo Python detectado
echo.

REM Verificar si existe un entorno virtual
if exist "venv\Scripts\activate.bat" (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
) else (
    echo No se encontro entorno virtual
    echo Creando entorno virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Entorno virtual creado
)

REM Instalar dependencias
echo.
echo Verificando dependencias...
pip install -q -r requirements.txt

if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo Dependencias instaladas
echo.
echo Iniciando TR-31 Manager...
echo.

REM Ejecutar la aplicación
python tr31_gui.py

REM Si hubo error, pausar para ver el mensaje
if errorlevel 1 (
    echo.
    echo La aplicacion termino con errores
    pause
    exit /b 1
)

exit /b 0
