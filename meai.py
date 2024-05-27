import streamlit as st

# Set up the page layout
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Initialize session state variables
if 'travel_month' not in st.session_state:
    st.session_state.travel_month = ''
if 'travel_days' not in st.session_state:
    st.session_state.travel_days = 0
if 'preference' not in st.session_state:
    st.session_state.preference = ''
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to display the main page
def main_page():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("## Questions")
        
        travel_month = st.selectbox("When do you plan to travel?", [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ])
        
        travel_days = st.number_input("For how many days?", min_value=1, max_value=31, step=1)

        preference = st.text_input("Do you prefer natural or cultural attractions this time?")

        if st.button("Submit", disabled=not (travel_month and travel_days and preference)):
            st.session_state.page = "results"
            st.session_state.travel_month = travel_month
            st.session_state.travel_days = travel_days
            st.session_state.preference = preference
            st.rerun()

    with col2:
        st.markdown("""
            <style>
            .main-image {
                width: 100%;
                height: 300px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            .small-images-container {
                display: flex;
                justify-content: space-between;
                gap: 20px;
            }
            .small-image {
                width: 48%;
                height: 200px;
                object-fit: cover;
                border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.image("images/pic1.jpg", caption="Main Image", use_column_width=True, output_format="auto")
        
        st.markdown("<div class='small-images-container'>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            st.image("images/pic2.jpg", caption="Small Image 1", use_column_width=True)
        with col4:
            st.image("images/pic3.jpg", caption="Small Image 2", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Function to display the results page
def results_page():
    st.markdown("## Your Travel Preferences")
    st.write(f"Month of Travel: {st.session_state.travel_month}")
    st.write(f"Number of Days: {st.session_state.travel_days}")
    st.write(f"Preference: {st.session_state.preference}")

    if st.button("Go Back"):
        st.session_state.page = "main"
        st.experimental_rerun()

# Sidebar layout
with st.sidebar:
    st.markdown("## MEAI (Beta)")
    st.button("Chats")
    st.button("Notifications")
    st.button("Likes")
    st.button("Up Next")
    st.button("Explore")
    st.button("Create")
    st.button("New Chat")

# Main content layout
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "results":
    results_page()
