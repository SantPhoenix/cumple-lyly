
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Feliz cumpleaños, bonita",
    page_icon="🎂",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
    body {
        margin: 0;
        padding: 0;
        overflow: hidden;
        font-family: 'Segoe UI', sans-serif;
        background: radial-gradient(circle at top, #ffe6f2, #f3e8ff, #dbeafe);
        height: 100vh;
    }

    .container {
        text-align: center;
        padding-top: 45px;
        color: #3b0764;
    }

    h1 {
        font-size: 48px;
        color: #d63384;
        text-shadow: 2px 2px 8px rgba(255,255,255,0.9);
        animation: aparecer 1.4s ease-in-out;
    }

    .frase {
        font-size: 27px;
        margin-top: 10px;
        color: #6f42c1;
        font-weight: 600;
        animation: aparecer 2s ease-in-out;
    }

    .mago {
        font-size: 120px;
        margin-top: 25px;
        animation: flotar 2s ease-in-out infinite;
    }

    .carta {
        display: inline-block;
        margin-top: 20px;
        padding: 18px 28px;
        border-radius: 24px;
        background: rgba(255,255,255,0.75);
        box-shadow: 0 8px 28px rgba(0,0,0,0.15);
        font-size: 22px;
        color: #831843;
        max-width: 520px;
        animation: aparecer 2.4s ease-in-out;
    }

    .sparkle {
        position: absolute;
        font-size: 28px;
        animation: brillar 2s linear infinite;
    }

    .s1 { top: 15%; left: 12%; animation-delay: 0s; }
    .s2 { top: 30%; left: 83%; animation-delay: .4s; }
    .s3 { top: 70%; left: 20%; animation-delay: .8s; }
    .s4 { top: 80%; left: 78%; animation-delay: 1.2s; }
    .s5 { top: 8%; left: 50%; animation-delay: 1.5s; }

    .heart {
        position: absolute;
        bottom: -40px;
        font-size: 24px;
        animation: subir 6s linear infinite;
        opacity: 0.75;
    }

    .h1 { left: 10%; animation-delay: 0s; }
    .h2 { left: 28%; animation-delay: 1s; }
    .h3 { left: 45%; animation-delay: 2s; }
    .h4 { left: 65%; animation-delay: 1.5s; }
    .h5 { left: 85%; animation-delay: .5s; }

    @keyframes flotar {
        0% { transform: translateY(0px) rotate(-2deg); }
        50% { transform: translateY(-18px) rotate(2deg); }
        100% { transform: translateY(0px) rotate(-2deg); }
    }

    @keyframes brillar {
        0% { opacity: .2; transform: scale(.7) rotate(0deg); }
        50% { opacity: 1; transform: scale(1.3) rotate(15deg); }
        100% { opacity: .2; transform: scale(.7) rotate(0deg); }
    }

    @keyframes subir {
        0% { transform: translateY(0); opacity: 0; }
        20% { opacity: .9; }
        100% { transform: translateY(-110vh); opacity: 0; }
    }

    @keyframes aparecer {
        from { opacity: 0; transform: translateY(25px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 600px) {
        h1 { font-size: 38px; }
        .frase { font-size: 22px; }
        .mago { font-size: 95px; }
        .carta { font-size: 19px; margin: 18px; }
    }
</style>
</head>
<body>
    <div class="sparkle s1">✨</div>
    <div class="sparkle s2">🌟</div>
    <div class="sparkle s3">✨</div>
    <div class="sparkle s4">💫</div>
    <div class="sparkle s5">⭐</div>

    <div class="heart h1">💖</div>
    <div class="heart h2">🎂</div>
    <div class="heart h3">💜</div>
    <div class="heart h4">🎉</div>
    <div class="heart h5">💖</div>

    <div class="container">
        <h1>🎂 Feliz cumpleaños, bonita 🎂</h1>
        <div class="frase">Hoy el universo se puso modo fiesta solo por ti, Lyly ✨ ✨</div>
        <div class="mago">🧙‍♂️🪄</div>
        <div class="carta">
            Que este nuevo año venga cargado de magia, sonrisas bonitas y dinero dinero para que me mantengas si.
        </div>
    </div>
</body>
</html>
"""

components.html(html, height=720)
st.balloons()
