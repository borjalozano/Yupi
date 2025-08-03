# Nueva versión orientada a galería para el lote completo
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Lote Completo de Juegos Yupi", layout="wide")

st.title("🧸 Lote Completo de Juegos Yupi en Venta")
st.markdown(
    '<div style="max-width:800px;margin:auto;"><video controls autoplay muted loop width="100%">'
    '<source src="images/videoyupi.MP4" type="video/mp4">'
    'Tu navegador no soporta video HTML5.</video></div>',
    unsafe_allow_html=True
)
st.markdown("""
Venta única de todos los juegos en conjunto. Incluye más de 10 elementos profesionales importados, en buen estado general. Ideal para iniciar un negocio infantil, habilitar un espacio de entretención o ampliar una oferta comercial existente.
""")


# Información de los juegos (versión extendida)
juegos = [
    {
        "nombre": "Estructura Modular Multijuegos",
        "descripcion": "Gran estructura modular de juegos infantiles que incluye:\n- Piscina de pelotas (3,87 x 6 m), con 3 resbalines paralelos que desembocan en ella (2,35 m de ancho total)\n- Resbalín curvo (1,9 m ancho x 2,6 m alto)\n- Escalera trepadora (1,3 m ancho)\n- Jaula de globos con 4 ventiladores grandes superiores que hacen circular los globos\n- Laberinto ubicado bajo la jaula de globos (2,64 m ancho x 3 m alto x 3,8 m fondo)\n- Zona inferior con columpios. Ideal para áreas de juegos interiores de alto tráfico.\n- En el segundo piso incluye una escalera de hierro para colgarse, ideal para juego físico y coordinación.",
        "medidas": "930 x 600 x 300 cm",
        "fotos": [
            "IMG_1810", "IMG_1811", "IMG_1812", "IMG_1813",
            "IMG_1817", "IMG_1818", "IMG_1819", "IMG_1820",
            "IMG_1828", "IMG_1822", "IMG_1823", "IMG_1824",
            "IMG_1826", "IMG_1827", "IMG_1821"
        ]
    },
    {
        "nombre": "Túnel Cuncuna Plástico",
        "descripcion": "Estructura de túnel modular con forma de cuncuna, de plástico resistente, colores vivos, ideal para gateo y juego de exploración.",
        "medidas": "380 x 100 x 110 cm (aprox)",
        "fotos": ["IMG_1798", "IMG_1799", "IMG_1808", "IMG_1797"]
    },
    {
        "nombre": "Palmera Giratoria con Bolas",
        "descripcion": "Juego giratorio de estructura acolchada en forma de palmera con bolas colgantes para que los niños se sujeten y giren. Apto para interiores.",
        "medidas": "270 cm diámetro x 245 cm alto",
        "fotos": ["IMG_1795", "IMG_1796", "IMG_1780"]
    },
    {
        "nombre": "Carrusel Ardilla Soft",
        "descripcion": "Carrusel blando con figuras de ardillas y otros animales sobre base circular giratoria. Material acolchado, seguro para niños pequeños.",
        "medidas": "195 cm diámetro",
        "fotos": ["IMG_1793"]
    },
    {
        "nombre": "Helicóptero Inflable Infantil",
        "descripcion": "Juego inflable acolchado con forma de helicóptero, con cabina frontal y hélices decorativas. Su forma llamativa lo convierte en un excelente punto para juegos simbólicos.",
        "medidas": "270 x 180 x 190 cm",
        "fotos": ["IMG_1911", "IMG_1912"]
    },
    {
        "nombre": "Piano Musical Gigante",
        "descripcion": "Piano musical gigante que se toca con los pies. Estimula el ritmo y el movimiento, ideal para juegos creativos.",
        "medidas": "245 x 122 cm",
        "fotos": ["IMG_1800"]
    },
    {
        "nombre": "Arco de Bienvenida Selvático",
        "descripcion": "Arco decorativo temático con forma de árbol y animales de la selva, usado como entrada principal a la zona de juegos.",
        "medidas": "242 x 217 cm",
        "fotos": ["IMG_1779"]
    },
    {
        "nombre": "Zapateros Plásticos Infantiles (x2)",
        "descripcion": "Dos zapateros plásticos bajos, ideales para almacenar calzado infantil en la entrada del recinto.",
        "medidas": "100 x 50 x 27 cm (c/u)",
        "fotos": ["IMG_1804", "IMG_1805"]
    },
    {
        "nombre": "Nubes Decorativas de Espuma (x24)",
        "descripcion": "Conjunto de 24 nubes colgantes blancas de espuma liviana, ideales para ambientación aérea y decoración temática.",
        "medidas": "30–40 cm de ancho (cada una)",
        "fotos": ["IMG_1829", "IMG_1830", "IMG_1831"]
    },
    {
        "nombre": "Mesas de Cumpleaños y Sillas (x5 + x35)",
        "descripcion": "Cinco mesas plásticas rectangulares con 35 sillas infantiles coloridas. Resistentes y fáciles de limpiar.",
        "medidas": "Mesas: 90 x 60 x 50 cm",
        "fotos": ["IMG_1806", "IMG_1807", "IMG_1857"]
    }
]

for juego in juegos:
    if juego["nombre"] == "Nubes Decorativas de Espuma (x24)":
        st.markdown("## Nubes Decorativas de Espuma (x24)")
        st.markdown("**Descripción:** Conjunto de 24 nubes colgantes blancas de espuma liviana, ideales para ambientación aérea y decoración temática.")
        st.markdown("**Medidas:** 30–40 cm de ancho (cada una)")
        cols = st.columns(3)
        with cols[0]:
            img = Image.open("images/IMG_1829.jpeg").transpose(Image.ROTATE_90)
            img = img.resize((300, int(img.height * (300 / img.width))))
            st.image(img)
        with cols[1]:
            img = Image.open("images/IMG_1830.jpeg")
            img = img.resize((300, int(img.height * (300 / img.width))))
            st.image(img)
        with cols[2]:
            img = Image.open("images/IMG_1831.jpeg").transpose(Image.ROTATE_270)
            img = img.resize((300, int(img.height * (300 / img.width))))
            st.image(img)
    else:
        st.markdown(f"## {juego['nombre']}")
        st.markdown(f"**Descripción:** {juego['descripcion']}")
        st.markdown(f"**Medidas:** {juego['medidas']}")

        fotos = juego['fotos']
        for i in range(0, len(fotos), 4):
            cols = st.columns(4)
            for j, foto in enumerate(fotos[i:i+4]):
                with cols[j]:
                    path = f"images/{foto.strip()}.jpeg"
                    img = Image.open(path)
                    img = img.resize((300, int(img.height * (300 / img.width))))
                    st.image(img)

# --- Sección Otros juegos menores ---
st.markdown("## Otros juegos menores")
st.markdown("**Descripción:** Estos juegos complementarios aportan variedad y diversión adicional. Ideales para primeros juegos de equilibrio y coordinación.")

st.markdown("**Balancines Plásticos Individuales (x8) y Ballena Roja (x1)**")
cols = st.columns([1, 0.01, 1])

with cols[0]:
    img = Image.open("images/IMG_1802.jpeg")
    img = img.resize((300, int(img.height * (300 / img.width))))
    st.image(img)

with cols[2]:
    img = Image.open("images/IMG_1801.jpeg")
    img = img.resize((300, int(img.height * (300 / img.width))))
    st.image(img)