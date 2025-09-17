# Proyecto RAG – Implementación con LangChain + Chroma + OpenAI

Este repositorio contiene la implementación de un sistema **RAG (Retrieval-Augmented Generation)** en entorno local con Python 3.11, gestionado con Anaconda/PyCharm y desplegado en CI/CD usando GitHub Actions.

## 🚀 Objetivo
Aprender y demostrar cómo funciona un sistema RAG paso a paso:  
- Ingesta de documentos (PDF)  
- Chunking del texto  
- Generación de embeddings  
- Almacenamiento vectorial en ChromaDB  
- Recuperación semántica  
- Generación de respuestas con grounding usando OpenAI  

---

## ⚙️ Tecnologías utilizadas
- **Python 3.11**
- [LangChain](https://www.langchain.com/)
- [LangChain Community](https://python.langchain.com/docs/modules/community/)
- [LangChain Chroma](https://docs.trychroma.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI API](https://platform.openai.com/)
- [PyPDF](https://pypi.org/project/pypdf/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pytest](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 📂 Estructura del proyecto

RAG_Env/
├── RETO_RAG.ipynb           # Notebook principal (implementación RAG)
├── requirements.txt         # Dependencias del proyecto
├── tests/                   # Carpeta de pruebas unitarias
│   └── test_rag_smoke.py    # Smoke test con embeddings “mock”
├── docs/                    # PDFs de ejemplo
├── .env                     # Variables de entorno (API Key, ignorado en git)
├── .gitignore               # Archivos/carpetas a ignorar en git
└── .github/workflows/ci.yml # CI mínimo con GitHub Actions


---

## 📝 Historial de Prompts y Aprendizajes

### Etapa 1 – Primeras preguntas
- *“Comportate como un estudiante que inicia en el desarrollo con IA Generativa. Realízame las preguntas necesarias antes de responder.”*  
- *“La actividad que deseo que realices se encuentra en el documento adjunto.”*  

👉 Aquí se definió el objetivo del proyecto: implementar un sistema RAG y documentarlo.

---

### Etapa 2 – Implementación en Notebook
- *“Paso 3 – Implementación del sistema RAG dentro del archivo RETO_RAG.ipynb con una versión clara y ejecutable en tu entorno local (Anaconda).”*  
- *“Me puedes dar los pasos para complementar el punto 3 de mi archivo entregable.”*  
- *“Me puedes generar nuevamente el archivo RETO_RAG.”*  

👉 Se construyó el notebook con chunks, embeddings, vectorstore y pipeline RAG.

---

### Etapa 3 – Instalación y errores en dependencias
- *“Estoy usando PyCharm, al instalar pip install langchain ... me da OSError: No space left on device.”*  
- *“ModuleNotFoundError: No module named 'langchain_community'.”*  
- *“Me actualizas el RETO_RAG y el archivo requirements para la versión 3.11.”*  

👉 Se solucionaron problemas de dependencias y compatibilidad con Python 3.11.

---

### Etapa 4 – Pruebas locales
- *“¿Cómo realizo la carga de variable con comando antes del paso 0?”*  
- *“ChromaDB inicializada en: .chroma_db_local … LangChainDeprecationWarning …”*  
- *“Ya me está funcionando, puedo subirte el notebook para que me desarrolles el punto 3 del documento para entrega?”*  

👉 Se ajustó la persistencia automática de ChromaDB y se validó la ejecución end-to-end.

---

### Etapa 5 – Configuración de CI/CD
- *“Quiero pasar al punto 4. Configuración de CI/CD con GitHub Actions.”*  
- *“Si, incluyamos pruebas unitarias.”*  
- *“Solo 1 test.”*  

👉 Se creó `test_rag_smoke.py` con embeddings dummy y se configuró workflow mínimo en GitHub Actions.

---

### Etapa 6 – Seguridad y manejo de secretos
- *“Me está marcando este error: Push Blocked: Secret Detected.”*  
- *“¿Cómo hago para que funcione con .env?”*  
- *“¿Me puedes crear el archivo .env?”*  

👉 Se aprendió a manejar variables de entorno con `.env`, `python-dotenv` y GitHub Secrets, evitando exponer claves en el repo.

---

## ✅ Próximos pasos
- Extender las pruebas unitarias (`pytest`) para validar ingestión de PDFs y chunking.  
- Ampliar el workflow de GitHub Actions para ejecutar el notebook completo con `papermill` y guardar artefactos.  
- Probar despliegue del sistema RAG en un microservicio Flask/FastAPI.  

---

## 🔒 Notas de seguridad
- El archivo `.env` con la clave de OpenAI está **ignorado en git** (`.gitignore`).  
- En GitHub Actions, se debe configurar `OPENAI_API_KEY` en **Settings → Secrets and variables → Actions**.  

---

## 👤 Autor
Mauricio Rochín  

---
