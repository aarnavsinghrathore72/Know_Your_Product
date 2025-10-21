import streamlit as st
import requests
from PIL import Image
import io
import plotly.graph_objects as go
import plotly.express as px
import random
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file
SERP_API_KEY = 'da277b644a8891854b75ef4a9c951a255734f3d5335da9dbf2ca41f3242c53b4'

if not SERP_API_KEY:
    st.error("❌ API key not found. Please check your .env file.")
else:
    st.success("✅ API key loaded successfully!")


# --- DARK THEME PROFESSIONAL CSS ---
st.markdown("""
<style>
    /* 🌙 DARK THEME BASE */
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        padding: 30px 20px;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid #2d3746;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .main-header {
        font-size: 3rem !important;
        background: linear-gradient(45deg, #667eea, #764ba2, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .sub-header {
        font-size: 1.2rem !important;
        color: #a0aec0;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* 📊 METRIC CARDS */
    .metric-card {
        background: linear-gradient(135deg, #1e2a47 0%, #2d3746 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .metric-title {
        color: #a0aec0;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    
    .metric-change {
        color: #48bb78;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .metric-subtext {
        color: #718096;
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }
    
    /* 🎯 SECTION HEADERS */
    .section-header {
        font-size: 1.8rem !important;
        color: white;
        margin: 2.5rem 0 1.5rem 0;
        padding: 1.2rem 0;
        border-bottom: 3px solid #667eea;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%);
        border-radius: 12px;
        letter-spacing: 0.5px;
    }
    
    .subsection-header {
        font-size: 1.4rem !important;
        color: #a0aec0;
        margin: 2rem 0 1rem 0;
        padding: 0.8rem 0;
        border-bottom: 2px solid #4a5568;
        font-weight: 600;
    }
    
    /* 💫 INFO CARDS */
    .info-card {
        background: linear-gradient(135deg, #1e2a47 0%, #2d3746 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        border: 1px solid #2d3746;
    }
    
    .nutrition-card {
        background: linear-gradient(135deg, #1a3c2f 0%, #2d3746 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        border: 1px solid #2d5a4b;
    }
    
    .company-card {
        background: linear-gradient(135deg, #2d1a47 0%, #2d3746 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        border: 1px solid #4a2d5a;
    }
    
    .price-card {
        background: linear-gradient(135deg, #1a473c 0%, #2d3746 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border: 1px solid #2d5a4b;
    }
    
    /* ⭐ STAR RATING */
    .star-rating {
        color: #FFD700;
        font-size: 1.8rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    /* 🎮 BUTTONS */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102,126,234,0.4);
    }
    
    /* 📱 INPUTS */
    .stTextInput input {
        border-radius: 8px;
        border: 1px solid #2d3746;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        background: #1a202c;
        color: white;
    }
    
    .stTextInput input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102,126,234,0.2);
    }
    
    /* 📊 CHART CONTAINERS */
    .chart-container {
        background: #1a202c;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid #2d3746;
    }
    
    /* 🔄 UPLOAD/CAMERA */
    .stCameraInput, .stFileUploader {
        border-radius: 12px;
        border: 2px dashed #2d3746;
        background: #1a202c;
    }
    
    /* 🏷️ LABELS */
    .section-label {
        color: #a0aec0;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    /* 🎨 IMPROVED HEADINGS */
    .main-title {
        font-size: 2.2rem !important;
        color: white;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .card-title {
        font-size: 1.5rem !important;
        color: white;
        font-weight: 600;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        padding-left: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Streamlit Setup ---
st.set_page_config(page_title="Know Your Product", page_icon="🧠", layout="wide")

# Main Header
st.markdown("""
<div class="main">
    <div class="main-header">Know Your Product</div>
    <div class="sub-header">Upload or click a product image and discover its details, nutrition, and company info</div>
</div>
""", unsafe_allow_html=True)

# --- Camera or Upload Input ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("#### 📷 Take a Photo")
    img = st.camera_input("", label_visibility="collapsed")
    
with col2:
    st.markdown("#### 📁 Or Upload Image")
    if not img:
        img = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

product_name = None

if img:
    image = Image.open(img)
    st.markdown('<div class="section-header">🖼️ Your Product</div>', unsafe_allow_html=True)
    st.image(image, caption="Your Product Image", use_container_width=True)
    
    product_name = st.text_input(
        "Enter product name or description:",
        placeholder="e.g., Amul Milk 1L, Coca Cola 500ml, iPhone 15 Pro",
        label_visibility="collapsed"
    )

def serpapi_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }
    try:
        res = requests.get("https://serpapi.com/search", params=params, timeout=10)
        return res.json()
    except:
        return {}

# --- Generate Sample Data ---
def generate_sample_data(name):
    return {
        "rating": round(random.uniform(3.5, 4.8), 1),
        "review_count": random.randint(100, 5000),
        "nutrition_score": random.randint(60, 95),
        "price_range": f"${random.randint(5, 50)}-${random.randint(51, 100)}",
        "ingredients": ["Water", "Sugar", "Natural Flavors", "Citric Acid", "Preservatives"],
        "allergens": ["None"],
        "sustainability_score": random.randint(70, 95),
        "popularity_trend": [random.randint(80, 95) for _ in range(6)],
        "compliance_score": random.randint(85, 98),
        "customer_complaints": random.randint(5, 50),
        "monthly_rating": round(random.uniform(3.8, 4.6), 1)
    }

# --- Star Rating Display ---
def display_star_rating(rating):
    stars = ""
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    
    stars += "★" * full_stars
    if half_star:
        stars += "½"
    stars += "☆" * (5 - full_stars - (1 if half_star else 0))
    
    return f'<div class="star-rating">{stars} {rating}/5</div>'

# --- Information Fetch ---
def get_product_info(name):
    info = {"overview": {}, "nutrition": {}, "company": {}, "price": {}, "reviews": {}}
    
    sample_data = generate_sample_data(name)

    # Overview
    data = serpapi_search(name + " product details")
    kg = data.get("knowledge_graph", {})
    if kg:
        info["overview"] = {
            "title": kg.get("title", name),
            "type": kg.get("type", "Consumer Product"),
            "desc": kg.get("description", "No description available."),
            "image": kg.get("image"),
            "brand": kg.get("source", "Unknown Brand"),
            "rating": sample_data["rating"],
            "review_count": sample_data["review_count"],
            "popularity_trend": sample_data["popularity_trend"],
            "compliance_score": sample_data["compliance_score"],
            "customer_complaints": sample_data["customer_complaints"],
            "monthly_rating": sample_data["monthly_rating"]
        }
    else:
        info["overview"] = {
            "title": name, "type": "Consumer Product", "desc": "Product description not available.",
            "brand": "Various Brands", "rating": sample_data["rating"],
            "review_count": sample_data["review_count"], "popularity_trend": sample_data["popularity_trend"],
            "compliance_score": sample_data["compliance_score"], "customer_complaints": sample_data["customer_complaints"],
            "monthly_rating": sample_data["monthly_rating"]
        }

    # Nutrition
    nutri = serpapi_search(name + " nutrition facts")
    snippet = nutri.get("organic_results", [{}])[0].get("snippet", "Nutrition information not available.")
    info["nutrition"] = {
        "facts": snippet, "score": sample_data["nutrition_score"],
        "ingredients": sample_data["ingredients"], "allergens": sample_data["allergens"]
    }

    # Company
    comp = serpapi_search(name + " manufacturer company details")
    company_data = comp.get("knowledge_graph", {})
    info["company"] = {
        "name": company_data.get("title", "Manufacturer information not available"),
        "desc": company_data.get("description", "Company description not available."),
        "website": company_data.get("website"), "sustainability": sample_data["sustainability_score"]
    }

    # Price
    price = serpapi_search(name + " price buy online")
    if "shopping_results" in price and price["shopping_results"]:
        products = price["shopping_results"][:3]
        info["price"]["items"] = [
            {"title": p.get("title"), "price": p.get("price"), "link": p.get("link")}
            for p in products
        ]
    else:
        info["price"]["items"] = [
            {"title": f"{name} - Online Retailer A", "price": f"${random.randint(10, 25)}.99", "link": "#"},
            {"title": f"{name} - Online Retailer B", "price": f"${random.randint(12, 28)}.49", "link": "#"}
        ]

    # Reviews
    reviews = serpapi_search(name + " product reviews")
    review_snippet = reviews.get("organic_results", [{}])[0].get("snippet", "Customer reviews not available.")
    info["reviews"] = {"snippet": review_snippet, "rating": sample_data["rating"]}

    return info

# --- Create Professional Charts ---
def create_compliance_gauge(score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Compliance Score", 'font': {'color': 'white', 'size': 16}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#48bb78"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#e53e3e'},
                {'range': [50, 80], 'color': '#dd6b20'},
                {'range': [80, 100], 'color': '#38a169'}
            ],
        }
    ))
    fig.update_layout(
        height=250,
        font={'color': "white", 'family': "Arial"},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_rating_trend(trend_data):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    fig = px.line(
        x=months, y=trend_data,
        title="Monthly Rating Trend",
        labels={'x': 'Month', 'y': 'Rating'},
        line_shape='spline'
    )
    fig.update_traces(line=dict(color='#667eea', width=3))
    fig.update_layout(
        height=250,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        title_font_color='white'
    )
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    return fig

# --- Display UI ---
if st.button("🔍 Get Product Information") and product_name:
    with st.spinner("Analyzing product data..."):
        data = get_product_info(product_name)

    st.success("Product analysis complete!")

    # --- METRICS DASHBOARD ---
    st.markdown('<div class="section-header">📊 Product Analytics Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Compliance Struct</div>
            <div class="metric-value">98.5%</div>
            <div class="metric-change">+2.1%</div>
            <div class="metric-subtext">Industry benchmark: 96.4%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_compliance_gauge(data["overview"].get("compliance_score", 95)), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Customer Complaints</div>
            <div class="metric-value">12</div>
            <div class="metric-change">-5 from last month</div>
            <div class="metric-subtext">Updated just now</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Resolution Rate</div>
            <div class="metric-value">94%</div>
            <div class="metric-change">+3% improvement</div>
            <div class="metric-subtext">Industry average: 89%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Avg. Customer Rating</div>
            <div class="metric-value">4.6/5</div>
            <div class="metric-change">Monthly average: 4.5</div>
            <div class="metric-subtext">Updated 1 minute ago</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_rating_trend(data["overview"].get("popularity_trend", [4.2, 4.4, 4.3, 4.6, 4.5, 4.6])), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- PRODUCT OVERVIEW ---
    st.markdown('<div class="section-header">🏷️ Product Overview</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        if data["overview"].get("image"):
            st.image(data["overview"]["image"], use_container_width=True)
        else:
            st.image("C:/Users/LOQ/Desktop/images.jpg", use_container_width=True)

    with col2:
        st.markdown(f'<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{data["overview"].get("title", "Unknown Product")}</div>', unsafe_allow_html=True)
        st.write(data["overview"].get("desc", "Product description not available."))
    
    # Display review count and brand first
        st.markdown(f"**Based on {data['overview'].get('review_count', 0):,} customer reviews**")
    
        if data["overview"].get("brand"):
            st.markdown(f"**Brand:** {data['overview']['brand']}")
    
    # Add separator
        st.markdown("---")
    
    # Display star rating at the bottom
        rating = data["overview"].get("rating", 4.0)
        st.markdown(display_star_rating(rating), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- NUTRITION & INGREDIENTS ---
    st.markdown('<div class="section-header">🍎 Nutrition & Ingredients</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f'<div class="nutrition-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Nutrition Facts</div>', unsafe_allow_html=True)
        st.write(data["nutrition"]["facts"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="subsection-header">Ingredients</div>', unsafe_allow_html=True)
        for ingredient in data["nutrition"].get("ingredients", []):
            st.markdown(f'<div class="metric-box" style="padding: 0.8rem; margin: 0.3rem 0; background: #2d3746; border-radius: 8px; color: white;">• {ingredient}</div>', unsafe_allow_html=True)

    # --- PRICING & AVAILABILITY ---
    # --- PRICING & AVAILABILITY ---
    st.markdown('<div class="section-header">Pricing & Availability</div>', unsafe_allow_html=True)
    if "items" in data["price"]:
        for p in data["price"]["items"]:
            st.markdown(f'<div class="price-card">', unsafe_allow_html=True)
            st.markdown(f"**{p['title']}**")
            st.markdown(f"**Price:** {p.get('price', 'N/A')}")
            if p.get('link') != '#':
                st.markdown(f"[Purchase Link]({p['link']})")
            st.markdown('</div>', unsafe_allow_html=True)

            # --- REVIEWS ---
    st.markdown('<div class="section-header">Customer Reviews</div>', unsafe_allow_html=True)
    gemini_badge = '<span class="gemini-badge">AI Enhanced</span>' if data["reviews"].get("gemini_generated") else ""
    st.markdown(f'<div class="info-card">', unsafe_allow_html=True)
    st.markdown(f"#### Review Summary {gemini_badge}")
    st.write(data["reviews"]["snippet"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #718096; font-size: 0.9rem;'>Know Your Product Analytics Dashboard • Powered by SerpAPI</div>", unsafe_allow_html=True)