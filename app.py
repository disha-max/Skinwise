
import streamlit as st
from ingredients import ingredients

st.set_page_config(
    page_title="SkinWise | Skincare Made Simple",
    page_icon="🌿",
    layout="wide"
)

# Custom design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(222, 224, 202, 0.30),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(244, 218, 207, 0.35),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #faf7ef 0%,
            #fffaf5 50%,
            #f7f3e9 100%
        );
    color: #3f503e;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 600;
    color: #344c40;
    text-align: center;
    margin-bottom: 2rem;
}

.eyebrow {
    text-align: center;
    color: #b96870;
    background: #f9e7e7;
    border-radius: 30px;
    padding: 9px 18px;
    display: table;
    margin: 0 auto 20px auto;
    letter-spacing: 3px;
    font-size: 0.75rem;
    font-weight: 700;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    line-height: 1.1;
    font-weight: 600;
    text-align: center;
    color: #344c40;
    margin: 0;
}

.hero-subtitle {
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 1.5rem;
    margin-top: 12px;
    color: #526a5b;
}

.hero-description {
    max-width: 620px;
    text-align: center;
    margin: 18px auto 30px auto;
    font-size: 1.05rem;
    line-height: 1.8;
    color: #68746c;
}

div[data-testid="stTextInput"] input {
   
    background: #fffdfb;
    padding: 14px 18px;
    color:black;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #cf8992;
}



/* Style the Explore SkinWise form button */
div[data-testid="stFormSubmitButton"] button {
    background-color: #c97985 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 0.65rem 1.5rem;
    font-weight: 600;
}

/* Force the button text to remain white */
div[data-testid="stFormSubmitButton"] button p,
div[data-testid="stFormSubmitButton"] button span {
    color: #ffffff !important;
}

/* Hover effect */
div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #ad626f !important;
    color: #ffffff !important;
}



.feature-card {
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid #f0dfd9;
    border-radius: 20px;
    padding: 24px 14px;
    text-align: center;
    min-height: 185px;
    box-shadow: 0 8px 24px rgba(95, 68, 55, 0.04);
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 10px;
}

.feature-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: #344c40;
    font-weight: 600;
    margin-bottom: 8px;
}

.feature-description {
    color: #727d74;
    font-size: 0.9rem;
    line-height: 1.6;
}

.notice {
    background: #f8e8e7;
    border-radius: 14px;
    padding: 15px;
    text-align: center;
    color: #765e5b;
    margin-top: 35px;
    font-size: 0.85rem;
}

.results-heading {
    text-align: center;
    margin: 38px 0 28px;
}

.results-label {
    color: #b96870;
    font-size: 0.72rem;
    letter-spacing: 3px;
    font-weight: 700;
}

.results-heading h2 {
    color: #344c40;
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    margin: 10px 0;
}

.results-heading p {
    color: #727d74;
    font-size: 0.95rem;
}

.ingredient-card {
    background: rgba(255, 255, 255, 0.82);
    border: 1px solid #f0dfd9;
    border-radius: 24px;
    padding: 28px;
    margin: 18px auto;
    max-width: 760px;
    box-shadow: 0 10px 30px rgba(95, 68, 55, 0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.ingredient-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 32px rgba(95, 68, 55, 0.10);
}

.ingredient-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

.ingredient-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    background: #edf2e8;
    color: #526a5b;
    width: 44px;
    height: 44px;
    border-radius: 15px;
    font-size: 1.6rem;
}

.ingredient-badge {
    background: #f9e7e7;
    color: #a75f6b;
    border-radius: 30px;
    padding: 7px 13px;
    font-size: 0.78rem;
    font-weight: 600;
}

.ingredient-card h3 {
    color: #344c40;
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    margin: 20px 0 12px;
}

.ingredient-divider {
    height: 1px;
    background: #f0dfd9;
    margin: 18px 0 22px;
}

.ingredient-label {
    color: #b96870;
    font-size: 0.7rem;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 16px 0 7px;
}

.ingredient-function {
    color: #46574b;
    font-size: 1rem;
    line-height: 1.8;
}

.ingredient-use {
    display: inline-block;
    background: #f1f3eb;
    color: #526a5b;
    padding: 9px 13px;
    border-radius: 10px;
    font-size: 0.9rem;
}



/* Product comparison heading */

.compare-heading {
    text-align: center;
    margin: 55px 0 30px;
}

.compare-heading span {
    color: #b8767e;
    font-size: 2.8rem;
    letter-spacing: 2px;
    font-weight: 600;
}

.compare-heading h2 {
    color: #526a5b;
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 400;
    margin: 10px 0;
}

.compare-heading p {
    color: #7b8178;
     font-size: 1.4 rem;;
    margin-top: 8px;
}

