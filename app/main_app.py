import streamlit as st
from utils.config import load_config
from utils.device import get_device, set_seed

st.set_page_config(page_title="ML Boilerplate — Hola Mundo", layout="centered")

cfg = load_config("config/base.yaml")
set_seed(cfg.get("seed", 42))
device = get_device(cfg.get("device", "auto"))

st.title("👋 Hola Mundo — ML Boilerplate")
st.write("Base mínima para forks de CV / NLP / Media con UI en Streamlit.")

with st.expander("Configuración actual"):
    st.json(cfg)

st.info(f"Dispositivo (etiqueta): **{device}**")

st.subheader("Sube un archivo de prueba (imagen / texto / audio)")
file = st.file_uploader("Selecciona un archivo", type=None)

if file is not None:
    st.write(f"**Nombre:** {file.name}")
    if file.type.startswith("image/"):
        st.image(file, caption="Vista previa", use_column_width=True)
    elif file.type.startswith("text/"):
        try:
            st.text_area("Contenido", file.getvalue().decode("utf-8")[:2000], height=200)
        except Exception:
            st.warning("No se pudo decodificar el archivo de texto.")
    elif file.type.startswith("audio/"):
        st.audio(file)
    else:
        st.write("Tipo no reconocido para vista previa. En los forks podrás procesarlo.")

st.divider()
st.caption("En tus forks, conecta run_pipeline(...) y tu lógica específica de proyecto.")
