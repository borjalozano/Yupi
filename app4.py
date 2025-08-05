# Nueva versión orientada a galería para el lote completo
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Lote Completo de Juegos Yupi", layout="wide")

st.title("☕ Catálogo de Equipamiento y Mobiliario de Cafetería")
st.markdown("""
Este catálogo incluye el mobiliario, equipamiento y utensilios completos de una cafetería operativa. Todo se vende únicamente como un lote completo.
""")


items_cafe = [
    {
        "nombre": "Banquetas Altas Metálicas Amarillas (x8)",
        "descripcion": "Conjunto de ocho banquetas altas con estructura metálica y asiento amarillo, ideales para barras y espacios de cafetería.",
        "medidas": "Altura estándar para barras",
        "precio_nuevo": 240000,
        "precio_venta": 100000,
        "fotos": ["IMG_1849.jpeg", "IMG_1850.jpeg", "IMG_1851.jpeg"]
    },
    {
        "nombre": "Lote Vajilla y Utensilios de Café",
        "descripcion": "Set completo que incluye vajilla, utensilios, servilleteros y porta menús para atención en cafetería.",
        "medidas": "Variedad de tamaños estándar",
        "precio_nuevo": 200000,
        "precio_venta": 85000,
        "fotos": ["IMG_1874.jpeg", "IMG_1887.jpeg", "IMG_1888.jpeg", "IMG_1883.jpeg", "IMG_1889.jpeg"]
    },
    {
        "nombre": "Lavaplatos Industrial Acero Inoxidable",
        "descripcion": "Lavaplatos industrial con capacidad para uso intensivo en cafetería. Incluye sistema de secado y fácil manejo.",
        "medidas": "80 x 60 x 85 cm",
        "precio_nuevo": 180000,
        "precio_venta": 80000,
        "fotos": ["IMG_1875.jpeg"]
    },
    {
        "nombre": "Lavaplatos Secundario con Llave Alta",
        "descripcion": "Segundo lavaplatos industrial, ideal para complementar el área de lavado con alta eficiencia.",
        "medidas": "75 x 65 x 90 cm",
        "precio_nuevo": 150000,
        "precio_venta": 40000,
        "fotos": ["IMG_1876.jpeg"]
    },
    {
        "nombre": "Refrigerador Vertical Whirlpool",
        "descripcion": "Refrigerador vertical con puertas de vidrio, ideal para exhibición y conservación de bebidas y productos perecibles.",
        "medidas": "60 x 60 x 180 cm",
        "precio_nuevo": 350000,
        "precio_venta": 200000,
        "fotos": ["IMG_1877.jpeg", "IMG_1878.jpeg"]
    },
    {
        "nombre": "Electrodomésticos de Barra (lote conjunto)",
        "descripcion": "Incluye horno eléctrico, hervidor, licuadora con jarra de vidrio y microondas. Todos en funcionamiento, ideales para cafetería operativa. Se venden solo juntos.",
        "medidas": "Tamaños estándar. Se entrega como lote.",
        "precio_nuevo": 300000,
        "precio_venta": 140000,
        "fotos": ["IMG_1879.jpeg", "IMG_1880.jpeg", "IMG_1881.jpeg", "IMG_1882.jpeg"]
    },
    {
        "nombre": "Sistema Punto de Venta Completo (POS)",
        "descripcion": "Sistema POS completo con pantalla táctil, impresora de tickets y cajón de dinero. Listo para uso inmediato.",
        "medidas": "Equipo compacto",
        "precio_nuevo": 280000,
        "precio_venta": 100000,
        "fotos": ["IMG_1884.jpeg", "IMG_1885.jpeg", "IMG_1900.jpeg", "IMG_1901.jpeg"]
    },
    {
        "nombre": "Mini Componente Philips DVD DCD2030",
        "descripcion": "Equipo de música con altavoces y mezcladora, ideal para ambientar la cafetería o eventos.",
        "medidas": "Sistema portátil",
        "precio_nuevo": 140000,
        "precio_venta": 60000,
        "fotos": ["IMG_1886.jpeg"]
    },
    {
        "nombre": "Vitrina Refrigerada Curva Calvac",
        "descripcion": "Vitrina curva marca Calvac, con sistema de refrigeración para mantención de productos de pastelería, snacks o sándwiches. Tres niveles de exhibición con iluminación interior. Solo 6 meses de uso.",
        "medidas": "120 x 120 x 70 cm",
        "precio_nuevo": 1280000,
        "precio_venta": 1000000,
        "fotos": ["IMG_1890.jpeg", "IMG_1891.jpeg", "IMG_1892.jpeg"]
    },
    {
        "nombre": "8 Mesas Cuadradas de Cubierta Wersalit Marca Thonet",
        "descripcion": "Superficie compuesta por múltiples capas de recubrimiento de resina de melamina resistente al exterior y a los rayos UV.",
        "medidas": "70 x 70 x 75 cm (aprox.)",
        "precio_nuevo": 4500000,
        "precio_venta": 1400000,
        "fotos": ["IMG_1893.jpeg", "IMG_1894.jpeg", "IMG_1895.jpeg"]
    },
    {
        "nombre": "Sillas Tolix Amarillas (x10)",
        "descripcion": "Diez sillas metálicas estilo Tolix, resistentes y con acabado industrial para cafetería o terraza.",
        "medidas": "45 x 45 x 85 cm",
        "precio_nuevo": 350000,
        "precio_venta": 180000,
        "fotos": ["IMG_1896.jpeg", "IMG_1897.jpeg"]
    },
    {
        "nombre": "Set Lounge: 4 Sillones y 2 Mesas Redondas",
        "descripcion": "Conjunto de muebles lounge que incluye cuatro sillones y dos mesas redondas, perfecto para áreas de descanso y espera.",
        "medidas": "Sillones y mesas de tamaño estándar",
        "precio_nuevo": 600000,
        "precio_venta": 300000,
        "fotos": ["IMG_1898.jpeg"]
    },
    {
        "nombre": "Sillas Altas para Bebés (x2)",
        "descripcion": "Dos sillas altas para bebés con cinturón de seguridad y estructura estable, ideales para familias con niños pequeños.",
        "medidas": "Estándar para bebés",
        "precio_nuevo": 140000,
        "precio_venta": 50000,
        "fotos": ["IMG_1899.jpeg"]
    },
    {
        "nombre": "Máquina de Popcorn Industrial",
        "descripcion": "Máquina para preparar popcorn, ideal para eventos y espacios recreativos dentro de la cafetería.",
        "medidas": "40 x 40 x 50 cm",
        "precio_nuevo": 150000,
        "precio_venta": 75000,
        "fotos": ["IMG_1902.jpeg", "IMG_1903.jpeg"]
    },
    {
        "nombre": "Módulo Principal Café (Curvo + Recto)",
        "descripcion": "Mueble de atención principal con diseño curvo y recto, con vitrina integrada para productos secos y repisas interiores. Cubierta superior de apoyo. Estructura laminada color wengue con detalles verdes. + 3 muebles accesorios del mismo juego de 1,2 de largo x 1,5 de alto y 40 de ancho",
        "medidas": "Largo total: 315 cm. Curva: 156 x 80 x 106 cm / Recto: 160 x 62 x 106 cm",
        "precio_nuevo": 2000000,
        "precio_venta": 850000,
        "fotos": ["IMG_1904.jpeg", "IMG_1905.jpeg", "IMG_1906.jpeg", "IMG_1907.jpeg", "IMG_1908.jpeg", "IMG_1909.jpeg", "IMG_1910.jpeg"]
    }
]

