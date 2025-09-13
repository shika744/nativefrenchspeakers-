import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timedelta
import random
import pandas as pd
import os
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Native French Speakers",
    page_icon="🇫🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
        
        .stButton>button {
            background-color: #2171b5;
            color: white !important;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.3rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        /* Make sidebar text white and add background color */
        .css-1d391kg, .css-1wrcr25, .css-ocqkz7, .css-10trblm {
            color: white !important;
        }
        /* Sidebar background and text color */
        .css-1cypcdb, .css-1aehpvj, [data-testid="stSidebar"] {
            background-color: #2171b5 !important;
            color: white !important;
        }
        /* Ensure sidebar header text is white */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6,
        [data-testid="stSidebar"] .st-emotion-cache-10trblm {
            color: white !important;
        }
        /* Make all button text white */
        button, .stButton button, .stButton>button span, button[kind="primary"] {
            color: white !important;
            font-weight: 600 !important;
        }
        .stButton>button:hover {
            background-color: #4393c3;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .footer {
            padding: 1.5rem;
            background-color: #f8f9fa;
            text-align: center;
            font-size: 0.9rem;
            color: #343a40;
            border-top: 1px solid #dee2e6;
            margin-top: 3rem;
            font-weight: 500;
        }
        h1 {
            color: #2171b5;
            font-weight: 700;
            margin-bottom: 1.5rem;
            font-size: 2.5rem;
        }
        h2 {
            color: #2171b5;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
        }
        h3 {
            color: #2171b5;
            font-weight: 600;
        }
        .service-card h3 {
            color: white;
            font-weight: 600;
        }
        .service-card p {
            color: white;
            font-weight: 400;
        }
        .service-card a {
            color: #ffffff;
            text-decoration: underline;
            font-weight: 500;
        }
        .service-card h2 {
            color: white;
            font-weight: 600;
        }
        .service-card {
            background-color: #2171b5;
            padding: 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
            margin-bottom: 1rem;
            border-left: 4px solid #4393c3;
            transition: all 0.3s ease;
            height: 100%;
            color: white;
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }
        .service-icon {
            font-size: 2.5rem;
            color: white;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.1rem;
            line-height: 1.7;
            color: #000000;
            font-weight: 500;
        }
        a {
            color: #2171b5;
            text-decoration: none;
            font-weight: 500;
        }
        /* Add semi-transparent white background to content containers for better readability */
        .block-container, .stApp > div:has(.block-container) {
            background-color: rgba(255, 255, 255, 0.85) !important;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to set page background using base64 encoding
def set_page_background():
    """Set the background image for the page using base64 encoding"""
    try:
        # Try several paths to find the background image
        bg_paths = [
            "../NFS/background.png",  # Relative path
            "C:\\Users\\shika\\OneDrive\\Desktop\\Evaluation\\NFS\\background.png",  # Absolute path
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "NFS", "background.png")  # Constructed path
        ]
        
        # Try each path
        for bg_path in bg_paths:
            if os.path.exists(bg_path):
                print(f"Found background image at: {bg_path}")
                # Embed the image directly using base64
                import base64
                with open(bg_path, "rb") as f:
                    data = base64.b64encode(f.read()).decode()
                
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("data:image/png;base64,{data}");
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                    }}
                    /* Semi-transparent background for content */
                    .block-container {{
                        background-color: rgba(255, 255, 255, 0.85);
                        padding: 2rem;
                        border-radius: 10px;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                print("Successfully embedded background image")
                return True
        
        print("Background image not found!")
        return False
    except Exception as e:
        print(f"Error setting background: {e}")
        return False

# Function to load and display logo
def display_logo():
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
    try:
        logo = Image.open(logo_path)
        st.image(logo, width=250)
    except FileNotFoundError:
        st.write("Logo not found. Please place logo.png in the assets folder.")

# Generate mock data for demonstration
def generate_mock_lessons():
    lesson_types = ["Free Consultation", "Débutant (Beginner)", "Intermédiaire (Intermediate)", "Avancé (Advanced)", 
                   "Conversation", "Grammaire (Grammar)", "Vocabulaire (Vocabulary)"]
    lesson_topics = ["Initial Assessment", "Introduction to French", "Verb Tenses", "Everyday Conversation", 
                    "French Culture", "Idiomatic Expressions", "French Literature"]
    
    today = datetime.now()
    lessons = []
    
    for i in range(5):
        lesson_date = today + timedelta(days=random.randint(1, 14))
        lesson = {
            "id": i + 1,
            "date": lesson_date.strftime("%m/%d/%Y"),  # American date format
            "time": f"{random.randint(9, 18)}:00",
            "type": random.choice(lesson_types),
            "topic": random.choice(lesson_topics),
            "status": random.choice(["scheduled", "completed", "cancelled"])
        }
        lessons.append(lesson)
    
    return lessons

# Page for embedding Calendly
def show_booking_page(translations=None):
    # Get the selected language (default to English if not set)
    lang = st.session_state.get('lang', 'English')
    
    # Use translations if provided, otherwise use English defaults
    if translations:
        t = translations[lang]
        st.title(t["book_lesson"])
    else:
        st.title("Book Your French Learning Journey")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Free Consultation
        Start with a free 30-minute consultation where we will:
        
        1. Discuss your language learning goals
        2. Assess your current French proficiency 
        3. Create a personalized learning plan
        4. Answer any questions about lessons and pricing
        5. Set up your first paid lesson if you decide to proceed

        ### Available Lesson Formats
        - **One-on-one lessons** - Personal attention and customized learning
        - **Small group sessions** - Practice with peers at your level
        - **Business French workshops** - Industry-specific language training
        - **Exam preparation** - Targeted DELF, DALF, TEF, TCF preparation
        """)
        
        # Booking & Rescheduling Policy
        with st.expander("📝 Booking & Rescheduling Policy", expanded=False):
            st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; border-left: 4px solid #2171b5;">
                <h4 style="color: #2171b5;">Booking Instructions</h4>
                <ul>
                    <li>Select available time slots in the calendar on the right</li>
                    <li>Fill in your details and lesson preferences</li>
                    <li>You'll receive an email confirmation with meeting details</li>
                </ul>
                
                <h4 style="color: #2171b5;">Rescheduling Lessons</h4>
                <ul>
                    <li>Need to reschedule? No problem! You can reschedule up to 24 hours before your lesson</li>
                    <li>Use the link in your confirmation email to reschedule</li>
                    <li>Or click the "Reschedule Existing Booking" button below the calendar</li>
                    <li>In your dashboard, each lesson has a "Reschedule" button</li>
                    <li>All sessions are standard 60-minute lessons</li>
                    <li>Appointments can be rescheduled a maximum of 2 times</li>
                </ul>
                
                <h4 style="color: #2171b5;">Cancellation Policy</h4>
                <ul>
                    <li><strong>No refunds</strong> are provided for missed lessons or late cancellations</li>
                    <li>Cancellations less than 24 hours before the scheduled lesson cannot be rescheduled</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Privacy Policy
        with st.expander("🔒 Privacy & Payment Policy", expanded=False):
            st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 10px; border-left: 4px solid #2171b5;">
                <h4 style="color: #2171b5;">Privacy Policy</h4>
                <p>Your personal information is kept confidential and is used only for booking and communication purposes. We do not share your information with third parties.</p>
                
                <h4 style="color: #2171b5;">Payment Terms</h4>
                <ul>
                    <li>Payment must be completed at least 24 hours before your scheduled lesson</li>
                    <li>All payments are final and <strong>non-refundable</strong></li>
                    <li>You may reschedule according to our rescheduling policy above</li>
                    <li>Lesson packages have a validity of 3 months from date of purchase</li>
                </ul>
                
                <p><em>By booking a lesson, you agree to these terms and policies.</em></p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### Questions?")
        st.markdown("""
        Email: [niloafer.chetty0608@gmail.com](mailto:niloafer.chetty0608@gmail.com)
        """)
    
    with col2:
        st.markdown("### Select Your Appointment Type")
        
        # Add availability instructions
        st.info("""
        **Calendar Availability**
        - ✅ Available slots are shown in white in the calendar
        - ❌ Unavailable time slots are grayed out or not shown
        - 📅 Select your preferred date and time to book
        - ⏰ Lesson durations: 30 minutes (free consultation) or 60 minutes (standard lesson)
        - 📆 If a day appears empty, it means no slots are available that day
        """)
        
        # Free 30-minute consultation Calendly integration
        st.markdown("#### 🎯 Free 30-Minute Consultation")
        calendly_html_free = """
        <div class="calendly-inline-widget" 
            data-url="https://calendly.com/niloafer-chetty0608?hide_landing_page_details=1&hide_gdpr_banner=1&primary_color=2171b5&background_color=f8f9fa&text_color=000000&duration=30" 
            style="min-width:320px;height:350px;">
        </div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        """
        components.html(calendly_html_free, height=350)
        
        # Standard 60-minute lesson Calendly integration
        st.markdown("#### 📚 60-Minute Standard Lesson")
        calendly_html_60 = """
        <div class="calendly-inline-widget" 
            data-url="https://calendly.com/niloafer-chetty0608?hide_landing_page_details=1&hide_gdpr_banner=1&primary_color=2171b5&background_color=f8f9fa&text_color=000000&duration=60" 
            style="min-width:320px;height:350px;">
        </div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        """
        components.html(calendly_html_60, height=350)
        
        # Add rescheduling buttons for existing bookings
        st.markdown("### Already Booked?")
        
        col_consult, col_lesson = st.columns(2)
        
        with col_consult:
            reschedule_consult_html = """
            <div style="margin-top: 15px; margin-bottom: 15px;">
                <a href="https://calendly.com/niloafer-chetty0608/rescheduling" target="_blank" style="
                    background-color: #4393c3;
                    color: white;
                    padding: 10px 15px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    width: 100%;
                    box-sizing: border-box;
                    cursor: pointer;
                    border-radius: 5px;
                    font-weight: 600;">
                    🔄 Reschedule Consultation
                </a>
            </div>
            """
            components.html(reschedule_consult_html, height=60)
            
        with col_lesson:
            reschedule_lesson_html = """
            <div style="margin-top: 15px; margin-bottom: 15px;">
                <a href="https://calendly.com/niloafer-chetty0608/rescheduling" target="_blank" style="
                    background-color: #4393c3;
                    color: white;
                    padding: 10px 15px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    width: 100%;
                    box-sizing: border-box;
                    cursor: pointer;
                    border-radius: 5px;
                    font-weight: 600;">
                    🔄 Reschedule Lesson
                </a>
            </div>
            """
            components.html(reschedule_lesson_html, height=60)

# Dashboard page
def show_dashboard(translations=None):
    # Get the selected language (default to English if not set)
    lang = st.session_state.get('lang', 'English')
    
    # Use translations if provided, otherwise use English defaults
    if translations:
        t = translations[lang]
        st.title(t["dashboard"])
    else:
        st.title("Dashboard")
        
    st.subheader("Manage your French lessons and track your progress")
    
    # Create mock data
    lessons = generate_mock_lessons()
    
    # Convert to DataFrame for easier display
    df = pd.DataFrame(lessons)
    
    # Display upcoming lessons
    st.subheader("My Upcoming Lessons")
    upcoming_lessons = df[df["status"] == "scheduled"]
    if not upcoming_lessons.empty:
        for _, lesson in upcoming_lessons.iterrows():
            with st.expander(f"{lesson['date']} at {lesson['time']} - {lesson['type']}: {lesson['topic']}"):
                st.write(f"**Lesson Type:** {lesson['type']}")
                st.write(f"**Topic:** {lesson['topic']}")
                st.write(f"**Date:** {lesson['date']} at {lesson['time']}")
                st.write(f"**Status:** {'✅ Confirmed' if lesson['status'] == 'scheduled' else '⏳ Pending'}")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(f"Join Teams Lesson #{lesson['id']}", key=f"teams_{lesson['id']}"):
                        st.markdown("[Join Microsoft Teams](https://myaccount.microsoft.com/?ref=MeControl)")
                with col2:
                    if st.button(f"Access Materials #{lesson['id']}", key=f"materials_{lesson['id']}"):
                        st.markdown("[Open Course Materials](https://sites.google.com/d/1q_C1IH3KkzbpgQRhVIhbsUGjJ4VwyCzc/p/1OpoVQc9bgi8XZtkPuh9X_XqrKNOkNst9/edit)")
                with col3:
                    if st.button(f"Reschedule #{lesson['id']}", key=f"reschedule_{lesson['id']}"):
                        st.markdown("[Reschedule Appointment](https://calendly.com/niloafer-chetty0608/rescheduling)")
                        st.info("You can reschedule up to 24 hours before your lesson. No refunds are available for missed lessons.")
    else:
        st.info("You don't have any upcoming lessons. Book a lesson now!")
        if st.button("Book a Lesson"):
            st.session_state.page = "booking"
            st.rerun()
    
    # Display lesson history
    st.subheader("Lesson History")
    past_lessons = df[df["status"] == "completed"]
    if not past_lessons.empty:
        st.dataframe(past_lessons[["date", "time", "type", "topic"]])
    else:
        st.info("No lesson history found.")

# Placeholder function for future custom resources
def show_lesson_resources():
    st.title("Learning Resources")
    
    st.markdown("""
    ### Learning materials coming soon
    
    This section will be updated with custom learning materials.
    """)
    
    st.info("No resources available yet.")

# Home page
def show_home(translations):
    # Get the selected language (default to English if not set)
    lang = st.session_state.get('lang', 'English')
    t = translations[lang]
    
    st.title(t["headline"])
    
    st.markdown(f"""
    <div style="font-size: 18px; color: #212529; font-weight: 500;">
    {t["intro"]}
    </div>
    """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown(f"""
    <div style="background-color: #2171b5; color: white; padding: 25px; border-radius: 10px; text-align: center; margin: 30px 0;">
        <h3 style="color: white; margin-bottom: 15px;">📩 {t["cta_title"]}</h3>
        <p style="color: white; font-size: 18px; font-weight: 500;">{t["cta_text"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Call to action buttons
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button(t["consult_btn"], use_container_width=True):
            st.session_state.page = "booking"
            st.rerun()
    with col_btn2:
        if st.button(t["lessons_btn"], use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()
    
    # Why Learn French? Global Benefits Section
    st.markdown("## 🌍 Why Learn French? A Global Perspective", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">🌐 Global Language</h3>
            <p>Spoken by over 300 million people across 5 continents and official in 29 countries. The fifth most spoken language in the world.</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">💼 Career Advantage</h3>
            <p>French companies operate in the US, UK, and globally. Bilingual professionals earn 5-20% higher salaries across industries.</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">🎓 Academic Excellence</h3>
            <p>Opens doors to top French universities and specialized courses. Vital for researchers in literature, arts, culinary, fashion, and international relations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">✈️ Travel & Culture</h3>
            <p>Enhance your experience in France, Canada, Switzerland, Belgium, and 25+ French-speaking countries. Access rich literary, artistic, and culinary traditions.</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">🧠 Cognitive Benefits</h3>
            <p>Learning French improves memory, problem-solving skills, and multitasking abilities. Studies show bilinguals have better resistance to age-related cognitive decline.</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">🔄 Gateway to Languages</h3>
            <p>Learning French makes it easier to learn Spanish, Italian, Portuguese and other Romance languages. A strategic choice for global citizens.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # What We Offer section
    st.markdown("## What We Offer", unsafe_allow_html=True)  # This section will remain in English as it's not in translations yet
    
    st.markdown("""
    <div style="background-color: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
        <p style="color: #212529; font-size: 18px; font-weight: 500; margin-bottom: 15px;">
            ✅ Want to settle in a French-speaking country and need to learn French?<br><br>
            ✅ Want to learn French from scratch?<br><br>
            ✅ Want to read, write, understand, and speak French fluently?<br><br>
            ✅ Want to prepare for Alliance Française exams?<br><br>
            ✅ Want to boost your Business & Professional French for career growth?<br><br>
            ✅ Want corporate training for your company team?<br><br>
            ✅ Want to prepare for international exams (DELF, DALF, TEF, TCF)?<br><br>
            ✅ Want conversation practice to build confidence?<br><br>
            ✅ Want to learn French culture & etiquette for travel or relocation?<br><br>
            ✅ Want a personalized learning plan that fits your goals and schedule?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills section
    st.markdown(f"## {t['skills_title']}", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Grammar & Conjugation</h3>
            <p>Mastering verbs, tenses, and sentence structure</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Vocabulary & Translation</h3>
            <p>Learning useful words and translating between English/French</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Pronunciation & Accent</h3>
            <p>Speaking clearly and sounding natural</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Listening Comprehension</h3>
            <p>Understanding spoken French in real-life situations</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Speaking (Conversation)</h3>
            <p>Practicing dialogue, role-plays, and debates</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Reading Comprehension</h3>
            <p>Reading texts, articles, and exam material</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Writing Skills</h3>
            <p>Writing emails, essays, CVs, and professional reports in French</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Business French</h3>
            <p>Vocabulary for meetings, presentations, and negotiations</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Exam Preparation</h3>
            <p>DELF, DALF, TEF, TCF, and Alliance Française certifications</p>
        </div>
        
        <div style="background-color: #2171b5; color: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
            <h3 style="color: white;">Culture & Etiquette</h3>
            <p>Learning French customs, traditions, and everyday expressions</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional space for visual separation
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pricing section
    st.markdown("## Lesson Pricing", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">🕐</div>
            <h3>Single Lesson</h3>
            <h2>€50</h2>
            <p>1 hour session</p>
            <p>Ideal for focus learning or conversational practice</p>
            <br>
            <a href="https://calendly.com/niloafer-chetty0608" target="_blank">Book Now</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">📘</div>
            <h3>6-Hour Pack</h3>
            <h2>€270</h2>
            <p>€45 per hour - Save €30</p>
            <p>Flexible scheduling within 2 months</p>
            <br>
            <a href="https://calendly.com/niloafer-chetty0608" target="_blank">Book Package</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">📚</div>
            <h3>10-Hour Pack</h3>
            <h2>€399</h2>
            <p>€39.90 per hour - Save €101</p>
            <p>Perfect for regular learners. Valid for 3 months</p>
            <a href="https://calendly.com/niloafer-chetty0608" target="_blank">Best Value</a>
        </div>
        """, unsafe_allow_html=True)

# Payment page
def show_payment():
    st.title("Secure Payment")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### Lesson Details
        - **Lesson Type:** French Conversation
        - **Date:** 09/20/2025
        - **Time:** 6:00 PM - 7:00 PM
        - **Teacher:** Niloafer Chetty
        - **Price:** €35
        """)
    
    with col2:
        st.markdown("### Payment Options")
        payment_option = st.selectbox("Choose a payment method", ["PayPal", "Credit Card"])
        
        # Mock PayPal button
        if payment_option == "PayPal":
            st.markdown("""
            <div style="text-align: center; margin-top: 2rem;">
                <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg" width="150">
                <p style="margin-top: 1rem;"><button style="background-color: #0070ba; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Pay with PayPal</button></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Mock credit card form
            st.text_input("Card Number", "4242 4242 4242 4242")
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Expiration Date", "12/25")
            with col2:
                st.text_input("CVV", "123")
            st.text_input("Name on Card", "")
            if st.button("Complete Payment"):
                st.success("Payment simulation successful! Your lesson is confirmed.")

# Navigation and main app logic
def main():
    # Apply CSS
    local_css()
    
    # Set background image
    set_page_background()
    
    # Initialize session state for navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    # Initialize language in session state
    if "language" not in st.session_state:
        st.session_state.language = "English"
    
    # Dictionary of translations
    translations = {
        "English": {
            "home": "🏠 Home",
            "book_lesson": "📅 Book a Lesson",
            "dashboard": "📊 Dashboard",
            "title": "Native French Speakers",
            "headline": "Fluent French. Confident Communication.",
            "intro": "Welcome! I'm Niloafer Chetty, a certified DALF C2 French trainer with over 15 years of teaching experience. I help individuals, professionals, and businesses achieve fluency, confidence, and cultural understanding in French—whether for work, study, or relocation.",
            "cta_title": "Start your French journey today!",
            "cta_text": "Book your free 30-minute consultation and discover how we can help you achieve your goals with confidence.",
            "consult_btn": "Book a Free 30-Minute Consultation",
            "lessons_btn": "My Lessons",
            "skills_title": "🔹 Skills",
            "pricing_title": "Lesson Pricing",
            "about_title": "About Me"
        },
        "Français": {
            "home": "🏠 Accueil",
            "book_lesson": "📅 Réserver un Cours",
            "dashboard": "📊 Tableau de bord",
            "title": "Locuteurs Natifs Français",
            "headline": "Français Fluide. Communication Confiante.",
            "intro": "Bienvenue ! Je suis Niloafer Chetty, formatrice de français certifiée DALF C2 avec plus de 15 ans d'expérience dans l'enseignement. J'aide les particuliers, les professionnels et les entreprises à atteindre la fluidité, la confiance et la compréhension culturelle en français, que ce soit pour le travail, les études ou la relocation.",
            "cta_title": "Commencez votre parcours en français dès aujourd'hui !",
            "cta_text": "Réservez votre consultation gratuite de 30 minutes et découvrez comment nous pouvons vous aider à atteindre vos objectifs en toute confiance.",
            "consult_btn": "Réserver une Consultation Gratuite de 30 Minutes",
            "lessons_btn": "Mes Leçons",
            "skills_title": "🔹 Compétences",
            "pricing_title": "Tarification des Cours",
            "about_title": "À Propos de Moi"
        },
        "Español": {
            "home": "🏠 Inicio",
            "book_lesson": "📅 Reservar una Clase",
            "dashboard": "📊 Panel",
            "title": "Hablantes Nativos de Francés",
            "headline": "Francés Fluido. Comunicación Confiada.",
            "intro": "¡Bienvenido! Soy Niloafer Chetty, profesora certificada de francés DALF C2 con más de 15 años de experiencia en enseñanza. Ayudo a individuos, profesionales y empresas a lograr fluidez, confianza y entendimiento cultural en francés, ya sea para trabajo, estudio o reubicación.",
            "cta_title": "¡Comienza tu viaje en francés hoy!",
            "cta_text": "Reserva tu consulta gratuita de 30 minutos y descubre cómo podemos ayudarte a alcanzar tus objetivos con confianza.",
            "consult_btn": "Reservar una Consulta Gratuita de 30 Minutos",
            "lessons_btn": "Mis Lecciones",
            "skills_title": "🔹 Habilidades",
            "pricing_title": "Precios de las Lecciones",
            "about_title": "Sobre Mí"
        },
        "Deutsch": {
            "home": "🏠 Startseite",
            "book_lesson": "📅 Unterricht buchen",
            "dashboard": "📊 Übersicht",
            "title": "Französische Muttersprachler",
            "headline": "Fließendes Französisch. Selbstbewusste Kommunikation.",
            "intro": "Willkommen! Ich bin Niloafer Chetty, eine zertifizierte DALF C2 Französisch-Trainerin mit über 15 Jahren Unterrichtserfahrung. Ich helfe Einzelpersonen, Fachleuten und Unternehmen, Flüssigkeit, Selbstvertrauen und kulturelles Verständnis in Französisch zu erreichen – sei es für die Arbeit, das Studium oder den Umzug.",
            "cta_title": "Beginnen Sie noch heute Ihre Französisch-Reise!",
            "cta_text": "Buchen Sie Ihre kostenlose 30-minütige Beratung und entdecken Sie, wie wir Ihnen helfen können, Ihre Ziele mit Selbstvertrauen zu erreichen.",
            "consult_btn": "Kostenlose 30-minütige Beratung buchen",
            "lessons_btn": "Meine Lektionen",
            "skills_title": "🔹 Fähigkeiten",
            "pricing_title": "Unterrichtspreise",
            "about_title": "Über Mich"
        },
        "中文": {
            "home": "🏠 首页",
            "book_lesson": "📅 预订课程",
            "dashboard": "📊 仪表板",
            "title": "法语母语人士",
            "headline": "流利法语。自信交流。",
            "intro": "欢迎！我是Niloafer Chetty，一位拥有超过15年教学经验的DALF C2认证法语培训师。无论是为了工作、学习还是搬迁，我都能帮助个人、专业人士和企业在法语中达到流利、自信和文化理解。",
            "cta_title": "今天就开始您的法语之旅！",
            "cta_text": "预约您的30分钟免费咨询，了解我们如何帮助您自信地实现目标。",
            "consult_btn": "预约30分钟免费咨询",
            "lessons_btn": "我的课程",
            "skills_title": "🔹 技能",
            "pricing_title": "课程价格",
            "about_title": "关于我"
        }
    }
    
    # Get current language translations
    current_lang = translations.get(st.session_state.language, translations["English"])
    
    # Sidebar
    with st.sidebar:
        display_logo()
        
        # Language selector
        st.markdown("### 🌐 Language / Langue")
        selected_language = st.selectbox(
            "",
            options=list(translations.keys()),
            index=list(translations.keys()).index(st.session_state.language),
            key="language_selector"
        )
        
        # Update language if changed
        if selected_language != st.session_state.language:
            st.session_state.language = selected_language
            st.rerun()
        
        st.markdown(f"## {current_lang['title']}", unsafe_allow_html=True)
        
        if st.button(current_lang["home"], use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
            
        if st.button(current_lang["book_lesson"], use_container_width=True):
            st.session_state.page = "booking"
            st.rerun()
            
        if st.button(current_lang["dashboard"], use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()
    
    # Display the selected page
    if st.session_state.page == "home":
        show_home(translations)
    elif st.session_state.page == "booking":
        show_booking_page(translations)
    elif st.session_state.page == "dashboard":
        show_dashboard(translations)
    # Resources page removed
    elif st.session_state.page == "payment":
        show_payment()
    
    # About Me section
    st.markdown("## About Me", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Contact Information:**
        
        📧 [NiloaferChetty@NativeFrenchSpeakers.onmicrosoft.com](mailto:NiloaferChetty@NativeFrenchSpeakers.onmicrosoft.com)
        
        📧 [niloafer.chetty0608@gmail.com](mailto:niloafer.chetty0608@gmail.com)
        
        📅 [Book a Free 30-Minute Consultation or French Lesson](https://calendly.com/niloafer-chetty0608)
        """)
    
    with col2:
        st.markdown("""
        My journey with French began at the age of 2, and it's been a lifelong passion ever since. Growing up speaking the language gave me not only fluency, but a deep cultural connection that I now bring into every lesson. 
        
        With over 15 years of experience, I've had the privilege of teaching learners from all walks of life—professionals, students, and adults—helping them gain the confidence to use French in real-world situations.
        
        I love reading, I have a deep appreciation for literature, and I'm passionate about discovering new cultures through travel. These passions enrich my teaching, allowing me to bring language to life through stories, cultural insights, and authentic contexts.
        """)
        
        if st.button("📩 Book your free 30-minute consultation today", use_container_width=True):
            st.session_state.page = "booking"
            st.rerun()
            
    # Footer
    st.markdown("""
    <div class="footer">
        &copy; 2025 All rights reserved to Native French Speakers.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    import socket
    # Print some diagnostic info
    print(f"Hostname: {socket.gethostname()}")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    print("Attempting to start Streamlit on port 8501...")
    main()