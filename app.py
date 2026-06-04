
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Feliz cumpleaños Lyly", page_icon="🎂", layout="centered")

html = """
<style>
body {
    background: linear-gradient(135deg, #ffe4f2, #e9ddff, #dbeafe);
}

.titulo {
    text-align: center;
    font-size: 48px;
    color: #d63384;
    font-weight: bold;
    margin-top: 20px;
}

.frase {
    text-align: center;
    font-size: 26px;
    color: #6f42c1;
    margin-bottom: 25px;
}

.mago {
    text-align: center;
    font-size: 115px;
    animation: flotar 2s ease-in-out infinite;
}

.tarjeta {
    background: rgba(255,255,255,0.90);
    border-radius: 28px;
    padding: 28px;
    text-align: center;
    color: #831843;
    font-size: 22px;
    line-height: 1.6;
    box-shadow: 0px 8px 28px rgba(0,0,0,0.18);
    margin: 25px auto;
    max-width: 680px;
}

.firework {
    position: fixed;
    font-size: 38px;
    animation: explotar 1.4s infinite alternate;
    z-index: 999;
}

.f1 { top: 8%; left: 12%; }
.f2 { top: 12%; right: 12%; animation-delay: .3s; }
.f3 { bottom: 18%; left: 15%; animation-delay: .6s; }
.f4 { bottom: 15%; right: 15%; animation-delay: .9s; }
.f5 { top: 45%; left: 5%; animation-delay: 1.2s; }
.f6 { top: 45%; right: 5%; animation-delay: 1.5s; }

@keyframes flotar {
    0% { transform: translateY(0px) rotate(-2deg); }
    50% { transform: translateY(-18px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(-2deg); }
}

@keyframes explotar {
    from { transform: scale(0.7); opacity: 0.4; }
    to { transform: scale(1.5); opacity: 1; }
}
</style>

<div class="firework f1">🎆</div>
<div class="firework f2">🎇</div>
<div class="firework f3">✨</div>
<div class="firework f4">💫</div>
<div class="firework f5">🎉</div>
<div class="firework f6">🌟</div>

<div class="titulo">🎂 Feliz cumpleaños, Lyly 🎂</div>
<div class="frase">Hoy el universo se puso modo fiesta solo por ti, Lyly ✨</div>

<div class="mago">🧙‍♂️🪄⚡</div>

<div class="tarjeta">
Que este nuevo año venga cargado de magia, sonrisas bonitas y momentos que brillen más que cualquier hechizo.
<br><br>
Que cada sueño que guardas en tu corazón encuentre el momento perfecto para hacerse realidad.
<br><br>
💖 Feliz cumpleaños, Lyly 💖
</div>
"""

components.html(html, height=650)

st.markdown(
    "<h2 style='text-align:center; color:#6f42c1;'>🎵 Música de cumpleaños</h2>",
    unsafe_allow_html=True
)

st.video("cumple.mp4")

st.markdown(
    "<h2 style='text-align:center; color:#6f42c1;'>📸 Recuerdos bonitos</h2>",
    unsafe_allow_html=True
)

st.image("lyly3.jpg.png", caption="✨ Nuestra versión mágica ✨", use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("lyly1.jpg", caption="💖", use_container_width=True)

with col2:
    st.image("lyly2.jpg", caption="🎂", use_container_width=True)

if st.button("💌 Mensaje secreto"):
    st.success("Eres única, increíble y mágica. Nunca lo olvides, Lyly 💖✨")

st.balloons()
