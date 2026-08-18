import streamlit as st
import random

# ตั้งค่าหน้าเว็บให้เป็น Theme โทนเข้มสไตล์แอปอาหาร
st.set_page_config(page_title="Food Recommendation App", layout="wide", page_icon="🍔")

# Custom CSS ตกแต่ง Card ให้มีมิติใกล้เคียงกับดีไซน์ UI
st.markdown("""
    <style>
    .food-card {
        background-color: #1E1E1E;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .star-rating {
        color: #FFB800;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 1. จำลองฐานข้อมูลอาหาร 
FOOD_DB = {
    "สปาเกตตีคาโบนารา": {
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?w=500",
        "description": "ซอสครีมเข้มข้น รสชาติกลมกล่อม หอมชีสพาร์เมซาน",
        "recipes": ["สูตรต้นตำรับอิตาเลียน (ใช้ไข่แดง)", "สูตรครีมซอสทำง่าย", "สูตรคลีน (ลดแคลอรี)"],
        "restaurants": ["Urban Bites (จัดส่ง 30 นาที)", "Pasta Corner", "Kitchen 101"]
    },
    "ข้าวผัดกุ้ง": {
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=500",
        "description": "ข้าวผัดเม็ดสวย หอมกลิ่นกระทะ กุ้งสดตัวโต",
        "recipes": ["สูตรเชฟกระทะเหล็ก (หอมกลิ่นกระทะ)", "สูตรข้าวผัดกุ้งคลีน", "สูตรด่วน 5 นาที"],
        "restaurants": ["ครัวบ้านเรา", "ร้านข้าวผัดคุณต๋อย", "อาหารตามสั่งเฮียเล้ง"]
    },
    "สลัดอกไก่ย่าง": {
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=500",
        "description": "ผักสดกรอบ พร้อมอกไก่นุ่มสุกกำลังดี น้ำสลัดงาญี่ปุ่น",
        "recipes": ["สูตรคลีน high protein", "สูตรอกไก่นุ่มด้วยหม้อทอดไร้น้ำมัน"],
        "restaurants": ["Salad Factory", "Green Bowl", "Clean Food Club"]
    }
}

# 2. ส่วนหัวของแอปพลิเคชัน (Header)
st.title("What are you Craving today? 🍕")
st.write("ค้นพบเมนูที่เหมาะกับคุณ พร้อมทางเลือกทั้งทำเองและสั่งทาน")

# ช่องค้นหาและตัวกรอง
col_search, col_filter = st.columns([4, 1])
with col_search:
    search_query = st.text_input("🔍 ค้นหาเมนูอาหาร หรือวัตถุดิบ...", placeholder="เช่น สปาเกตตี, กุ้ง, คลีน")

st.divider()

# 3. ส่วนแสดงผลรายการอาหารแนะนำตามระดับดาว (Featured Menu)
st.subheader("🌟 เมนูแนะนำสำหรับคุณ (จัดอันดับตามความชอบ)")

cols = st.columns(len(FOOD_DB))

for idx, (food_name, info) in enumerate(FOOD_DB.items()):
    with cols[idx]:
        st.image(info["image"], use_container_width=True)
        st.subheader(food_name)
        
        # แสดงระดับดาว (Score Rating)
        stars = "⭐" * int(info["rating"])
        st.markdown(f"<span class='star-rating'>{stars} {info['rating']}/5.0</span>", unsafe_allow_html=True)
        st.caption(info["description"])
        
        # ปุ่มเลือกเพื่อดูรายละเอียดเพิ่มเติม
        if st.button(f"เลือกเมนูนี้", key=f"btn_{idx}"):
            st.session_state["selected_food"] = food_name

# 4. ส่วนแสดงรายละเอียดเมื่อผู้ใช้กดเลือกเมนู (Action Area)
if "selected_food" in st.session_state:
    selected = st.session_state["selected_food"]
    food_info = FOOD_DB[selected]
    
    st.divider()
    st.header(f"📌 คุณกำลังสนใจ: {selected}")
    
    # ทางเลือกของผู้ใช้: ทำเอง vs หาร้าน
    option = st.radio("เลือกรูปแบบที่คุณต้องการ:", ["📖 ดูสูตรและวิธีทำ (ทำกินเอง)", "📍 ค้นหาร้านอาหารที่มีเมนูนี้ (สั่งทาน)"], horizontal=True)
    
    if "ทำกินเอง" in option:
        st.subheader("👨‍🍳 คลังสูตรอาหารหลากสไตล์")
        recipe_choice = st.selectbox("เลือกสูตรที่ต้องการทำ:", food_info["recipes"])
        st.success(f"คุณเลือก: **{recipe_choice}**")
        st.info("💡 ส่วนผสมและขั้นตอนการทำจะถูกแสดงผลที่นี่...")
        
    else:
        st.subheader("🛵 ร้านอาหารแนะนำ")
        for res in food_info["restaurants"]:
            st.write(f"- 🏪 **{res}**")