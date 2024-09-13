import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval

# Define the HTML and JavaScript
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Streamlit JS Eval Example</title>
</head>
<body>
    <h1>Saving Data to Session Storage</h1>
    <script>
        // JavaScript code to calculate a data series and save it to session storage
        const dataSeries = [1, 2, 3, 4, 5].map(x => x * 2);
        sessionStorage.setItem('dataSeries', JSON.stringify(dataSeries));
        // Print the data series to the console for debugging
        console.log("Data Series:", dataSeries);
        // Display the data series on the HTML page for debugging
        document.write("<p>Data Series: " + dataSeries + "</p>");
    </script>
</body>
</html>
"""

# Embed the HTML and JavaScript in the Streamlit app
components.html(html_code, height=200)

# Use streamlit_js_eval to retrieve the data series from session storage
data_series = streamlit_js_eval(js_expressions='JSON.parse(sessionStorage.getItem("dataSeries"))', key='DATA_SERIES')

if st.button("print", key = 'printbutton'):
    # Display the retrieved data series in Streamlit
    st.write("Data Series from JavaScript:", data_series)

    # Visualize the data series using Streamlit's charting capabilities
    if data_series:
        st.line_chart(data_series)
    else:
        st.write("No data series retrieved. Check the console for errors.")
