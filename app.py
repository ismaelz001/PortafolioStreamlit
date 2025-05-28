import streamlit as st

import streamlit as st




col1 , col2 = st.columns([1,3])

def load_estilo(style):
    with open(style) as g:
        st.markdown(f"<style>{g.read()}</style>", unsafe_allow_html=True)


load_estilo("style.css")        


with col1:
    st.image("imgs/proAvatar.png", width=160)

# Inicializar el estado la primera vez
if "mostrar_sidebar" not in st.session_state:
    st.session_state.mostrar_sidebar = False

# Botón toggle: cambia el estado al hacer clic
if st.button("Más Sobre mí"):
    st.session_state.mostrar_sidebar = not st.session_state.mostrar_sidebar


if st.session_state.mostrar_sidebar:
    with st.sidebar:
    
        st.markdown("---")
        st.markdown("### 🎓 Formación")
        st.markdown("- Bootcamp Data Analytics (2024, Hack a Boss)")
        st.markdown("- CFGS Desarrollo Web (en curso)")
        st.markdown("- Técnico Big Data – CCC (2024)")

        st.markdown("---")
        st.markdown("### 🛠️ Habilidades")
        st.markdown("- Python, SQL, HTML, JS, PHP")
        st.markdown("- Pandas, NumPy, Seaborn")
        st.markdown("- Power BI, Tableau")
        st.markdown("- MongoDB, MySQL, PostgreSQL")
        st.markdown("- Git, Excel Avanzado")

        st.markdown("---")
        st.markdown("### 🚗 Otros")
        st.markdown("- Carnet y coche propio")
        st.markdown("- Disponibilidad para viajar")




st.title("Portafolio de Ismael Rodríguez")


with col2:
    st.markdown("### Ismael Rodríguez")
    st.markdown("*Analista de Datos Junior*")
    st.markdown("📧 rodriguezortegaismael@gmail.com")
    st.markdown("🔗 [GitHub](https://github.com/ismaelz001)")
    st.markdown("📍 Boiro, A Coruña")


# Sección de proyectos
st.subheader("📁 Proyectos destacados")

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="proyecto-box">
            <h4>🛒 <a href='https://github.com/ismaelz001/Proyecto-Final-Bootcamp' target='_blank'>E-commerce PCComponentes</a></h4>
            <p>Proyecto final del bootcamp. Simulación de e-commerce con análisis de productos, categorías y visualizaciones.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="proyecto-box">
            <h4>🏘️ <a href='https://github.com/ismaelz001/Particulares_Scraper' target='_blank'>Scraper Idealista</a></h4>
            <p>Web scraper automatizado para obtener precios de viviendas de particulares en Idealista y análisis posterior de tendencias.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="proyecto-box">
            <h4>☀️ <a href='https://github.com/ismaelz001/App-Tiempo' target='_blank'>App del Tiempo - DAW</a></h4>
            <p>Aplicación web simple desarrollada con tecnologías del DAW, conectada a API meteorológica en tiempo real.</p>
        </div>
        """, unsafe_allow_html=True)



st.divider()

# Footer
st.markdown("""
📫 ¿Quieres contactar conmigo?  
Puedes escribirme en [LinkedIn](https://www.linkedin.com/in/ismael-rodriguez-b6155165/)

---

© 2025 Ismael Rodríguez
""")
