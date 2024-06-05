import streamlit as st
from streamlit_float import *
from streamlit_folium import st_folium
import folium
import random
import time

# Set up the page layout
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
# st.title("MEAI (Beta)")


# Initialize session state variables
if 'travel_month' not in st.session_state:
    st.session_state.travel_month = ''
if 'travel_days' not in st.session_state:
    st.session_state.travel_days = 0
if 'preference' not in st.session_state:
    st.session_state.preference = ''
if 'additional_question' not in st.session_state:
    st.session_state.additional_preference = ''
if 'budget' not in st.session_state:
    st.session_state.budget = 10000
if 'self_driving' not in st.session_state:
    st.session_state.self_driving = 5
if 'weather' not in st.session_state:
    st.session_state.weather = 5
if 'schedule' not in st.session_state:
    st.session_state.schedule = 5
if 'language' not in st.session_state:
    st.session_state.language = ''
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'chatbot_messages' not in st.session_state:
    st.session_state.chatbot_messages = []

famous_sites = {
    "Matterhorn Glacier Paradise": [45.9763, 7.6586],
    # Add more sites here if needed
}
# Function to display the main page
def main_page():
    st.markdown("""
            <style>
                .css-1d391kg {
                    width: 250px !important;
                }
                .css-1e5imcs {
                    margin-left: 260px !important;
                }
                .explore-heading {
                    padding-top: 20px;
                    text-align: center;
                    margin-left: 50px; /* Add space before the word "Explore" */
                    font-size: 20pt;
                    font-weight: 600
                }
                .preference-heading {
                    font-size: 24pt;
                    font-weight: 800;
                }
                .sidebar-icons {
                    font-size: 24px;
                    margin-right: 10px;
                }
            </style>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

        """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 3])

    with col1:
        # st.markdown("### Your preference for this trip")
        st.markdown('<div class="preference-heading">Your preference for this trip</div>', unsafe_allow_html=True)

        travel_month = st.selectbox("Which month do you plan to travel?", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        travel_days = st.number_input("For how many days?",
                                      min_value=1, max_value=31, step=1)

        preference = st.selectbox("Do you prefer natural or cultural attractions?", [
            "natural", "cultural"
        ])

        if preference == "natural":
            additional_preference = st.selectbox("What type of natural attractions do you prefer?",
                                                 ["mountains", "beaches", "lakes/rivers/waterfalls",
                                                  'forests', 'desserts', "others"])
        elif preference == "cultural":
            additional_preference = st.selectbox("What type of cultural attractions do you prefer?",
                                                 ["historical", "museums", "ethnic neighbourhoods",
                                                  "festivals/events", 'others'])

        budget = st.number_input("How much is your budget?",
                                 min_value=10, max_value=100000, step=1)

        self_driving = st.number_input('Do you prefer self-driving? ' + \
                                       '0: not prefer at all, 10: extremely prefer.',
                                       min_value=0, max_value=10, step=1)

        weather = st.number_input('Are you sensitive to weather?' + \
                                  '0: insensitive, 10: very sensitive.',
                                  min_value=0, max_value=10, step=1)

        schedule = st.number_input('Do you prefer a tight or loose schedule? ' + \
                                   '0: very loose, 10：very tight.',
                                   min_value=0, max_value=10, step=1)

        langs = ['English', 'Spanish', 'Chinese', 'Arabic', 'French', 'German',
                 'Hindi', 'Portuguese', 'Bengali', 'Russian', 'Indonesian',
                 'Turkish', 'Urdu', 'Japanese', 'Greek', 'Croatian', 'Korean',
                 'Telugu', 'Malay', 'Italian', 'Romansh', 'Dutch', 'Polish',
                 'Thai', 'Others']

        language = st.selectbox("Which language do you speak?", langs)

        st.markdown('<div class="submit-button">', unsafe_allow_html=True)
        if st.button("Submit", disabled=not (travel_month and travel_days and preference
                                             and additional_preference and budget
                                             and (0 <= self_driving <= 10)
                                             and (0 <= weather <= 10)
                                             and (0 <= schedule <= 10)
                                             and language)

                     ):
            st.session_state.page = "results"
            st.session_state.travel_month = travel_month
            st.session_state.travel_days = travel_days
            st.session_state.preference = preference
            st.session_state.additional_preference = additional_preference
            st.session_state.budget = budget
            st.session_state.self_driving = self_driving
            st.session_state.weather = weather
            st.session_state.schedule = schedule
            st.session_state.language = language
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # st.markdown('<div class="explore-padding">', unsafe_allow_html=True)
        # st.markdown('<div class="explore-padding">', unsafe_allow_html=True)
        # st.markdown("### Explore destinations")
        st.markdown('<div class="explore-heading"> Explore destinations</div>', unsafe_allow_html=True)

        st.markdown("""
            <style>
            .column-padding {
                padding-top: 50px !important;
            }
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
        st.markdown('<div class="column-padding">', unsafe_allow_html=True)
        # st.markdown(unsafe_allow_html=True)
        st.image("images/pic1.jpg", caption="Horseshoe Bend", use_column_width=True, output_format="auto")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div class='small-images-container'>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            st.image("images/pic2.jpg", caption="Santa Monica Pier", use_column_width=True)
        with col4:
            st.image("images/pic3.jpg", caption="Grand Rapids", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


def chat_content():
    if "prompt" in st.session_state:
        st.session_state.prompt = st.session_state.prompt


# Function to display the results page
def results_page():
    float_init(theme=True, include_unstable_primary=False)  # to make the chatbot input text goes down

    st.markdown("""
        <style>
            .css-1d391kg {
                width: 250px !important;
            }
            .css-1e5imcs {
                margin-left: 260px !important;
            }
            .explore-heading {
                padding-top: 20px;
                text-align: center;
                margin-left: 50px; /* Add space before the word "Explore" */
                font-size: 20pt;
                font-weight: 600
            }
            .preference-heading {
                font-size: 24pt;
                font-weight: 800;
            }
            .sidebar-icons {
                font-size: 24px;
                margin-right: 10px;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col2:
        st.markdown('<div class="explore-heading"> Explore destinations</div>', unsafe_allow_html=True)

        m = folium.Map(location=[46.8182, 8.2275], zoom_start=8)
        for site, coordinates in famous_sites.items():
            folium.Marker(
                location=coordinates,
                popup=f'<b style="font-size:16px;">{site}</b>'
            ).add_to(m)

        st_folium(m, width=700, height=500)

    if 'contents' not in st.session_state:
        st.session_state['contents'] = [("robot",
                                         "Based on your preferences, needs and constraints, here are the best destinations:\n1. Swiss Alps [95]\n2. Canadian Rockies [83]\n3. Patagonia [80].\n\nDo you have any other questions?")
                                        ]

    # with col1:
    #     with st.container(border=True):
    #         with st.container():
    #             st.chat_input(key='content', on_submit=chat_content)
    #             button_b_pos = "0rem"
    #             button_css = float_css_helper(width="2.2rem", bottom=button_b_pos, transition=0)
    #             float_parent(css=button_css)
    #
    #         if st.session_state.contents:
    #             for role, content in st.session_state.contents:
    #                 if role == 'user':
    #                     with st.chat_message(name='User', avatar='👤'):
    #                         st.write(content)
    #                 elif role == 'robot':
    #
    #                     if content == st.session_state.contents[-1][1] and len(st.session_state['contents']) > 1:
    #                         with st.chat_message(name='MEAI', avatar='🤖'):
    #                             st.write_stream(stream_the_text(content))
    #                     else:
    #                         with st.chat_message(name='MEAI', avatar='🤖'):
    #                             st.write(content)

    with col1:
        for role, content in st.session_state['contents']:
            if role == 'user':
                with st.chat_message(name='User', avatar='👤'):
                    st.write(content)
            elif role == 'robot':
                if content == "VIDEO_RESPONSE":
                    st.video("https://www.youtube.com/watch?v=_88XGkSaWos")
                else:
                    st.write(content)

        if prompt := st.chat_input("Your question"):
            st.session_state['contents'].append(('user', prompt))
            chatbot_response = generate_chatbot_response(prompt)
            st.session_state['contents'].append(('robot', chatbot_response))
            st.experimental_rerun()

def chat_content():
    user_message = st.session_state.content
    st.session_state['contents'].append(('user', user_message))
    chatbot_response = generate_chatbot_response(user_message)
    st.session_state['contents'].append(('robot', chatbot_response))

def generate_chatbot_response(user_input):
    if user_input.lower() == "why":
        return "VIDEO_RESPONSE"
    else:
        return "This is what you sent: " + user_input


def stream_the_text(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)


with st.sidebar:
    st.markdown("## MEAI (Beta)")
    st.markdown('<button class="sidebar-icons"><i class="fas fa-comments"></i></button> Chats', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-bell"></i></button> Notifications',
                unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-thumbs-up"></i></button> Likes', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-arrow-circle-up"></i></button> Up Next',
                unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-search"></i></button> Explore', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-plus-circle"></i></button> Create',
                unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-comment-alt"></i></button> New Chat',
                unsafe_allow_html=True)

# Main content layout
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "results":
    results_page()