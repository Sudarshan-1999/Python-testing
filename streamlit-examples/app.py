# # import streamlit as st
# # import pandas as pd
# # import numpy as np 
# # import time


# # st.markdown("# Main page 🎈")
# # st.sidebar.markdown("# Main page 🎈")

# # fp = st.sidebar.file_uploader("") 
# # # dataframe = pd.DataFrame(
# # #     np.random.randn(10, 20),
# # #     columns=('col %d' % i for i in range(20)))

# # # st.dataframe(dataframe.style.highlight_max(axis=0))


# # # dataframe = pd.DataFrame(
# # #     np.random.randn(10, 20),
# # #     columns=('col %d' % i for i in range(20)))
# # # st.table(dataframe)

# # # Draw a Line chart

# # # chart_data = pd.DataFrame(
# # #      np.random.randn(20, 3),
# # #      columns=['a', 'b', 'c'])

# # # st.line_chart(chart_data)

# # # Plot a Map 
# # # map_data = pd.DataFrame(
# # #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
# # #     columns=['lat', 'lon'])

# # # st.map(map_data)

# # x = st.slider('x')  # 👈 this is a widget
# # st.write(x, 'squared is', x * x)
# # st.text_input("Your name", key="name")

# # # You can access the value at any point with:
# # st.session_state.name


# # if st.checkbox('Show dataframe'):
# #     chart_data = pd.DataFrame(
# #     #    np.random.randn(20, 3),
# #        columns=['a', 'b', 'c']) 
    

# #     chart_data  

# # df = pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column': [10, 20, 30, 40]
# #     })

# # option = st.selectbox(
# #     'Which number do you like best?',
# #      df['first column'])

# # 'You selected: ', option

# # # Add a selectbox to the sidebar:
# # add_selectbox = st.sidebar.selectbox(
# #     'How would you like to be contacted?',
# #     ('Email', 'Home phone', 'Mobile phone')
# # )

# # # Add a slider to the sidebar:
# # add_slider = st.sidebar.slider(
# #     'Select a range of values',
# #     0.0, 100.0, (25.0, 75.0)
# # )


# # left_column, right_column = st.columns(2)
# # # You can use a column just like st.sidebar:
# # left_column.button('Press me!')

# # # Or even better, call Streamlit functions inside a "with" block:
# # with right_column:
# #     chosen = st.radio(
# #         'Sorting hat',
# #         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
# #     st.write(f"You are in {chosen} house!")



# # 'Starting a long computation...'

# # # Add a placeholder
# # latest_iteration = st.empty()
# # bar = st.progress(0)

# # for i in range(100):
# #   # Update the progress bar with each iteration.
# #   latest_iteration.text(f'Iteration {i+1}')
# #   bar.progress(i + 1)
# #   time.sleep(0.1)

# # '...and now we\'re done!'

# import streamlit as st

# def intro():
#     import streamlit as st

#     st.write("# Welcome to Streamlit! 👋")
#     st.sidebar.success("Select a demo above.")

#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.

#         **👈 Select a demo from the dropdown on the left** to see some examples
#         of what Streamlit can do!

#         ### Want to learn more?

#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)

#         ### See more complex demos

#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )

# def mapping_demo():
#     import streamlit as st
#     import pandas as pd
#     import pydeck as pdk

#     from urllib.error import URLError

#     st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
#     st.write(
#         """
#         This demo shows how to use
# [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
# to display geospatial data.
# """
#     )

#     @st.cache_data
#     def from_data_file(filename):
#         url = (
#             "http://raw.githubusercontent.com/streamlit/"
#             "example-data/master/hello/v1/%s" % filename
#         )
#         return pd.read_json(url)

