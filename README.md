# 🔐 TR-31 Key Block Manager

Una interfaz gráfica moderna para trabajar con TR-31 key blocks según el estándar ANSI X9.143.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Características

- **Validar**: Desencripta TR-31 key blocks y extrae la clave protegida
- **Decodificar**: Analiza y muestra información detallada de cabeceras TR-31
- **Generar**: Crea TR-31 key blocks con configuración personalizada o presets
- **40+ Key Usage Types**: Implementación completa de la especificación TR-31
- **9 Presets Predefinidos**: Configuraciones rápidas para casos de uso comunes
- **Interfaz Autoexplicativa**: Todos los parámetros incluyen descripciones claras
- **Temas**: Modo oscuro, claro o según el sistema

## 📸 Capturas de Pantalla

### Pestaña de Generación
La interfaz muestra todos los parámetros TR-31 con sus descripciones:
- Version ID, Key Usage, Algorithm, Mode of Use, Exportability
- 9 presets predefinidos para configuración rápida
- Área de resultados expandible con scroll

### Casos de Uso
- **Educación**: Perfecto para enseñar TR-31 en cursos de criptografía
- **Testing**: Generar y validar key blocks sin herramientas comerciales
- **Desarrollo**: Integración y pruebas de sistemas criptográficos

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Windows

```cmd
# Clonar el repositorio
git clone https://github.com/FelipeRodriguezFonte/TR31-KeyBlock-Manager.git
cd TR31-KeyBlock-Manager

# Crear entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python tr31_gui.py
```

### macOS / Linux

```bash
# Clonar el repositorio
git clone https://github.com/FelipeRodriguezFonte/TR31-KeyBlock-Manager.git
cd TR31-KeyBlock-Manager

# Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python tr31_gui.py
```

### Ejecutar sin Instalación (Linux/macOS)

```bash
chmod +x start.sh
./start.sh
```

### Ejecutar sin Instalación (Windows)

```cmd
start.bat
```

## 📋 Uso

### Generar un TR-31 Key Block

1. Abre la pestaña "✨ Generar"
2. Selecciona un preset (ej: "CVV/CVK") o configura manualmente
3. Introduce:
   - **KBPK** (hex): Clave que protege el TR-31
   - **Clave a proteger** (hex): Clave que será encriptada
4. Clic en "✨ Generar TR-31 Key Block"
5. El resultado aparecerá en el área de abajo
6. Usa "📋 Copiar" para copiar el key block generado

### Validar un TR-31 Key Block

1. Abre la pestaña "🔍 Validar"
2. Introduce:
   - **KBPK** (hex): Clave que protege el TR-31
   - **TR-31 Key Block**: El key block completo
3. Clic en "🔓 Validar"
4. El resultado mostrará la clave extraída y la información de la cabecera

### Decodificar una Cabecera

1. Abre la pestaña "📋 Decodificar"
2. Introduce la cabecera o el key block completo
3. Clic en "🔍 Decodificar"
4. El resultado mostrará todos los campos decodificados

## 🎓 Presets Disponibles

| Preset | Version | Key Usage | Algorithm | Descripción |
|--------|---------|-----------|-----------|-------------|
| AES Data Encryption | D (AES) | D0 | AES | Cifrado de datos genérico |
| TDES Data Encryption | B (TDES) | D0 | TDES | Cifrado de datos legacy |
| PIN Encryption (AES) | D (AES) | P0 | AES | Cifrado de PIN moderno |
| PIN Encryption (TDES) | B (TDES) | P0 | TDES | Cifrado de PIN legacy |
| MAC Generation (HMAC) | D (AES) | M7 | AES | HMAC-SHA |
| MAC Generation (TDES) | B (TDES) | M1 | TDES | MAC ISO 9797-1 |
| CVV/CVK | B (TDES) | C0 | TDES | Verificación de tarjetas |
| Key Wrapping (AES) | D (AES) | K0 | AES | Envolver otras claves |
| DUKPT BDK | B (TDES) | B0 | TDES | Base Derivation Key |

## 📚 Documentación TR-31

Este proyecto implementa el estándar **ANSI X9.143** para TR-31 Key Blocks, que especifica:

- **Version ID**: Tipo de binding (AES/TDES derivation o variant)
- **Key Usage**: Propósito de la clave (40+ tipos soportados)
- **Algorithm**: AES, TDES, DES, RSA
- **Mode of Use**: Encrypt, Decrypt, Generate, Verify, etc.
- **Exportability**: E (Exportable), N (No exportable), S (Sensitive)

### Key Usage Types Soportados

- **B0-B2**: DUKPT (Base Derivation Key, Initial DUKPT, Base Key Variant)
- **C0**: CVK (Card Verification Key)
- **D0-D2**: Data Encryption (Symmetric, Asymmetric, Decimalization Table)
- **E0-E6**: EMV/Chip Issuer Master Keys
- **I0**: Initialization Vector
- **K0-K3**: Key Encryption/Wrapping
- **M0-M8**: MAC algorithms (incluye HMAC)
- **P0-P1**: PIN Encryption y Generation
- **S0-S2**: Asymmetric Signature
- **V0-V2**: PIN/Card Verification

## 🏗️ Estructura del Proyecto

```
TR31-KeyBlock-Manager/
├── tr31_gui.py           # Aplicación principal
├── requirements.txt      # Dependencias (customtkinter y psec)
├── start.sh             # Launcher para Linux/macOS
├── start.bat            # Launcher para Windows
├── README.md            # Este archivo
└── .gitignore           # Archivos a ignorar en Git
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación
- **CustomTkinter**: Framework moderno para interfaz gráfica
- **psec**: Librería para operaciones TR-31 (instalada desde PyPI)

## 🙏 Créditos

Este proyecto utiliza la librería **psec** desarrollada por [Konstantin Novichikhin](https://github.com/knovichikhin).

- **Repositorio psec**: https://github.com/knovichikhin/psec
- **PyPI**: https://pypi.org/project/psec/
- **Agradecimiento especial** a Konstantin por su excelente implementación del estándar TR-31

La librería psec se instala automáticamente desde PyPI al ejecutar `pip install -r requirements.txt`.

La interfaz gráfica (tr31_gui.py) fue desarrollada para facilitar el uso educativo y profesional de la librería psec.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

La librería `psec` tiene su propia licencia - consulta el [repositorio original](https://github.com/knovichikhin/psec) para más información.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🐛 Reportar Issues

Si encuentras un bug o tienes una sugerencia:

1. Verifica que no exista un issue similar
2. Crea un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Sistema operativo y versión de Python
   - Screenshots si es relevante

## 📮 Contacto

- **Autor**: Felipe Rodríguez Fonte
- **Email**: felipe.rodriguez.fonte@gmail.com
- **GitHub**: [@FelipeRodriguezFonte](https://github.com/FelipeRodriguezFonte)

## ⭐ Star History

Si este proyecto te resulta útil, considera darle una estrella ⭐

---

**Desarrollado con ❤️ para la comunidad de criptografía y seguridad**
