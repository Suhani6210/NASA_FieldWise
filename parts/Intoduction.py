import streamlit as st

def intro():
    st.markdown(
        """
        <h1 style='color: white; font-size: 40px; font-family: 'Georgia', serif; text-align: center; margin-top: 10px;'>
        Introduction
        </h1>

        <h2>Aim</h2>
        <p>Integrating technologies like satellite imagery and remote sensing into agriculture to help farmers respond proactively to environmental changes, increasing yields and cutting costs.</p>

        <h2>The "Why" behind it</h2>
        <p>Data-driven farming optimizes everything—from planting to irrigation and 
        pest management. It helps farmers make smarter decisions, use resources 
        efficiently, reduce waste, and get the most out of fertilizers, pesticides, 
        and water. Informed decisions are based on various data sources, tools, models, 
        and maps.</p>

        <h2>How to Make Informed Agricultural Decisions</h2>
        <p>Earth observation data is a game-changer for farmers and land managers. 
        Satellite imagery and remote sensing offer real-time insights into crop health, 
        water usage, and soil conditions, enabling better, faster decisions.</p>

        <h2>What We Do</h2>
        <p>Our web app integrates Earth observation data with:</p>
            <ul>
                <li>Irrigation management using ET (Evapotranspiration) values to fine-tune water usage.</li>
                <li>NDVI (Normalized Difference Vegetation Index) maps for monitoring crop vitality.</li>
                <li>Comparisons of agricultural maps (like soil moisture and vegetation) to provide a full field overview.</li>
            </ul>




        """, unsafe_allow_html=True
    )
    # st.title("Introduction")
    # st.write("Integrating technologies like satellite imagery and remote sensing into agriculture helps farmers respond proactively to environmental changes, increasing yields and cutting costs.")
