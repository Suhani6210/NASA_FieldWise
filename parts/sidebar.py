import streamlit as st

def sidebar_navigation():
    # Initialize session state for the toggle button
    if 'show_team' not in st.session_state:
        st.session_state.show_team = False

    # Create an "i" button to toggle team member display
    col1, col2 = st.sidebar.columns([1, 8])
    
    with col1:
        
        # Toggle the value of show_team in session_state when the button is clicked
        if st.button("ℹ", help="Click here for information", key="info_button"):
            st.session_state.show_team = not st.session_state.show_team

    # If the "i" button is clicked, show the expander with team member names
    if st.session_state.show_team:
        with st.sidebar.expander("Team Members", expanded=True):
            st.markdown(
                """
                <ul style="list-style-type: none; padding-left: 0;">
                    <li>👤 Parth Modi</li>
                    <li>👤 Niwesh</li>
                    <li>👤 Siddhi Pogakwar</li>
                    <li>👤 Manish</li>
                    <li>👤 Suhani Sharma</li>
                    <li>👤 Sarthak Prajapati</li>
                </ul>
                """,
                unsafe_allow_html=True
            )
    
    # Create three columns in the sidebar to center the image
    col1, col2, col3 = st.sidebar.columns([1, 8, 1])
    with col1:
        st.write("")
    with col2:
        st.image('statics/logo4.png', use_column_width=True)
    with col3:
        st.write("")
    
    # Sidebar title and navigation
    st.sidebar.markdown(
        "<div style='text-align: center; font-size:24px; font-weight:bold;'>SENTINAL KINGS</div>",
        unsafe_allow_html=True
    )
    st.sidebar.title("Navigation")
    
    # Create sidebar navigation options
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Introduction", "Irrigation Monitoring","NDVI Map","Soil Moisture"]
    )

    return page