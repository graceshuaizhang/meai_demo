import streamlit as st
from streamlit_float import *
import random
import time

# Set up the page layout
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

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


def chat_content():
    user_message = st.session_state.content
    st.session_state['contents'].append(('user', user_message))
    chatbot_response = generate_chatbot_response(user_message)
    st.session_state['contents'].append(('robot', chatbot_response))


def generate_chatbot_response(user_input):
    if user_input.lower() == "why":
        return '<div style="display: flex; flex-direction: row; align-items: center;"><div style="flex: 1;">one</div><div style="flex: 1;"><iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>'
    elif user_input.lower() == "plan":
        return "two"
    else:
        return "This is what you sent: " + user_input


def stream_the_text(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)


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

    col1 = st.columns([1])[0]

    if 'contents' not in st.session_state:
        st.session_state['contents'] = [("robot",
                                         "Based on your preferences, needs and constraints, here are the best destinations:\n1. Swiss Alps [95]\n2. Canadian Rockies [83]\n3. Patagonia [80].\n\nDo you have any other questions?")
                                        ]

    with col1:
        with st.container(border=True):
            for role, content in st.session_state.contents:
                if role == 'user':
                    with st.chat_message(name='User', avatar='👤'):
                        st.write(content)
                elif role == 'robot':
                    if content.startswith('<div'):
                        st.components.v1.html(content, height=380)
                    else:
                        with st.chat_message(name='MEAI', avatar='🤖'):
                            st.write(content)

            st.chat_input(key='content', on_submit=chat_content)

with st.sidebar:
    st.markdown("## MEAI (Beta)")
    st.markdown('<button class="sidebar-icons"><i class="fas fa-comments"></i></button> Chats', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-bell"></i></button> Notifications', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-thumbs-up"></i></button> Likes', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-arrow-circle-up"></i></button> Up Next', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-search"></i></button> Explore', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-plus-circle"></i></button> Create', unsafe_allow_html=True)
    st.markdown('<button class="sidebar-icons"><i class="fas fa-comment-alt"></i></button> New Chat', unsafe_allow_html=True)

# Main content layout
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "results":
    results_page()
