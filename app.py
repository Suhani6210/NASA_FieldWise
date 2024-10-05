import streamlit as st
from parts.sidebar import sidebar_navigation
from parts.irrigation import irrigation_monitoring
from parts.irrigation import maps_visualization
from parts.soilMoistue import on_page
from parts.Intoduction import intro
from parts.NDVI import webpage

# Load custom CSS file to style the app
#page config 
st.set_page_config(page_title="Crop Monitoring",page_icon="🛰️",initial_sidebar_state="expanded")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file for custom styling
local_css("styles.css")

# Main function to handle page rendering
def main():
    # Get the selected page from sidebar navigation
    page = sidebar_navigation()


    # Render the appropriate page based on selection
    if page=="Introduction":
        intro()
    elif page == "Irrigation Monitoring":
        maps_visualization()
        irrigation_monitoring()
    elif page== "NDVI Map":
        webpage()
    elif page=="Soil Moisture":
        on_page()
    # elif page == "Irrigation Mapping":
    #     irrigation_mapping()
    # elif page == "Farm Maps":
    #     maps_visualization()  # Unified map visualization page


# Run the app
if __name__ == "__main__":
    main()