imagenes_disponibles = [
    "IMG_1849.jpeg", "IMG_1850.jpeg", "IMG_1851.jpeg",
    "IMG_1874.jpeg", "IMG_1875.jpeg", "IMG_1876.jpeg", "IMG_1877.jpeg", "IMG_1878.jpeg", "IMG_1879.jpeg",
    "IMG_1880.jpeg", "IMG_1881.jpeg", "IMG_1882.jpeg", "IMG_1883.jpeg", "IMG_1884.jpeg", "IMG_1885.jpeg", "IMG_1886.jpeg",
    "IMG_1887.jpeg", "IMG_1888.jpeg", "IMG_1889.jpeg",
    "IMG_1890.jpeg", "IMG_1891.jpeg", "IMG_1892.jpeg", "IMG_1893.jpeg", "IMG_1894.jpeg", "IMG_1895.jpeg", "IMG_1896.jpeg", "IMG_1897.jpeg", "IMG_1898.jpeg", "IMG_1899.jpeg",
    "IMG_1900.jpeg", "IMG_1901.jpeg", "IMG_1902.jpeg", "IMG_1903.jpeg", "IMG_1904.jpeg", "IMG_1905.jpeg", "IMG_1906.jpeg", "IMG_1907.jpeg", "IMG_1908.jpeg", "IMG_1909.jpeg",
    "IMG_1910.jpeg"
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
    # if "precio_nuevo" in item:
    #     st.markdown(f"💰 Precio nuevo: ${item['precio_nuevo']:,.0f}")
    # if "precio_venta" in item:
    #     st.markdown(f"🔻 Precio venta: ${item['precio_venta']:,.0f}")
    fotos = item.get("fotos", [])
    for i in range(0, len(fotos), 4):
        cols = st.columns(4)
        for j, foto in enumerate(fotos[i:i+4]):
            with cols[j]:
                path = f"images/cafe/{foto}"
                img = Image.open(path)
                img = img.resize((300, int(img.height * (300 / img.width))))
                st.image(img)