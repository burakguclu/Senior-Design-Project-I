import streamlit as st
import json
from streamlit_pdf_viewer import pdf_viewer

def display_pdf(file_path):
    pdf_viewer(input=file_path)

def home():
    st.title("Post-Disaster Communication")
    st.write("""
        ## Welcome to the Post-Disaster Communication Project Webpage!

        ### Introduction
        This project is a disaster response system designed to enhance safety and communication during emergency scenarios. It integrates IoT sensors to detect anomalies such as seismic waves, temperature fluctuations, or rising water levels. Once a potential hazard is detected, notifications are dispatched to a centralized web application and mobile users. Mobile users receive an "Are You Safe?" alert and can respond accordingly. If a user marks themselves as unsafe or fails to respond within a specified timeframe, the system escalates by displaying their details (name, location, and contact information) on a monitor for further action. The system also notifies their pre-designated emergency contacts.

        ### Objectives
        - Provide easy access to critical project documents, including proposals, specifications, analysis reports, and high-level designs.
        - Track the status and priority of tasks in an intuitive and interactive table.
        - Enhance collaboration and reduce delays in task execution.
        - Support project stakeholders in making informed decisions through real-time data visibility.

        ### Goals
        - To enable seamless navigation through different project components.
        - To integrate dynamic task management features.
        - To provide download options for detailed PDF reports.

        ### Disaster Response System Overview
        Natural disasters and unexpected emergencies are among the most important risks that threaten human life. In regions like Turkey, frequently affected by earthquakes, rapid access to critical information and coordination of emergency response teams is vital. The main purpose of this system is to detect risk factors through IoT sensors during a disaster and to collect rapid feedback through notifications sent via a mobile application. Users' safety statuses are shared with their relatives and emergency response teams to ensure prompt action.

        ### Features
        - **IoT Sensors**: Monitors environmental changes (e.g., seismic waves, temperature, water levels) to detect potential disasters.
        - **Mobile Application**: Sends "Are You Safe?" notifications, collects user responses, and provides options to add emergency contacts.
        - **Web Application**: Centralized platform for managing disaster data, monitoring user responses, and coordinating emergency teams.
        - **Emergency Notifications**: Automatically escalates unresponsive users' details to emergency teams for immediate action.

        ### Working Principle
        1. IoT sensors continuously monitor for anomalies.
        2. When a hazard is detected, the system sends alerts to the web application and mobile users.
        3. Users respond to the "Are You Safe?" notification with options like "I am safe" or "I am not safe."
        4. Unresponsive or unsafe users are flagged, and their details are sent to emergency teams and relatives.
        5. Emergency teams use the centralized web platform to manage responses and provide aid.

        ### Benefits
        - Real-time monitoring and communication during disasters.
        - Accurate and rapid information flow to ensure safety and peace of mind.
        - Efficient management of emergency resources to minimize delays.

        Use the menu on the left to explore the features of this application.
    """)

def project_proposals():
    st.title("491 - Project Proposal")
    display_pdf("PostdisasterCommunication-ProjectProposal_updated.pdf")
    
def project_specifications_report():
    st.title("491 - Project Specifications Report")
    display_pdf("PostdisasterCommunication-ProjectSpecificationsReport.pdf")

def project_analysis_report():
    st.title("491 - Project Analysis Report")
    display_pdf("PostDisasterCommunication-ProjectAnalysisReport.pdf")

def high_level_design_report():
    st.title("491 - High Level Design Report")
    display_pdf("PostdisasterCommunication-HighLevelDesignReport.pdf")

def low_level_design_report():
    st.title("492 - Low Level Design Report")
    display_pdf("PostdisasterCommunication-LowLevelDesignReport.pdf")

def test_plan_report():
    st.title("492 - Test Plan Report")
    display_pdf("PostdisasterCommunication-TestPlanReport.pdf")

def backlog():
    with open('backlog.json', 'r') as file:
        data = json.load(file)

    st.title("Project Backlog")
    st.dataframe(data, height=1508)

st.set_page_config(page_title="Project Management App", layout="wide", initial_sidebar_state="collapsed")

st.sidebar.title("Menu")
page = st.sidebar.radio("Select a Page", 
                         ["Home", "491 - Project Proposal", "491 - Project Specifications Report", "491 - Project Analysis Report", "491 - High Level Design Report", "492 - Low Level Design Report", "492 - Test Plan Report", "Backlog"])

if page == "Home":
    home()
elif page == "491 - Project Proposal":
    project_proposals()
elif page == "491 - Project Specifications Report":
    project_specifications_report()
elif page == "491 - Project Analysis Report":
    project_analysis_report()
elif page == "491 - High Level Design Report":
    high_level_design_report()
elif page == "492 - Low Level Design Report":
    low_level_design_report()
elif page == "492 - Test Plan Report":
    test_plan_report()
elif page == "Backlog":
    backlog()
