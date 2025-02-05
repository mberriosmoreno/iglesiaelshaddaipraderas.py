import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Iglesia El Shaddai",
    page_icon="⛪",
    layout="centered",
)

# Título principal
st.title("Bienvenido")
st.markdown("### Iglesia El Shaddai Praderas")

# Agregar imagen del logotipo
st.image("logo.png", use_column_width=True)  # Reemplaza "logo.png" con el nombre de tu archivo de imagen

# Sección de visión
st.markdown("---")  # Línea divisoria
st.markdown("### **Visión**")
st.markdown(
    """
    Edificar familias que tengan como fundamento amor, fe y esperanza en Dios, creyendo que lo que hacemos aquí en la tierra tiene un impacto en el cielo.
    """
)

# Menú de navegación
menu = st.radio("Navegación", options=["Inicio", "Reuniones", "Liderazgo", "Cumpleaños", "Literatura"])

# Contenido de las secciones
if menu == "Inicio":
    st.write("Estás en la sección de Inicio.")
elif menu == "Reuniones":
    st.write("Información sobre las reuniones.")
elif menu == "Liderazgo":
    st.write("Detalles sobre el liderazgo de la iglesia.")
elif menu == "Cumpleaños":
    st.write("Aquí se mostrarán los cumpleaños de la comunidad.")
elif menu == "Literatura":
    st.write("Acceso a recursos literarios.")

# Agregar estilo personalizado con CSS
st.markdown(
    """
    <style>
        .css-18e3th9 {
            background-color: #f4f4f4;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton button {
            background-color: #0070C0;
            color: white;
            border-radius: 10px;
        }
        .stButton button:hover {
            background-color: #FFC107;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
