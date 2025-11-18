import streamlit as st

# -----------------------------------------------------------
#   🎀 BIS Compliance Checker — Pink + Purple Aesthetic UI
#   Mini Project (Student Friendly)
# -----------------------------------------------------------

st.set_page_config(page_title="Checker", page_icon="🛡️")

# 🌸 Pink-Purple Theme CSS
st.markdown("""
<style>

body {
    background-color: #fdeff4;
}

/* Title Box */
.title-box {
    background: linear-gradient(90deg, #ff80b5, #c77dff);
    padding: 18px;
    border-radius: 14px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 4px 14px rgba(255, 105, 180, 0.28);
}

/* Generic Card Box */
.box {
    background: #fff0f7;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 18px;
    border: 1px solid #ffb3d9;
    box-shadow: 0px 3px 12px rgba(255, 105, 180, 0.18);
}

/* Headers */
h2, h3, .stSubheader {
    color: #d63384 !important;
    font-weight: 700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffe6f1 !important;
    border-right: 2px solid #ffb3d9;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff99cc, #c77dff);
    color: white;
    border: none;
    padding: 10px 18px;
    font-size: 16px;
    border-radius: 8px;
    box-shadow: 0px 3px 10px rgba(255, 105, 180, 0.3);
}

.stButton>button:hover {
    background: linear-gradient(90deg, #ff70b8, #b45bff);
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title-box'><h1>🛡️smart-quality-checker</h1></div>", unsafe_allow_html=True)


# ---------------------------
# RULES
# ---------------------------
RULES = {
    "Electronics": {
        "required": [
            "Electrical safety test",
            "EMI/EMC test (if needed)",
            "Energy label (optional)"
        ],
        "recommended": [
            "Grounding check",
            "Insulation resistance test"
        ]
    },
    "Helmet": {
        "required": [
            "ISI mark (IS 4151)",
            "Impact absorption test",
            "Strap strength test"
        ],
        "recommended": [
            "Proper size marking",
            "Manufacturing date on product"
        ]
    },
    "Packaged Food": {
        "required": [
            "FSSAI license",
            "Expiry + MRP label",
        ],
        "recommended": [
            "Batch trace info",
            "Proper storage label"
        ]
    },
    "Toy": {
        "required": [
            "Mechanical safety test",
            "Flammability test"
        ],
        "recommended": [
            "Age group marking",
            "Warning labels"
        ]
    },
    "Other": {
        "required": ["Relevant BIS test"],
        "recommended": ["Basic labeling"]
    }
}


# ---------------------------------
# Sidebar Inputs
# ---------------------------------
st.sidebar.title("📌 Product Details")

ptype = st.sidebar.selectbox("Select product type", list(RULES.keys()))
pname = st.sidebar.text_input("Product name / model")
puse = st.sidebar.text_input("Intended use")

st.sidebar.write("---")
elec = st.sidebar.checkbox("Contains electrical parts")
chem = st.sidebar.checkbox("Has chemicals / paint")
wear = st.sidebar.checkbox("Product is wearable")


# ---------------------------------
# Summary Section
# ---------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("📌 Product Summary")
st.write(f"**Type:** {ptype}")
if pname:
    st.write(f"**Name:** {pname}")
if puse:
    st.write(f"**Use:** {puse}")
st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------
# Rule Processing
# ---------------------------------
req = RULES[ptype]["required"].copy()
rec = RULES[ptype]["recommended"].copy()

if elec:
    req.append("Electrical leakage test")

if chem:
    req.append("Chemical safety check")

if wear and ptype != "Helmet":
    rec.append("Skin allergy test")


# ---------------------------------
# Mandatory Tests
# ---------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("🛠 Mandatory Tests")
for i, r in enumerate(req, 1):
    st.write(f"{i}. {r}")
st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------
# Recommended Checks
# ---------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("📄 Recommended Checks")
for i, r in enumerate(rec, 1):
    st.write(f"{i}. {r}")
st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------
# Checklist Generator
# ---------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("📝 Generate Checklist")

if st.button("Create"):
    text = f"""
BIS COMPLIANCE CHECKLIST
------------------------
Product Type: {ptype}
Name: {pname or 'N/A'}

Mandatory:
{chr(10).join(['- '+x for x in req])}

Recommended:
{chr(10).join(['- '+x for x in rec])}
"""
    st.code(text)
    st.download_button("Download Checklist", text, "checklist.txt")
    
st.markdown("</div>", unsafe_allow_html=True)
