import streamlit as st
import pickle
import datetime
import pandas as pd

model = open("Model/rfmodel_flight.pkl", "rb") 
classifier  = pickle.load(model)


def perdicton_func(airline_,source, stop_,Dep_Time_in_hours,Dep_Time_in_minutes,Arrival_Time_in_hours,Arrival_Time_in_minutes,day, month,new_route,destination_,duration):
    prediction = classifier.predict([[airline_,source, stop_,Dep_Time_in_hours,Dep_Time_in_minutes,Arrival_Time_in_hours,Arrival_Time_in_minutes,day, month,new_route,destination_,duration]])
    return prediction

## Tabes 
Home, Prediction, Data_info, Visualization = st.tabs(["Home", "Prediction", "Dataset Overview", "Visualization"])
with Home:
    st.image('D://ML//flight-price-prediction//images//flight.jpg')

with Prediction:
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    c5, c6 = st.columns(2)
    c7, c8 = st.columns(2)
    c9, c10 = st.columns(2)
    c11, c12 = st.columns(2)

    with c1:
        airline = st.selectbox(
            'Select Aireline',
            ('Jet Airways',
            'IndiGo',
            'Air India',
            'Multiple carriers',
            'SpiceJet',
            'Vistara',
            'Air Asia',
            'GoAir',
            'Multiple carriers Premium economy',
            'Jet Airways Business',
            'Vistara Premium economy',
            'Vistara Premium economy',
            'Trujet'))
    if airline == 'Jet Airways':
        airline_ =  0
    elif airline == 'IndiGo':
        airline_ =  1
    elif airline == 'Air India':
        airline_ =  2
    elif airline == 'Multiple carriers':
        airline_ =  3
    elif airline == 'SpiceJet':
        airline_ =  4
    elif airline == 'Vistara':
        airline_ =  5
    elif airline == 'Air Asia':
        airline_ =  6
    elif airline == 'GoAir':
        airline_ =  7
    elif airline == 'Multiple carriers Premium economy':
        airline_ =  8
    elif airline == 'Jet Airways Business':
        airline_ =  9
    elif airline == 'Vistara Premium economy':
        airline_ =  10
    else:
        airline_ = 12 
    
    with c2:
        source_op = st.selectbox(
            'Select Source',
            ('Delhi', 'Kolkata', 'Banglore','Mumbai','Chennai'))
        if source_op == 'Delhi':
            source = 0
        elif source_op == 'Kolkata':
            source = 1
        elif source_op =='Banglore':
            source =2 
        elif source_op == 'Mumbai':
            source = 3
        else: source = 4
        
    with c3:
        stop = st.selectbox(
            'Select Total Stopes',
            ('non-stop', '1 stop', '2 stops', '3 stops', '4 stops'))
        if stop == 'non-stop':
            stop_= 0
        elif stop == '1 stop':
            stop_= 1
        elif stop == '2 stops':
            stop_= 2
        elif stop == '3 stops':
            stop_= 3
        else:  stop_= 4
            
    with c4:
        Dep_Time_in_hours = st.number_input("Enter Dep_Time_in_hours")

    with c5:
        Dep_Time_in_minutes = st.number_input("Enter Dep_Time_in_minutes:")
    with c6:
        Arrival_Time_in_hours = st.number_input("Enter Arrival_Time_in_hours:")
    with c7:
        Arrival_Time_in_minutes = st.number_input("Enter Arrival_Time_in_minutes:")
    
    with c8:
        # day = st.number_input('Enter Day')
        d = st.date_input("Select Date for flight")
        day = d.day
        month = d.month
        # st.write()

    with c9 :
        new_route_op = st.selectbox(
            'Select Route',
            ('DEL → BOM → COK', 'BLR → DEL', 'CCU → BOM → BLR', 'CCU → BLR', 'BOM → HYD', 'CCU → DEL → BLR','BLR → BOM → DEL', 'MAA → CCU', 'DEL → HYD → COK', 'DEL → JAI → BOM → COK', 'Other'))
        if new_route_op == 'DEL → BOM → COK':
            new_route =  0
        elif new_route_op == 'BLR → DEL':
            new_route =  1
        elif new_route_op == 'CCU → BOM → BLR':
            new_route =  2
        elif new_route_op == 'CCU → BLR':
            new_route =  3
        elif new_route_op == 'BOM → HYD':
            new_route =  4
        elif new_route_op == 'CCU → DEL → BLR':
            new_route =  5
        elif new_route_op == 'BLR → BOM → DEL':
            new_route =  6
        elif new_route_op == 'MAA → CCU':
            new_route =  7
        elif new_route_op == 'DEL → HYD → COK':
            new_route =  8
        elif new_route_op == 'DEL → JAI → BOM → COK':
            new_route =  9
        else:
            new_route =  10
            

    with c10:
        destination_op = st.selectbox(
            'Select Destination',
            ('Cochin', 'Banglore', 'Delhi', 'New Delhi', 'Hyderabad','Kolkata'))
        if destination_op == 'Cochin':
            destination_ = 0
        elif destination_op == 'Banglore':
            destination_ = 1
        elif destination_op == 'Delhi':
            destination_ =2
        elif destination_op == 'New Delhi':
            destination_ = 3
        elif destination_op == 'Hyderabad':
            destination_ = 4
        else: destination_ = 5
    with c12:
        duration = st.number_input("Enter Duration:")
    if st.button("Predict", type="primary"):
        result = perdicton_func(airline_,source, stop_,Dep_Time_in_hours,Dep_Time_in_minutes,Arrival_Time_in_hours,Arrival_Time_in_minutes,day, month,new_route,destination_,duration)
        st.write("The price for flight is: ", int(result))


with Data_info:
    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View Raw data"):
        df = pd.read_csv("D://ML//flight-price-prediction//Dataset//Data_Train.csv")
        st.dataframe(df)
        st.subheader("This Dataset")
    
    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        st.dataframe(df.describe().T)

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])         
            
            
with Visualization:
    # Set the page title
        st.title("Visualise Some Demographics")

        # Create a checkbox to show correlation heatmap
        with st.expander("Show the correlation heatmap"):
            st.subheader("Correlation Heatmap")
            st.image("D://ML//flight-price-prediction//images//corelation.png")
        
        with st.expander("Show prices with features")  : 
            st.subheader("Target Count Relation")
            st.image("D://ML//flight-price-prediction//images//airline_price.png")
            st.image("D://ML//flight-price-prediction//images//source.png")
            st.image("D://ML//flight-price-prediction//images//total_stop.png")
            st.image("D://ML//flight-price-prediction//images//destination.png")

            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("D://ML//flight-price-prediction//images//outliers.png")
            
            