import streamlit as st
import streamlit.components.v1 as components

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Sales Intelligence Dashboard",
    layout="wide"
)

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>
header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}
            
.hero-title {
    animation: floatText 6s ease-in-out infinite;
}

@keyframes floatText {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-6px);
    }

    100% {
        transform: translateY(0px);
    }
}  

/* MAIN BACKGROUND */
.stApp {
    background: transparent;
    color: white;
}

/* FULL PAGE STARFIELD */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background:
        radial-gradient(circle at 20% 20%, rgba(56,189,248,0.15), transparent 25%),
        radial-gradient(circle at 80% 30%, rgba(168,85,247,0.12), transparent 25%),
        radial-gradient(circle at 50% 80%, rgba(59,130,246,0.12), transparent 25%),
        #020617;

    z-index: -2;
}

/* ANIMATED STARS */
.stApp::after {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;

    background-image:
        radial-gradient(white 1px, transparent 1px);

    background-size: 50px 50px;

    opacity: 0.15;

    animation: moveStars 120s linear infinite;

    z-index: -1;
}

@keyframes moveStars {
    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(-2000px);
    }
}

/* REMOVE STREAMLIT PADDING */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* HERO TITLE */
.hero-title {
    font-size: 72px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(90deg, #ffffff, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

/* HERO SUBTEXT */
.hero-sub {
    font-size: 22px;
    color: #94a3b8;
    margin-bottom: 35px;
    max-width: 750px;
}

/* FEATURE CARDS */
.feature-card {
    background: rgba(15, 23, 42, 0.45);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 28px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    transition: 0.3s;
    height: 220px;
    backdrop-filter: blur(16px);
    box-shadow: 0 8px 40px rgba(0,0,0,0.35);
}

.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid #38bdf8;
    box-shadow: 0 0 25px rgba(56,189,248,0.35);
}

/* CARD TITLE */
.card-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 12px;
    color: white;
}

/* CARD TEXT */
.card-text {
    color: #94a3b8;
    line-height: 1.7;
    font-size: 15px;
}

/* BADGE */
.badge {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    background: rgba(56,189,248,0.12);
    border: 1px solid rgba(56,189,248,0.3);
    color: #38bdf8;
    font-size: 14px;
    margin-bottom: 25px;
}

/* SECTION SPACING */
.spacer {
    height: 60px;
}
.hero-title,
.hero-sub,
.badge {
    position: relative;
    z-index: 2;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HERO SECTION
# ======================================================

# ======================================================
# HERO SECTION
# ======================================================

hero_left, hero_right = st.columns([1.1, 1])

# ================= LEFT SIDE =================

with hero_left:

    st.markdown(
        """
        <div class="badge">
            AI-Powered Business Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
            Sales Intelligence<br>
            Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-sub">
            Transform raw business data into powerful executive insights,
            predictive analytics, and intelligent forecasting — all in one
            modern analytics workspace.
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= RIGHT SIDE =================

with hero_right:

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: transparent;
            }

            canvas {
                display: block;
            }
        </style>
    </head>

    <body>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <script>

    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
        75,
        500 / 600,
        0.1,
        1000
    );

    camera.position.z = 3;

    const renderer = new THREE.WebGLRenderer({
        antialias: true,
        alpha: true
    });
                    
    renderer.setClearColor(0x000000, 0);

    renderer.setSize(500, 600);

    document.body.appendChild(renderer.domElement);

    // GEOMETRY

    const geometry = new THREE.IcosahedronGeometry(1, 1);

    const material = new THREE.MeshStandardMaterial({
        color: 0x38bdf8,
        wireframe: true
    });

    const sphere = new THREE.Mesh(
        geometry,
        material
    );

    scene.add(sphere);

    // LIGHT

    const light = new THREE.PointLight(
        0xffffff,
        2
    );

    light.position.set(5,5,5);

    scene.add(light);

    // PARTICLES

    const particlesGeometry = new THREE.BufferGeometry();

    const particlesCount = 3000;

    const posArray = new Float32Array(
        particlesCount * 3
    );

    for(let i = 0; i < particlesCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 10;
    }

    particlesGeometry.setAttribute(
        'position',
        new THREE.BufferAttribute(posArray, 3)
    );

    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.015,
        color: 0x38bdf8
    });

    const particlesMesh = new THREE.Points(
        particlesGeometry,
        particlesMaterial
    );

    scene.add(particlesMesh);

    // ANIMATION

    function animate() {

        requestAnimationFrame(animate);

        sphere.rotation.x += 0.003;
        sphere.rotation.y += 0.004;

        particlesMesh.rotation.y += 0.0003;

        renderer.render(scene, camera);
    }

    animate();

    </script>

    </body>
    </html>
    """,
    height=600
    )

# ======================================================
# FEATURE CARDS
# ======================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
    <div class="card-title">
    Executive Overview
    </div>

    <div class="card-text">
    Monitor revenue, profit margins, customer trends,
    and regional performance through dynamic KPI analytics.
    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
    <div class="card-title">
    AI Analytics
    </div>

    <div class="card-text">
    Discover hidden patterns, customer behaviors,
    and sales intelligence powered by modern data analytics.
    </div>

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
    <div class="card-title">
    Forecast Engine
    </div>

    <div class="card-text">
    Predict future business growth and identify
    strategic opportunities with forecasting models.
    </div>

    </div>
    """, unsafe_allow_html=True)

# ======================================================
# SPACING
# ======================================================

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)


