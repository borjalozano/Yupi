# Nueva versión orientada a galería para el lote completo
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Lote Completo de Juegos Yupi", layout="wide")

st.title("☕ Catálogo de Equipamiento y Mobiliario de Cafetería")


items_cafe = [
    {
        "nombre": "Lámparas colgantes industriales (x6)",
        "descripcion": "Seis lámparas industriales colgantes de plástico acanalado con luz cálida, ideales para zonas altas o techos industriales.",
        "medidas": "Ø50 cm aprox.",
        "fotos": ["IMG_1832.jpeg"],
        "precio_nuevo": 700000,
        "precio_venta": 250000
    },
    {
        "nombre": "Rieles energizados para focos LED (x3)",
        "descripcion": "Tres rieles metálicos energizados con instalación para focos LED, en color blanco, ideal para espacios de iluminación direccional.",
        "medidas": "2 m aprox. cada uno",
        "fotos": ["IMG_1834.jpeg", "IMG_1835.jpeg", "IMG_1836.jpeg"],
        "precio_nuevo": 180000,
        "precio_venta": 60000
    },
    {
        "nombre": "Aire acondicionado cassette KHONE (x4)",
        "descripcion": "Cuatro equipos de aire acondicionado tipo cassette marca KHONE, 220V, 50/60Hz, potencia 24.000 BTU. Para climatización interior.",
        "medidas": "60 x 60 cm (unidad visible)",
        "fotos": ["IMG_1837.jpeg", "IMG_1839.jpeg", "IMG_1840.jpeg", "IMG_1841.jpeg"],
        "precio_nuevo": 4800000,
        "precio_venta": 2600000
    },
    {
        "nombre": "Lámparas colgantes rojas (3 tríos + 4 individuales)",
        "descripcion": "Tres juegos de lámparas colgantes triples + cuatro individuales. Cúpulas de vidrio rojo en forma de esfera, ideales para cafetería o zona de barra.",
        "medidas": "Ø18 cm aprox. por lámpara",
        "fotos": ["IMG_1842.jpeg", "IMG_1843.jpeg", "IMG_1844.jpeg", "IMG_1845.jpeg"],
        "precio_nuevo": 480000,
        "precio_venta": 150000
    },
    {
        "nombre": "Cámaras de seguridad IP (x3)",
        "descripcion": "Tres cámaras IP domo con antenas WiFi, ideales para monitoreo de seguridad. Marca 2B Electrónica.",
        "medidas": "10 x 10 x 15 cm aprox.",
        "fotos": ["IMG_1846.jpeg", "IMG_1847.jpeg", "IMG_1848.jpeg"],
        "precio_nuevo": 90000,
        "precio_venta": 40000
    },
    {
        "nombre": "Extintores de polvo químico (x3)",
        "descripcion": "Tres extintores multipropósito de polvo químico, instalados y operativos, con soporte mural.",
        "medidas": "5 kg aprox. cada uno",
        "fotos": ["IMG_1852.jpeg", "IMG_1853.jpeg"],
        "precio_nuevo": 120000,
        "precio_venta": 50000
    },
    {
        "nombre": "Mudador portátil plegable",
        "descripcion": "Mudador plegable con superficie acolchada e ilustración infantil. Ideal para espacios reducidos o baños familiares.",
        "medidas": "80 x 50 x 90 cm aprox.",
        "fotos": ["IMG_1854.jpeg", "IMG_1856.jpeg"],
        "precio_nuevo": 50000,
        "precio_venta": 20000
    },
    {
        "nombre": "Dispensadores de papel (4 nova + 3 interfoliado)",
        "descripcion": "Cuatro dispensadores de toalla nova marca Elite y tres dispensadores de papel higiénico interfoliado marca Kimberly-Clark.",
        "medidas": "30 x 25 x 13 cm aprox.",
        "fotos": ["IMG_1860.jpeg", "IMG_1861.jpeg", "IMG_1865.jpeg", "IMG_1867.jpeg"],
        "precio_nuevo": 250000,
        "precio_venta": 100000
    },
    {
        "nombre": "Inodoros WC (x2)",
        "descripcion": "Dos inodoros blancos de cerámica compacta con sistema dual flush.",
        "medidas": "60 x 38 x 65 cm aprox.",
        "fotos": ["IMG_1862.jpeg", "IMG_1868.jpeg"],
        "precio_nuevo": 200000,
        "precio_venta": 80000
    },
    {
        "nombre": "Lavamanos con grifería (x2)",
        "descripcion": "Dos lavamanos de loza tipo bowl sobre cubierta, con grifería monomando.",
        "medidas": "Ø42 x 15 cm aprox.",
        "fotos": ["IMG_1863.jpeg", "IMG_1869.jpeg"],
        "precio_nuevo": 160000,
        "precio_venta": 70000
    },
    {
        "nombre": "Lámparas infantiles de techo (abeja) (x2)",
        "descripcion": "Dos lámparas decorativas infantiles con diseño de girasol y abeja en relieve, montaje de cielo.",
        "medidas": "Ø30 cm",
        "fotos": ["IMG_1871.jpeg", "IMG_1914.jpeg"],
        "precio_nuevo": 60000,
        "precio_venta": 20000
    },
    {
        "nombre": "Termo eléctrico ANWO 80L",
        "descripcion": "Calefón eléctrico ANWO modelo DSCF80-A22 de 80 litros, 220V, 1700W, fabricado en 2019, para agua caliente sanitaria.",
        "medidas": "Altura 105 cm, Ø40 cm",
        "fotos": ["IMG_1872.jpeg", "IMG_1873.jpeg"],
        "precio_nuevo": 320000,
        "precio_venta": 150000
    }
]

