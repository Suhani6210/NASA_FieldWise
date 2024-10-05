# Crop Monitoring and Irrigation Management Web App

### Overview
This web application integrates satellite imagery, remote sensing, and geospatial data to provide crop monitoring and irrigation management tools for farmers. The app allows users to visualize NDVI maps, manage irrigation based on evapotranspiration (ET) values, and monitor various agricultural factors in real-time.

### Features
- **Introduction Page**: Describes the aim of the project and the benefits of data-driven farming.
- **Irrigation Monitoring**: Monitors soil moisture and water usage using ET values.
- **Maps Visualization**: Visualizes NDVI maps for crop health monitoring, along with other agricultural maps such as soil moisture.
- **Unified Farm Overview**: Displays an interactive map for selecting farm boundaries and visualizing region-specific agricultural data.

### Tech Stack
- **Frontend**: Built using [Streamlit](https://streamlit.io/), a fast and user-friendly Python web framework.
- **Geospatial Data**: Uses satellite data for crop monitoring (e.g., NDVI, soil moisture).
- **Mapping Tools**: Implements mapping using [leafmap](https://leafmap.org/), a geospatial data visualization tool.

### How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app using Streamlit:
    ```bash
    streamlit run app.py
    ```

4. The app should open automatically in your browser at `http://localhost:8501/`.

## 📂 Project Structure

```bash
├── parts/                    
│   ├── Introduction.py       # Introduction page logic
│   ├── irrigation.py         # Irrigation monitoring page logic
│   ├── maps.py               # Mapping page logic (for visualizing farm data)
│   ├── NDVI.py               # NDVI calculations and visualization logic
│   ├── sidebar.py            # Sidebar navigation logic
├── statics/                  
│   ├── images/               # Static images used in the app (logos, icons, etc.)
│   ├── styles.css            # Custom styles for the app (e.g., colors, fonts)
├── utils/                    
│   ├── data_processing.py     # Utility functions for data processing
│   ├── satellite_data.py      # Functions to handle satellite data fetching and parsing
├── .gitignore                # Git configuration to ignore files like env or pycache
├── app.py                    # Main app file to run the entire web app
├── requirements.txt          # Dependencies needed to run the project
├── README.md                 # Project documentation
└── styles.css                # Custom CSS styling for the web application





