import streamlit as st

# Cargar CSS externo
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Menú lateral tipo TD Hopper
menu = st.sidebar.selectbox("Navegación", ["Inicio", "Archivo", "Notas para un analista", "Currículum", "Proyectos"])

# Inicio
if menu == "Inicio":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("imgs/fotoPro.jpeg", width=180)  # Asegúrate de tener esta imagen en la carpeta imgs

    with col2:
        st.title("Ismael Rodríguez")
        st.markdown("""
        Analista de Datos Junior con formación técnica sólida en desarrollo web (**CFGS DAW**) y especialización intensiva en análisis de datos a través del **Bootcamp de Data Analytics** en Hack a Boss.

        Me enfoco en transformar datos en soluciones, con experiencia en Python, SQL, herramientas de visualización (Power BI, Tableau) y bases de datos tanto relacionales como no relacionales.

        Actualmente en continuo crecimiento, combinando mis conocimientos en desarrollo y análisis para construir soluciones integrales, desde la extracción de datos hasta su presentación visual.
        """)

        st.markdown("""
        **📍 Boiro, A Coruña**  
        📧 [rodriguezortegaismael@gmail.com](mailto:rodriguezortegaismael@gmail.com)  
        🔗 [GitHub](https://github.com/ismaelz001) | [LinkedIn](https://www.linkedin.com/in/ismael-rodriguez-b6155165/)
        """)

    st.markdown("---")
    st.subheader("💡 Este sitio recopila:")
    st.markdown("- Proyectos personales y académicos")
    st.markdown("- Reflexiones y artículos sobre análisis de datos")
    st.markdown("- Recursos y presentaciones sobre herramientas que utilizo")


# Archivo 
elif menu == "Archivo":
    st.title("Reflexiones Proyectos")
    st.markdown("Por ahora este espacio mostrará futuras reflexiones y análisis relacionados con datos y tecnología.")
    st.markdown("#### 🏘️ Scraper Idealista")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("imgs/viviendas.png", use_container_width=True)

    with col2:
        st.markdown("""
        Trabajar en este scraper de Idealista me permitió profundizar en la automatización de extracción de datos web, enfocándome en identificar vendedores particulares de viviendas.

        Aprendí a manejar estructuras HTML dinámicas, optimizar el filtrado de información útil (como teléfonos y nombres), y organizar los datos por localidad para generar insights comerciales relevantes.

        Este tipo de soluciones puede marcar la diferencia para agentes inmobiliarios que buscan captar clientes directos.
        """)

    st.markdown("---")

    # Proyecto 2: E-commerce PCComponentes
    st.markdown("#### 🛒 E-commerce PCComponentes")
    col3, col4 = st.columns([1, 2])

    with col3:
        st.image("imgs/ecomerce.png", use_container_width=True)

    with col4:
        st.markdown("""
        Durante este proyecto aprendí a desarrollar una solución completa de análisis de datos en el sector eCommerce, desde la extracción y limpieza de información hasta la visualización de insights a través de dashboards.

        Apliqué técnicas de clustering y clasificación para segmentar productos, diseñé bases de datos relacionales eficientes y creé una aplicación interactiva con Streamlit.

        Esta experiencia me permitió consolidar conocimientos técnicos, mejorar el trabajo en equipo y entender la importancia de crear herramientas útiles tanto para usuarios finales como para clientes estratégicos.
        """)



elif menu == "Notas para un analista":
    st.title("🧠 Ideas & Recursos")

    st.markdown("Este espacio lo uso para compartir aprendizajes rápidos, recursos interesantes, impresiones sobre el sector del dato y consejos personales que me han sido útiles.")

    st.markdown("---")

    st.subheader("📌 Por qué aprender SQL sigue siendo esencial")
    st.markdown("""
    Aunque hoy todo el mundo habla de Python, frameworks y modelos complejos, dominar **SQL** sigue siendo una de las habilidades más valoradas y prácticas en el día a día del analista.

    Yo lo uso para:
    - Validar datos de origen rápidamente
    - Hacer auditorías en bases relacionales
    - Armar prototipos de dashboards

    No lo subestimes: muchos perfiles se caen en entrevistas por no tener una buena base en esto.
    """)

    st.subheader("🔍 ¿Qué está pasando con la IA en analítica?")
    st.markdown("""
    Herramientas como ChatGPT, Claude o Gemini están ayudando a escribir código, documentar, explicar resultados. Pero **no reemplazan el criterio humano**.

    Lo importante hoy:
    - Saber usar IA como copiloto, no como piloto automático
    - Validar todo lo que genera
    - Integrarla en tus procesos, pero no depender ciegamente
    """)

    st.subheader("📚 Lecturas recomendadas")
    st.markdown("""
    - *Storytelling with Data* – Cole Nussbaumer
    - *Data Science for Business* – Provost & Fawcett
    - *Designing Data-Intensive Applications* – Martin Kleppmann
    """)



elif menu == "Currículum":
    st.title("📄 Currículum Profesional")

    st.markdown("""
    ### 🎓 Formación Académica
    - **Bootcamp en Data Analytics** – Hack a Boss (2024)  
      Formación intensiva en análisis de datos con enfoque en Python, SQL, visualización y manejo de datos reales.
    
    - **CFGS Desarrollo de Aplicaciones Web (DAW)** – En curso  
      Aprendizaje de tecnologías frontend (HTML, CSS, JS) y backend (PHP, MySQL), junto con fundamentos sólidos de programación web.

    - **Curso Técnico en Big Data** – CCC (2024)  
      Enfoque en ecosistemas Big Data, introducción a Hadoop, bases de datos NoSQL y herramientas de almacenamiento y análisis masivo.
    """)

    st.markdown("### 🛠️ Herramientas y Lenguajes")

    st.markdown("""
    **Lenguajes y Programación**  
    Python · SQL · HTML · CSS · JavaScript · PHP

    **Análisis y Visualización**  
    Pandas · NumPy · Seaborn · Matplotlib · Power BI · Tableau · Streamlit

    **Bases de Datos**  
    MySQL · PostgreSQL · MongoDB

    **Otras herramientas**  
    Git · GitHub · Excel Avanzado · Web Scraping · APIs
    """)

    st.markdown("📄 Puedes consultar o descargar el CV completo en PDF:")
    #st.markdown("[Descargar Currículum (PDF)](https://github.com/ismaelz001/PortafolioStreamlit/blob/main/Curr%C3%ADculum%20Vitae%20.pdf)")

    st.markdown("[Descargar CV (PDF)](https://github.com/ismaelz001/PortafolioStreamlit/blob/main/Curr%C3%ADculum%20Vitae%20.pdf)")

# Proyectos
elif menu == "Proyectos":
    st.title("Proyectos Personales")
    st.markdown("- [Scraper de Particulares en Idealista](https://github.com/ismaelz001/Particulares_Scraper)")
    st.markdown("- [App del Tiempo (HTML+JS)](https://github.com/ismaelz001/App-Tiempo)")
    st.markdown("- [E-commerce Análisis – Bootcamp Final](https://github.com/ismaelz001/Proyecto-Final-Bootcamp)")

# Footer
st.markdown("<footer style='margin-top: 50px; font-size: 0.8rem; color: gray;'>© 2025 Ismael Rodríguez · Construido con Streamlit</footer>", unsafe_allow_html=True)