imagenes_disponibles = [
    "IMG_1832.jpeg", "IMG_1834.jpeg", "IMG_1835.jpeg", "IMG_1836.jpeg", "IMG_1837.jpeg", "IMG_1839.jpeg",
    "IMG_1840.jpeg", "IMG_1841.jpeg", "IMG_1842.jpeg", "IMG_1843.jpeg", "IMG_1844.jpeg", "IMG_1845.jpeg",
    "IMG_1846.jpeg", "IMG_1847.jpeg", "IMG_1848.jpeg", "IMG_1852.jpeg", "IMG_1853.jpeg", "IMG_1854.jpeg",
    "IMG_1856.jpeg", "IMG_1859.jpeg", "IMG_1860.jpeg", "IMG_1861.jpeg", "IMG_1862.jpeg", "IMG_1863.jpeg",
    "IMG_1865.jpeg", "IMG_1867.jpeg", "IMG_1868.jpeg", "IMG_1869.jpeg", "IMG_1871.jpeg", "IMG_1872.jpeg",
    "IMG_1873.jpeg", "IMG_1914.jpeg"
]

for item in items_cafe:
    fotos_filtradas = [foto for foto in item.get("fotos", []) if foto in imagenes_disponibles]
    item["fotos"] = fotos_filtradas

def obtener_precio_venta(item):
    if "precio_venta" in item:
        return item["precio_venta"]
    else:
        return -1

items_cafe = sorted(items_cafe, key=obtener_precio_venta, reverse=True)

for item in items_cafe:
    st.markdown(f"## {item['nombre']}")
    st.markdown(f"**Descripción:** {item['descripcion']}")
    st.markdown(f"**Medidas:** {item['medidas']}")
    if "precio_nuevo" in item:
        st.markdown(f"💰 Precio nuevo: ${item['precio_nuevo']:,.0f}")
    if "precio_venta" in item:
        st.markdown(f"🔻 Precio venta: ${item['precio_venta']:,.0f}")
    fotos = item.get("fotos", [])
    for i in range(0, len(fotos), 4):
        cols = st.columns(4)
        for j, foto in enumerate(fotos[i:i+4]):
            with cols[j]:
                path = f"images/accesorios/{foto}"
                img = Image.open(path)
                img = img.resize((300, int(img.height * (300 / img.width))))
                st.image(img)