# ML Boilerplate — Hola Mundo con Streamlit (para forks de CV / NLP / Media)

Base mínima en **Python + Streamlit** para iniciar proyectos de ML con interfaz visual y luego **forquear**:
- CV con YOLO
- NLP con Transformers
- Texto/Audio → Video

## Requisitos
- Python 3.10+
- (Opcional) Visual Studio Code + extensión Python

## Instalación rápida
```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Ejecutar (Hola Mundo)
```bash
make run-app
# o
streamlit run app/main_app.py
```

## Estructura mínima
```
ml-boilerplate/
├── app/main_app.py
├── config/base.yaml
├── utils/config.py
├── utils/device.py
├── data/.gitkeep
├── models/.gitkeep
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md
```

## Cómo forquear
1. Duplica este repo.
2. Agrega dependencias específicas (YOLO, Transformers, MoviePy, etc.).
3. Crea `tasks/<proyecto>/pipeline.py` con `run_pipeline(file, cfg)`.
4. Extiende `config/` con tu `<proyecto>.yaml`.
5. Modifica `app/main_app.py` para invocar tu pipeline.

¡Listo para construir!
