# =========================
# Python 3.10.11
# =========================

import streamlit as st
import views.detect_view as dv
import views.event_view as ev

# Streamlit configuration
st.set_page_config(
    page_title="Application for Detecting Littering Actions using YOLO",
    page_icon=":wastebasket:",
)

# Sidebar Title
st.sidebar.title("Dashboard")

# Sidebar Page Navigation
page = st.sidebar.selectbox("Select Page", ["Detect", "Events"])

# Load the selected page content
if page == "Detect":
    dv.app()  # Run the detect page content
elif page == "Events":
    ev.app()  # Run the events page content
