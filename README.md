# Client Geolocation and Visualization

This project geocodes client addresses and visualizes their locations on an interactive map using Streamlit and Folium. The addresses are extracted from a Google Sheet, geocoded into latitude and longitude, and then displayed on a map with options for heat maps, markers, or marker clusters.

## Files in the Project
 - .gitignore: Gitignore file to exclude unnecessary files and folders.
 - Client Data - df.csv: Contains client data with geocoded latitude and longitude information.
 - Client Data - gdf.csv: A GeoDataFrame version of the client data, stored in CSV format.
 - addressCoordinates.py: Python script for fetching, geocoding, and cleaning client address data.
 - app.py: Streamlit app for visualizing the client data on an interactive map.

## Dependencies
The following Python libraries are required to run the scripts:
 - pandas
 - numpy
 - geopandas
 - geopy
 - gspread
 - folium
 - streamlit
 - streamlit_folium
 - math

You can install the dependencies using pip:
`pip install pandas numpy geopandas geopy gspread folium streamlit streamlit_folium`
## Setup
### 1. Geocoding Client Data
The addressCoordinates.py script performs the following tasks:
 - Connects to a Google Sheet using the gspread library to retrieve client data.
 - Filters clients with the 'Client?' column marked as 'TRUE'.
 - Uses the geopy library to geocode addresses based on the client's home street, city, state, and postal code.
 - The latitude and longitude are added to the DataFrame.
 - Geocoded client data is saved in two CSV files: Client Data - df.csv (with geocoordinates) and Client Data - gdf.csv (as a GeoDataFrame).
### 2. Visualizing Client Data
The app.py script provides an interactive map where you can visualize the geocoded client data:
 - The map is generated using Folium with a default zoom level and position based on the mean latitude and longitude of the clients.
 - You can choose to display the data as:
   - Markers: Pins representing client locations.
[streamlit-app-2025-02-24-01-02-70.webm](https://github.com/user-attachments/assets/b90bcd22-1f71-4701-9b68-eccfeea97aaf)


   - Heat Map: A heatmap visualization of client density.
[streamlit-app-2025-02-24-01-02-70 (1).webm](https://github.com/user-attachments/assets/62ebca25-b111-4678-81ce-6a26aba96d02)


   - Marker Clusters: A clustered view for better handling large sets of data points.
[streamlit-app-2025-02-24-01-02-77.webm](https://github.com/user-attachments/assets/7645a224-e9b9-4d9a-9483-a21b71bb3615)


### 3. Running the Streamlit App
To run the app, use the following command:
`streamlit run app.py`
This will start a local web server and you can open your browser to interact with the map and explore the client data.
### Notes
 - Ensure you have a valid creds.json file for Google Sheets authentication.
 - The `addressCoordinates.py` script assumes a Google Sheet with a structure containing columns like `Home Street`, `Home City`, `Home State`, `Home Postal Code`, and `Client?`.
 - The map will display various options to adjust the view and see client data in different formats.
