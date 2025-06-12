import streamlit as st

# Set page config
st.set_page_config(page_title="Smart Sahayak", page_icon="🤖", layout="wide")

# Sidebar Logo and Navigation
st.sidebar.image("https://i.ibb.co/fSP64Vq/smart-sahayak-logo.png", width=200)
st.sidebar.title("🔍 Smart Sahayak")
page = st.sidebar.radio("Navigate to", ["🏠 Home", "📚 AI Lessons", "🌐 Translate", "❓ Help"])

# AI Lessons Content (Multilingual)
lessons = {
    "What is Artificial Intelligence?": {
        "English": "Artificial Intelligence (AI) is a technology where machines can think and act like humans.",
        "Hindi": "कृत्रिम बुद्धिमत्ता (AI) एक ऐसी तकनीक है जिसमें मशीनें इंसानों की तरह सोच और काम कर सकती हैं।",
        "Marathi": "कृत्रिम बुद्धिमत्ता (AI) ही एक तंत्रज्ञान आहे जिथे यंत्रे माणसांसारखी विचार करू शकतात.",
        "Bengali": "কৃত্রিম বুদ্ধিমত্তা (AI) এমন একটি প্রযুক্তি যেখানে মেশিন মানুষের মতো চিন্তা ও কাজ করতে পারে।",
        "Tamil": "செயற்கை நுண்ணறிவு என்பது மனிதர்களைப் போல சிந்தித்து செயல்படும் தொழில்நுட்பமாகும்."
    },
    "How Does AI Work?": {
        "English": "AI works by learning from data using algorithms and making decisions or predictions.",
        "Hindi": "AI डेटा से सीखता है और एल्गोरिद्म का उपयोग करके निर्णय या पूर्वानुमान करता है।",
        "Marathi": "AI डेटामधून शिकतो आणि अल्गोरिदम वापरून निर्णय घेतो किंवा अंदाज करतो.",
        "Bengali": "AI ডেটা থেকে শিখে এবং অ্যালগরিদম ব্যবহার করে সিদ্ধান্ত বা পূর্বাভাস দেয়।",
        "Tamil": "AI தரவுகளிலிருந்து கற்றுக்கொண்டு الگாரிதம்களை பயன்படுத்தி முடிவுகளை எடுக்கிறது."
    },
    "Applications of AI in Daily Life": {
        "English": "AI is used in voice assistants, recommendation systems, translation apps, and more.",
        "Hindi": "AI का उपयोग वॉयस असिस्टेंट, सिफारिश प्रणाली, अनुवाद ऐप्स आदि में होता है।",
        "Marathi": "AI चा वापर व्हॉईस असिस्टंट, शिफारस प्रणाली, भाषांतर अॅप्स इत्यादीमध्ये होतो.",
        "Bengali": "AI ব্যবহৃত হয় ভয়েস অ্যাসিস্ট্যান্ট, সুপারিশ সিস্টেম, অনুবাদ অ্যাপে।",
        "Tamil": "AI குரல் உதவியாளர்கள், பரிந்துரை அமைப்புகள் மற்றும் மொழிபெயர்ப்பு செயலிகளில் பயன்படுத்தப்படுகிறது."
    }
}

# Home Page
if page == "🏠 Home":
    st.title("🤖 Welcome to Smart Sahayak")
    st.subheader("Empowering India with AI knowledge in local languages")
    st.image("https://cdn.pixabay.com/photo/2020/06/30/20/59/kids-5357528_960_720.jpg", use_column_width=True)
    st.markdown("""
    ### 🚀 Features:
    - Multilingual AI lessons
    - Translation tool for learners
    - Visual and text-based learning
    - Designed for accessibility and simplicity
    """)

# AI Lessons Page
elif page == "📚 AI Lessons":
    st.title("📚 Learn AI Basics")
    language = st.selectbox("Choose your language:", ["English", "Hindi", "Marathi", "Bengali", "Tamil"])
    topic = st.radio("Select a topic:", list(lessons.keys()))
    if topic:
        st.subheader(f"📘 {topic}")
        st.success(lessons[topic][language])

# Translate Tool Page
elif page == "🌐 Translate":
    st.title("🌐 Language Translator (Demo)")
    input_text = st.text_input("Enter a sentence to translate:")
    target_lang = st.selectbox("Translate to:", ["Hindi", "Marathi", "Bengali", "Tamil", "English"])
    if input_text:
        st.info("🔁 Translation (simulated):")
        st.success(f"[Translated '{input_text}' to {target_lang}]")

# Help Page
elif page == "❓ Help":
    st.title("❓ Help & Support")
    st.markdown("""
    **What is Smart Sahayak?**  
    A simple, AI-powered interpreter-style app that teaches AI basics in your own language.

    **Can I use it offline?**  
    Offline mode is coming soon via SMS-based lessons.

    **Who is it for?**  
    Students, rural learners, and curious minds who want to learn AI in their own tongue.

    📧 Contact: smart.sahayak@appsupport.org
    """)
