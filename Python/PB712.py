# Q712 Build a Streamlit app with:
# - Sidebar to select a country from a dropdown (India, USA, UK, Canada)
# - Number input for Total Population
# - Number input for Vaccinated People
# - A button that, when clicked, calculates and displays the vaccination percentage
# - Display results with a progress bar and a success/warning message depending on whether the vaccination rate is above
# 70%
import streamlit as st
import time
st.sidebar.title("Vaccination data")
con=st.sidebar.selectbox("Country",["India","USA","UK","Canada"])
pop=st.sidebar.number_input("Enter total population:")
vp=st.sidebar.number_input("Enter number of vaccinated people:")
if st.sidebar.button("Get vaccinated percentage"):
    progress=st.sidebar.progress(0)
    with st.sidebar.spinner("Progress..."):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    pr=int(vp)/int(pop)*100
    st.title("Vaccinated people's data")
    st.write(f"Country:{con}")
    st.write(f"Population:{pop}")
    st.write(f"Vaccinated people:{vp}")
    st.write(f"Vaccinated percentage:{pr}")
    if pr>70:
        st.success("More than 70% population is vaccinated")
    else:
        st.warning("Less than 70% population is vaccinated")
else:
    st.title("Vaccinated people's data")
    st.write(f"Country:{con}")
    st.write(f"Population:{pop}")
    st.write(f"Vaccinated people:{vp}")