#     try:
#         ALL_LAYERS = {
#             "Bike Rentals": pdk.Layer(
#                 "HexagonLayer",
#                 data=from_data_file("bike_rental_stats.json"),
#                 get_position=["lon", "lat"],
#                 radius=200,
#                 elevation_scale=4,
#                 elevation_range=[0, 1000],
#                 extruded=True,
#             ),
#             "Bart Stop Exits": pdk.Layer(
#                 "ScatterplotLayer",
#                 data=from_data_file("bart_stop_stats.json"),
#                 get_position=["lon", "lat"],
#                 get_color=[200, 30, 0, 160],
#                 get_radius="[exits]",
#                 radius_scale=0.05,
#             ),
#             "Bart Stop Names": pdk.Layer(
#                 "TextLayer",
#                 data=from_data_file("bart_stop_stats.json"),
#                 get_position=["lon", "lat"],
#                 get_text="name",
#                 get_color=[0, 0, 0, 200],
#                 get_size=15,
#                 get_alignment_baseline="'bottom'",
#             ),
#             "Outbound Flow": pdk.Layer(
#                 "ArcLayer",
#                 data=from_data_file("bart_path_stats.json"),
#                 get_source_position=["lon", "lat"],
#                 get_target_position=["lon2", "lat2"],
#                 get_source_color=[200, 30, 0, 160],
#                 get_target_color=[200, 30, 0, 160],
#                 auto_highlight=True,
#                 width_scale=0.0001,
#                 get_width="outbound",
#                 width_min_pixels=3,
#                 width_max_pixels=30,
#             ),
#         }
#         st.sidebar.markdown("### Map Layers")
#         selected_layers = [
#             layer
#             for layer_name, layer in ALL_LAYERS.items()
#             if st.sidebar.checkbox(layer_name, True)
#         ]
#         if selected_layers:
#             st.pydeck_chart(
#                 pdk.Deck(
#                     map_style="mapbox://styles/mapbox/light-v9",
#                     initial_view_state={
#                         "latitude": 37.76,
#                         "longitude": -122.4,
#                         "zoom": 11,
#                         "pitch": 50,
#                     },
#                     layers=selected_layers,
#                 )
#             )
#         else:
#             st.error("Please choose at least one layer above.")
#     except URLError as e:
#         st.error(
#             """
#             **This demo requires internet access.**

#             Connection error: %s
#         """
#             % e.reason
#         )

# def plotting_demo():
#     import streamlit as st
#     import time
#     import numpy as np

#     st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
#     st.write(
#         """
#         This demo illustrates a combination of plotting and animation with
# Streamlit. We're generating a bunch of random numbers in a loop for around
# 5 seconds. Enjoy!
# """
#     )

#     progress_bar = st.sidebar.progress(0)
#     status_text = st.sidebar.empty()
#     last_rows = np.random.randn(1, 1)
#     chart = st.line_chart(last_rows)

#     for i in range(1, 101):
#         new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#         status_text.text("%i%% Complete" % i)
#         chart.add_rows(new_rows)
#         progress_bar.progress(i)
#         last_rows = new_rows
#         time.sleep(0.05)

#     progress_bar.empty()

#     # Streamlit widgets automatically run the script from top to bottom. Since
#     # this button is not connected to any other logic, it just causes a plain
#     # rerun.
#     st.button("Re-run")


# def data_frame_demo():
#     import streamlit as st
#     import pandas as pd
#     import altair as alt

#     from urllib.error import URLError

#     st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
#     st.write(
#         """
#         This demo shows how to use `st.write` to visualize Pandas DataFrames.

# (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
# """
#     )

#     @st.cache_data
#     def get_UN_data():
#         AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#         df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#         return df.set_index("Region")

#     try:
#         df = get_UN_data()
#         countries = st.multiselect(
#             "Choose countries", list(df.index), ["China", "United States of America"]
#         )
#         if not countries:
#             st.error("Please select at least one country.")
#         else:
#             data = df.loc[countries]
#             data /= 1000000.0
#             st.write("### Gross Agricultural Production ($B)", data.sort_index())

#             data = data.T.reset_index()
#             data = pd.melt(data, id_vars=["index"]).rename(
#                 columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#             )
#             chart = (
#                 alt.Chart(data)
#                 .mark_area(opacity=0.3)
#                 .encode(
#                     x="year:T",
#                     y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                     color="Region:N",
#                 )
#             )
#             st.altair_chart(chart, use_container_width=True)
#     except URLError as e:
#         st.error(
#             """
#             **This demo requires internet access.**

#             Connection error: %s
#         """
#             % e.reason
#         )

# page_names_to_funcs = {
#     "—": intro,
#     "Plotting Demo": plotting_demo,
#     "Mapping Demo": mapping_demo,
#     "DataFrame Demo": data_frame_demo
# }

# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()

import streamlit as st
# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

# text_contents = '''This is some text'''
# st.download_button('Download some text', text_contents)

# with open(r"D:\python-exercise\streamlit-examples\flower.jpg", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="flower.jpg",
#             mime="image/png"
#           )
# video_file = open('./action.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

# from PIL import Image

# image = Image.open('./flower.jpg')

# st.image(image, caption='Sunrise by the mountains')
# col1, col2, col3 = st.columns(3)

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)