/* Product labels */
.product-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 500;
    line-height: 1.5;
    margin-bottom: 14px;    
}

.product-one {
    color: #b8767e !important;
}

.product-two {
    color: #647b68 !important;
}

/* Form labels */
div[data-testid="stForm"] label {
    color: #526a5b;
}

/* Input boxes */
div[data-testid="stForm"] input,
div[data-testid="stForm"] textarea {
    background-color: #fffdfb;
    
    border-radius: 12px;
    color: #3e5145;
}

/* Comparison button */
div[data-testid="stFormSubmitButton"] button {
    background-color: #c77d87 !important;
    color: white !important;
    border: none !important;
    padding: 0.7rem 1.5rem;
    font-weight: 600;
    margin-top: 12px;
}

div[data-testid="stFormSubmitButton"] button p {
    color: white !important;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #ad6874 !important;
}


/* Comparison results */
.comparison-results {
    margin: 32px 0;
}

.comparison-title {
    font-family: 'Playfair Display', serif;
    color: #526a5b;
    font-size: 2rem;
    text-align: center;
    margin-bottom: 6px;
}

.comparison-subtitle {
    color: #7b8178;
    text-align: center;
    font-size: 0.95rem;
    margin-bottom: 26px;
}

.overlap-card {
    background: #fffdfb;
    border: 1px solid #eeded9;
    border-radius: 22px;
    padding: 26px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(95, 68, 55, 0.04);
}

.overlap-label {
    color: #b8767e;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.overlap-number {
    color: #526a5b;
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    line-height: 1.3;
    margin: 8px 0;
}

.overlap-track {
    height: 8px;
    background: #f3e8e5;
    border-radius: 20px;
    overflow: hidden;
    margin: 16px auto 10px;
    max-width: 420px;
}

.overlap-fill {
    height: 100%;
    background: #c97985;
    border-radius: 20px;
}

.overlap-caption {
    color: #7b8178;
    font-size: 0.85rem;
}

.ingredient-result-card {
    background: rgba(255, 253, 251, 0.9);
    border: 1px solid #eeded9;
    border-radius: 18px;
    padding: 22px;
    min-height: 150px;
    margin-bottom: 14px;
}

.ingredient-result-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    margin-bottom: 14px;
}

.shared-title {
    color: #647b68;
}

.unique-one-title {
    color: #b8767e;
}

.unique-two-title {
    color: #647b68;
}

.ingredient-chip {
    display: inline-block;
    background: #f5eee9;
    color: #526a5b;
    border-radius: 20px;
    padding: 7px 11px;
    margin: 3px;
    font-size: 0.84rem;
    overflow-wrap: anywhere;
}

.empty-result {
    color: #8b8b80;
    font-size: 0.9rem;
    font-style: italic;
}



</style>
""", unsafe_allow_html=True)

# Brand
st.markdown('<div class="brand">🌿 SkinWise</div>',
            unsafe_allow_html=True)

# Hero section
st.markdown(
    '<div class="eyebrow">✦ SKINCARE MADE SIMPLE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<h1 class="hero-title">SkinWise</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Your personal skincare ingredient explorer'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-description">'
    'Discover skincare ingredients, understand their '
    'common functions, and compare products — all in one place.'
    '</div>',
    unsafe_allow_html=True
)

# Search area
with st.form("product_search"):
    product_name = st.text_input(
        "",
        placeholder="Search for a skincare product or ingredient..."
    )

    search_clicked = st.form_submit_button(
        "Explore SkinWise",
        use_container_width=True
    )



if search_clicked:
    if not product_name.strip():
        st.info("Please enter an ingredient to search.")
    else:
        query = product_name.strip().lower()

        results = [
            ingredient
            for ingredient in ingredients
            if query in ingredient["name"].lower()
        ]

        if results:
            st.markdown("""
            <div class="results-heading">
                <span class="results-label">YOUR SKINCARE LIBRARY</span>
                <h2>Ingredient discoveries 🌿</h2>
                <p>A little more knowledge for your skincare shelf.</p>
            </div>
            """, unsafe_allow_html=True)

            for ingredient in results:
                st.markdown(f"""
                <div class="ingredient-card">
                    <div class="ingredient-card-top">
                        <span class="ingredient-icon">✿</span>
                        <span class="ingredient-badge">
                            {ingredient['category']}
                        </span>
                    </div>
                    <h3>{ingredient['name']}</h3>
                    <div class="ingredient-divider"></div>
                    <p class="ingredient-label">WHAT IT DOES</p>
                    <p class="ingredient-function">
                        {ingredient['function']}
                    </p>
                    <p class="ingredient-label">COMMONLY FOUND IN</p>
                    <p class="ingredient-use">
                        {ingredient['common_use']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No matching ingredient found in our sample database.")




# PRODUCT COMPARISON
st.markdown("""
<div class="compare-heading">
    <h1>Compare your products</h1>
    <p>A little clarity for your skincare shelf.</p>
</div>
""", unsafe_allow_html=True)

with st.form("product_comparison"):
    col1, col2 = st.columns(2, gap="medium")

    with col1:
       st.markdown(
    '<div class="product-label product-one">Product One</div>',
    unsafe_allow_html=True
)
       product_a = st.text_input(
            "Product name",
            placeholder="e.g. Daily Moisturiser",
            key="product_a"
        )
       ingredients_a = st.text_area(
            "Ingredients",
            placeholder="Niacinamide, Glycerin, Ceramides...",
            height=110,
            key="ingredients_a"
        )

    with col2:
        st.markdown(
    '<div class="product-label product-two">Product Two</div>',
    unsafe_allow_html=True
)
        product_b = st.text_input(
            "Product name",
            placeholder="e.g. Hydrating Serum",
            key="product_b"
        )
        ingredients_b = st.text_area(
            "Ingredients",
            placeholder="Glycerin, Hyaluronic Acid...",
            height=110,
            key="ingredients_b"
        )

    st.markdown(
        '<div class="compare-button-marker"></div>',
        unsafe_allow_html=True
    )
    compare_clicked = st.form_submit_button(
        "Compare products ↗",
        use_container_width=True
    )


# PRODUCT COMPARISON LOGIC

if compare_clicked:
    if not ingredients_a.strip() or not ingredients_b.strip():
        st.warning("Please enter ingredients for both products.")

    else:
        # Split the ingredient lists and normalize the text
        product_a_set = {
            item.strip().lower()
            for item in ingredients_a.split(",")
            if item.strip()
        }

        product_b_set = {
            item.strip().lower()
            for item in ingredients_b.split(",")
            if item.strip()
        }

        # Find shared and unique ingredients
        shared = sorted(product_a_set & product_b_set)
        unique_a = sorted(product_a_set - product_b_set)
        unique_b = sorted(product_b_set - product_a_set)

        # Calculate ingredient overlap
        total_unique = product_a_set | product_b_set
        overlap = (
            len(shared) / len(total_unique) * 100
            if total_unique else 0
        )

       
        import html

        # Pretty comparison heading
        st.markdown("""
        <div class="comparison-results">
            <div class="comparison-title">Your comparison results</div>
            <div class="comparison-subtitle">
                A closer look at what's shared and what's different.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Overlap score card
        st.markdown(f"""
        <div class="overlap-card">
            <div class="overlap-label">Ingredient overlap</div>
            <div class="overlap-number">{overlap:.1f}%</div>
            <div class="overlap-track">
                <div class="overlap-fill"
                     style="width: {overlap:.1f}%;">
                </div>
            </div>
            <div class="overlap-caption">
                {len(shared)} shared ingredients out of
                {len(total_unique)} distinct ingredients
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Ingredient result cards
        result_cols = st.columns(3, gap="medium")

        sections = [
            ("Shared ingredients", shared, "shared-title"),
            ("Only in Product One", unique_a, "unique-one-title"),
            ("Only in Product Two", unique_b, "unique-two-title"),
        ]

        for column, (title, items, color_class) in zip(
            result_cols, sections
        ):
            with column:
                if items:
                    chips = "".join(
                        f'<span class="ingredient-chip">'
                        f'{html.escape(item.title())}</span>'
                        for item in items
                    )
                else:
                    message = (
                        "No shared ingredients found."
                        if title == "Shared ingredients"
                        else "No unique ingredients."
                    )
                    chips = (
                        f'<div class="empty-result">'
                        f'{message}</div>'
                    )

                st.markdown(f"""
                <div class="ingredient-result-card">
                    <div class="ingredient-result-title {color_class}">
                        {html.escape(title)}
                    </div>
                    {chips}
                </div>
                """, unsafe_allow_html=True)


st.write("")

# Feature cards
features = [
    ("🌱", "Ingredient Insights",
     "Learn what's in your skincare products."),
    ("🧪", "Function Guide",
     "Understand what ingredients commonly do."),
    ("🛡️", "Informed Choices",
     "Explore product information before you buy."),
    ("♡", "Your Skin, Your Way",
     "Make choices that fit your skincare goals.")
]

columns = st.columns(4)

for column, feature in zip(columns, features):
    icon, title, description = feature

    with column:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    ✦ SkinWise is an educational project, not a medical diagnosis tool.
    Ingredient effects depend on formulation and individual circumstances.
</div>
""", unsafe_allow_html=True)
