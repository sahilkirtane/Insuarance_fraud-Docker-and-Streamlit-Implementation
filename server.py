import streamlit as st
import pickle
from datetime import datetime

print('Successfully executed ')

model = pickle.load(open('model.pkl', 'rb'))

def predict(vehicle_make, manu_year, severity_incident, incident_state, incident_city, incident_time, number_of_vehicles,
                       bodily_injuries, witness, amount_total_claim, amount_injury_claim, amount_property_claim, amount_vehicle_claim,
                       incident_month, incident_type_parked, incident_type_single_vehicle, incident_type_theft, collision_type_rear,
                       collision_type_side, authorities_contacted_fire, authorities_contacted_none, authorities_contacted_others,
                       authorities_contacted_police, insured_age, insured_gender, insured_education, capital_gains, capital_loss,
                       insured_occupation_armed_forces, insured_occupation_craft, insured_occupation_managerial, 
                       insured_occupation_framing_fishing, insured_occupation_cleaners, insured_occupation_inspect, 
                       insured_occupation_others, insured_occupation_house_service, insured_occupation_prof_speciality,
                       insured_occupation_protective_service, insured_occupation_sales, insured_occupation_tech_support,
                       insured_occupation_transport, insured_hobbies_basketball, insured_hobbies_board_games, insured_hobbies_bungee_jump,
                       insured_hobbies_camping, insured_hobbies_chess, insured_hobbies_crossfit, insured_hobbies_dancing, insured_hobbies_exercise,
                       insured_hobbies_golf, insured_hobbies_hiking, insured_hobbies_kayaking, insured_hobbies_movies, 
                       insured_hobbies_paintball, insured_hobbies_polo,insured_hobbies_reading, insured_hobbies_skydiving, 
                       insured_hobbies_sleeping, insured_hobbies_video_games, insured_hobbies_yachting, customer_loyalty, 
                       policy_state, single_limit, policy_deductible, policy_annual_premium, umbrella_premium,insured_relationship_not_family,
                       insured_relationship_others, insured_relationship_own_child, insured_relationship_unmarried, insured_relationship_wife):
    #step 5: make the predictions based on passed data
    prediction=model.predict([[vehicle_make, manu_year, severity_incident, incident_state, incident_city, incident_time, number_of_vehicles,
                       bodily_injuries, witness, amount_total_claim, amount_injury_claim, amount_property_claim, amount_vehicle_claim,
                       incident_month, incident_type_parked, incident_type_single_vehicle, incident_type_theft, collision_type_rear,
                       collision_type_side, authorities_contacted_fire, authorities_contacted_none, authorities_contacted_others,
                       authorities_contacted_police, insured_age, insured_gender, insured_education, capital_gains, capital_loss,
                       insured_occupation_armed_forces, insured_occupation_craft, insured_occupation_managerial, 
                       insured_occupation_framing_fishing, insured_occupation_cleaners, insured_occupation_inspect, 
                       insured_occupation_others, insured_occupation_house_service, insured_occupation_prof_speciality,
                       insured_occupation_protective_service, insured_occupation_sales, insured_occupation_tech_support,
                       insured_occupation_transport, insured_hobbies_basketball, insured_hobbies_board_games, insured_hobbies_bungee_jump,
                       insured_hobbies_camping, insured_hobbies_chess, insured_hobbies_crossfit, insured_hobbies_dancing, insured_hobbies_exercise,
                       insured_hobbies_golf, insured_hobbies_hiking, insured_hobbies_kayaking, insured_hobbies_movies, 
                       insured_hobbies_paintball, insured_hobbies_polo,insured_hobbies_reading, insured_hobbies_skydiving, 
                       insured_hobbies_sleeping, insured_hobbies_video_games, insured_hobbies_yachting, customer_loyalty, 
                       policy_state, single_limit, policy_deductible, policy_annual_premium, umbrella_premium,insured_relationship_not_family,
                       insured_relationship_others, insured_relationship_own_child, insured_relationship_unmarried, insured_relationship_wife]])
    if prediction == 0:
        return 'There will be no fraud'
    else:
        return 'There will be fraud... '
    
def main():
    st.title("Insurance Fraud Prdiction")
    html_temp = """
    <div style="background-color:Black;padding:20px">
    <h2 style="color:white;text-align:center;">Streamlit Insurance Fraud Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.sidebar.title("Customer's Data")
    # Categorical and binary variables
    var_make = ("Audi", "Volkswagen","Toyota", "Mercedes", "Suburu", "Saab", "Nissan", "Ford", "Accura", "Dodge", "Honda", "Chevrolet",
                "Jeep","BMW")
    # var_man_year = ("1993", "1994","1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2003","2004","2005","2006",
    #                 "2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023")
    var_severity = ("Trivial", "Minor","Major", "Total Loss")
    var_incident_state = ("State1", "State2","State3", "State4","State5", "State6","State7","State8","State9")
    var_incident_city = ("City1", "City2","City3", "City4","City5", "City6","City7")
    var_incident_type = ("Parked Car", "Single Vehicle Collision","Vehicle Theft", "Multi Vehicle Collision")
    var_collision_type = ("Rear", "Side","Front")
    var_authorities_contacted = ("Fire", "None","Others","Police","Ambulance")
    var_insured_gender = ("Male", "Female")
    var_insured_education = ("High School", "College", "Associate","Masters","MD","PhD","JD")
    var_insured_relationship = ("Not family", "Others", "Own child","Unmarried","Wife","Husband")
    var_insured_occupation = ("Armed Forces", "Craft Repair", "Managerial","Farming-Fishing","Cleaners","OP Inspect","Others","Priv House Service",
                              "Prof. Speciality", "Protective Service", "Sales","Tech Support", "Transport", "Clerical")
    var_insured_hobbies = ("Basketball", "Board Games", "Bungee Jump","Camping","Chess","Crossfit","Dancing","Exercise","Golf","Hiking",
                           "Kayaking","Hiking","Movies","Paintball","Polo","Reading","Skydiving","Sleeping","Video Games","Yachting","Base Jump")

    # var_bool = ("Yes", "No")
    # var_multiple = ("Yes", "Not", "No phone service")
    # var_internet = ("DSL", "Fiber optic", "No")
    # var_contract = ("Month-to-month", "One year", "Two year")
    # var_payment_m = ("Credit card (automatic)", "Bank transfer (automatic)", "Electronic check", "Mailed check")

    #step 1: we read all the data here
    vehicle_make = st.sidebar.selectbox("Customer's Vehicle Make", var_make)
    #man_year = st.sidebar.selectbox("Year of car manufacture", var_man_year)
    severity_incident = st.sidebar.selectbox("Severity Of Incident", var_severity)
    incident_state = st.sidebar.selectbox("State where incident Occured", var_incident_state)
    incident_city = st.sidebar.selectbox("City where the incident occured", var_incident_city)
    incident_type = st.sidebar.selectbox("Select the type of incident", var_incident_type)
    collision_type = st.sidebar.selectbox("Select the type of collision", var_collision_type)
    authorities_contacted = st.sidebar.selectbox("Select the authorities contacted", var_authorities_contacted)
    insured_gender = st.sidebar.selectbox("Select the gender of insured", var_insured_gender)
    insured_education = st.sidebar.selectbox("Select the education of insured", var_insured_education)
    insured_occupation = st.sidebar.selectbox("Select the occupation of insured", var_insured_occupation)
    insured_hobbies = st.sidebar.selectbox("Select the hobbies of insured", var_insured_hobbies)
    policy_state = st.sidebar.selectbox("Give the State where policy was taken", var_incident_state)
    insured_relationship = st.sidebar.selectbox("Select the insured relationship", var_insured_relationship)

    # Numerical variables
    manu_year = st.sidebar.number_input("Select the year of manufacture", min_value = 1993, max_value = 2023)
    incident_time = st.sidebar.number_input("Select the incident time", min_value = 0, max_value = 23)
    number_of_vehicles = st.sidebar.number_input("Select the number of vehicles", min_value = 1, max_value = 4)
    bodily_injuries = st.sidebar.number_input("Select the bodily injuries", min_value = 0, max_value = 2)
    witness = st.sidebar.number_input("Select the number of witness", min_value = 0, max_value = 3)
    amount_total_claim = st.sidebar.number_input("Select the total amount of claim")
    amount_injury_claim = st.sidebar.number_input("Select the amount of injury claim")
    amount_property_claim = st.sidebar.number_input("Select the amount of property claim")
    amount_vehicle_claim = st.sidebar.number_input("Select the amount of vehicle claim")
    incident_month = st.sidebar.number_input("Select the incident month number", min_value = 1, max_value = 12)
    insured_age = st.sidebar.number_input("Select the insured age")
    capital_gains = st.sidebar.number_input("Select the capital gains")
    capital_loss = st.sidebar.number_input("Select the capital loss")
    customer_loyalty = st.sidebar.number_input("Select the customer loyalty score")
    single_limit = st.sidebar.number_input("Enter the single limit")
    policy_deductible = st.sidebar.number_input("Enter the policy deductible")
    policy_annual_premium = st.sidebar.number_input("Enter the annual premium")
    umbrella_premium = st.sidebar.number_input("Enter the umbrella premium")
    policy_year = st.sidebar.number_input("Enter the year of policy coverage", min_value = 1993, max_value = 2023)
    
    #step3: functions to change the category as per requirements of the model
    # Binary variables
    def create_binary(content):
        if content == "Male":
            content = 1.0
        elif content == "Female":
            content = 0.0
        return content

    #convert car makes into label encoders
    def convert_vehicle_make(content):
        if content == "Audi":
            content = 1
        elif content == "Volkswagen":
            content = 2
        elif content == "Toyota":
            content = 3
        elif content == "Mercedes":
            content = 4
        elif content == "Suburu":
            content = 5
        elif content == "Saab":
            content = 6
        elif content == "Nissan":
            content = 7
        elif content == "Ford":
            content = 8
        elif content == "Accura":
            content = 9
        elif content == "Dodge":
            content = 10
        elif content == "Honda":
            content = 11
        elif content == "Chevrolet":
            content = 12
        elif content == "Jeep":
            content = 13
        elif content == "BMW":
            content = 14
        return content
    
    def convert_severity_incident(content):
        if content == "Trivial":
            content = 1
        elif content == "Minor":
            content = 2
        elif content == "Major":
            content = 3
        elif content == "Total Loss":
            content = 4
        return content
    
    def convert_incident_state(content):
        if content == "State1":
            content = 1
        elif content == "State2":
            content = 2
        elif content == "State3":
            content = 3
        elif content == "State4":
            content = 4
        elif content == "State5":
            content = 5
        elif content == "State6":
            content = 6
        elif content == "State7":
            content = 7
        elif content == "State8":
            content = 8
        elif content == "State9":
            content = 9
        return content
    
    def convert_incident_city(content):
        if content == "City1":
            content = 1
        elif content == "City2":
            content = 2
        elif content == "City3":
            content = 3
        elif content == "City4":
            content = 4
        elif content == "City5":
            content = 5
        elif content == "State6":
            content = 6
        elif content == "City6":
            content = 7
        elif content == "City7":
            content = 8
        return content
    
    def convert_incident_type(content):
        if content == "Parked Car":
            incident_type_parked = 1
            incident_type_single_vehicle = 0
            incident_type_theft = 0
        elif content == "Single Vehicle Collision":
            incident_type_parked = 0
            incident_type_single_vehicle = 1
            incident_type_theft = 0
        elif content == "Vehicle Theft":
            incident_type_parked = 0
            incident_type_single_vehicle = 0
            incident_type_theft = 1
        elif content == "Multi Vehicle Collision":
            incident_type_parked = 0
            incident_type_single_vehicle = 0
            incident_type_theft = 0
        return incident_type_parked, incident_type_single_vehicle, incident_type_theft
    
    def convert_collision_type(content):
        if content == "Rear":
            collision_type_rear = 1
            collision_type_side = 0
        elif content == "Side":
            collision_type_rear = 0
            collision_type_side = 1
        elif content == "Front":
            collision_type_rear = 0
            collision_type_side = 0
        return collision_type_rear, collision_type_side
    
    def convert_authorities_contacted(content):
        if content == "Fire":
            authorities_contacted_fire = 1
            authorities_contacted_none = 0
            authorities_contacted_others = 0
            authorities_contacted_police = 0
        elif content == "None":
            authorities_contacted_fire = 0
            authorities_contacted_none = 1
            authorities_contacted_others = 0
            authorities_contacted_police = 0
        elif content == "Others":
            authorities_contacted_fire = 0
            authorities_contacted_none = 0
            authorities_contacted_others = 1
            authorities_contacted_police = 0
        elif content == "Police":
            authorities_contacted_fire = 0
            authorities_contacted_none = 0
            authorities_contacted_others = 0
            authorities_contacted_police = 1
        elif content == "Ambulance":
            authorities_contacted_fire = 0
            authorities_contacted_none = 0
            authorities_contacted_others = 0
            authorities_contacted_police = 0
        return authorities_contacted_fire, authorities_contacted_none, authorities_contacted_others, authorities_contacted_police
    
    def convert_insured_education(content):
        if content == "High School":
            content = 1
        elif content == "College":
            content = 2
        elif content == "Associate":
            content = 3
        elif content == "Masters":
            content = 4
        elif content == "MD":
            content = 5
        elif content == "PhD":
            content = 6
        elif content == "JD":
            content = 7
        return content
    
    def convert_insured_occupation(content):
        if content == "Armed Forces":
            insured_occupation_armed_forces = 1
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Craft Repair":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 1
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Managerial":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 1
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Farming-Fishing":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 1
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Cleaners":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 1
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "OP Inspect":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 1
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Others":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 1
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Priv House Service":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 1
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Prof. Speciality":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 1
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Protective Service":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 1
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Sales":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 1
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        elif content == "Tech Support":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 1
            insured_occupation_transport = 0
        elif content == "Transport":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 1
        elif content == "Clerical":
            insured_occupation_armed_forces = 0
            insured_occupation_craft = 0
            insured_occupation_managerial = 0
            insured_occupation_framing_fishing = 0
            insured_occupation_cleaners = 0
            insured_occupation_inspect = 0
            insured_occupation_others = 0
            insured_occupation_house_service = 0
            insured_occupation_prof_speciality = 0
            insured_occupation_protective_service = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport = 0
        return insured_occupation_armed_forces, insured_occupation_craft, insured_occupation_managerial, insured_occupation_framing_fishing,\
            insured_occupation_cleaners, insured_occupation_inspect, insured_occupation_others, insured_occupation_house_service, \
                insured_occupation_prof_speciality, insured_occupation_protective_service, insured_occupation_sales, \
                    insured_occupation_tech_support, insured_occupation_transport
    
    def convert_insured_hobbies(content):
        if content == "Basketball":
            insured_hobbies_basketball = 1
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Board Games":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 1
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Bungee Jump":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 1
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Camping":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 1
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Chess":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 1
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Crossfit":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 1
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Dancing":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 1
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Exercise":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 1
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Golf":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 1
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Hiking":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 1
            insured_hobbies_kayaking = 1
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Kayaking":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 1
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Movies":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 1
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Paintball":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 1
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Polo":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 1
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Reading":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 1
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Skydiving":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 1
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Sleeping":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 1
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        elif content == "Video Games":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 1
            insured_hobbies_yachting = 0
        elif content == "Base Jump":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 1
        elif content == "Base Jump":
            insured_hobbies_basketball = 0
            insured_hobbies_board_games = 0
            insured_hobbies_bungee_jump = 0
            insured_hobbies_camping = 0
            insured_hobbies_chess = 0
            insured_hobbies_crossfit = 0
            insured_hobbies_dancing = 0
            insured_hobbies_exercise = 0
            insured_hobbies_golf = 0
            insured_hobbies_hiking = 0
            insured_hobbies_kayaking = 0
            insured_hobbies_movies = 0
            insured_hobbies_paintball = 0
            insured_hobbies_polo = 0
            insured_hobbies_reading = 0
            insured_hobbies_skydiving = 0
            insured_hobbies_sleeping = 0
            insured_hobbies_video_games = 0
            insured_hobbies_yachting = 0
        return insured_hobbies_basketball, insured_hobbies_board_games, insured_hobbies_bungee_jump, insured_hobbies_camping, \
            insured_hobbies_chess, insured_hobbies_crossfit, insured_hobbies_dancing, insured_hobbies_exercise, insured_hobbies_golf, \
                insured_hobbies_hiking,insured_hobbies_kayaking, insured_hobbies_movies, insured_hobbies_paintball, insured_hobbies_polo, \
                    insured_hobbies_reading,insured_hobbies_skydiving, insured_hobbies_sleeping, insured_hobbies_video_games, \
                        insured_hobbies_yachting
    
    def convert_insured_relationship(content):
        if content == "Not family":
            insured_relationship_not_family = 1
            insured_relationship_others = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif content == "Others":
            insured_relationship_not_family = 0
            insured_relationship_others = 1
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif content == "Own child":
            insured_relationship_not_family = 0
            insured_relationship_others = 0
            insured_relationship_own_child = 1
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif content == "Unmarried":
            insured_relationship_not_family = 0
            insured_relationship_others = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 1
            insured_relationship_wife = 0
        elif content == "Wife":
            insured_relationship_not_family = 0
            insured_relationship_others = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 1
        elif content == "Husband":
            insured_relationship_not_family = 0
            insured_relationship_others = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        return insured_relationship_not_family, insured_relationship_others, insured_relationship_own_child, insured_relationship_unmarried,\
        insured_relationship_wife



    
    #step2: convert the data into the required format of the model. ie convert category to binary
    vehicle_make = convert_vehicle_make(vehicle_make)
    severity_incident = convert_severity_incident(severity_incident)
    incident_state = convert_incident_state(incident_state)
    policy_state = convert_incident_state(policy_state)
    incident_city = convert_incident_city(incident_city)
    incident_type_parked, incident_type_single_vehicle, incident_type_theft = convert_incident_type(incident_type)
    collision_type_rear, collision_type_side = convert_collision_type(collision_type)
    authorities_contacted_fire, authorities_contacted_none, authorities_contacted_others, authorities_contacted_police = convert_authorities_contacted(authorities_contacted)
    insured_gender = create_binary(insured_gender)
    insured_education = convert_insured_education(insured_education)
    insured_occupation_armed_forces, insured_occupation_craft, insured_occupation_managerial, insured_occupation_framing_fishing,\
        insured_occupation_cleaners, insured_occupation_inspect, insured_occupation_others, insured_occupation_house_service, \
            insured_occupation_prof_speciality, insured_occupation_protective_service, insured_occupation_sales, \
                insured_occupation_tech_support, insured_occupation_transport = convert_insured_occupation(insured_occupation)
    insured_hobbies_basketball, insured_hobbies_board_games, insured_hobbies_bungee_jump, insured_hobbies_camping, \
            insured_hobbies_chess, insured_hobbies_crossfit, insured_hobbies_dancing, insured_hobbies_exercise, insured_hobbies_golf, \
                insured_hobbies_hiking,insured_hobbies_kayaking, insured_hobbies_movies, insured_hobbies_paintball, insured_hobbies_polo, \
                    insured_hobbies_reading,insured_hobbies_skydiving, insured_hobbies_sleeping, insured_hobbies_video_games, \
                        insured_hobbies_yachting = convert_insured_hobbies(insured_hobbies)
    insured_relationship_not_family, insured_relationship_others, insured_relationship_own_child, insured_relationship_unmarried,\
        insured_relationship_wife = convert_insured_relationship(insured_relationship)
    
    manu_year = int(datetime.now().year - manu_year)
    incident_time = int(incident_time)
    number_of_vehicles = int(number_of_vehicles)
    bodily_injuries = int(bodily_injuries)
    witness = int(witness)
    amount_total_claim = amount_total_claim
    amount_injury_claim = int(amount_injury_claim)
    amount_property_claim = int(amount_property_claim)
    amount_vehicle_claim = int(amount_vehicle_claim)
    incident_month = int(incident_month)
    insured_age = int(insured_age)
    capital_gains = int(capital_gains)
    capital_loss = int(capital_loss)
    customer_loyalty = int(customer_loyalty)
    single_limit = single_limit
    policy_deductible = int(policy_deductible)
    policy_annual_premium = policy_annual_premium
    umbrella_premium = int(umbrella_premium)
    policy_year = int(datetime.now().year - policy_year)

    result=""
    #step4: pass the created the data to the model.
    if st.button("Predict"):
        result=predict(vehicle_make, manu_year, severity_incident, incident_state, incident_city, incident_time, number_of_vehicles,
                       bodily_injuries, witness, amount_total_claim, amount_injury_claim, amount_property_claim, amount_vehicle_claim,
                       incident_month, incident_type_parked, incident_type_single_vehicle, incident_type_theft, collision_type_rear,
                       collision_type_side, authorities_contacted_fire, authorities_contacted_none, authorities_contacted_others,
                       authorities_contacted_police, insured_age, insured_gender, insured_education, capital_gains, capital_loss,
                       insured_occupation_armed_forces, insured_occupation_craft, insured_occupation_managerial, 
                       insured_occupation_framing_fishing, insured_occupation_cleaners, insured_occupation_inspect, 
                       insured_occupation_others, insured_occupation_house_service, insured_occupation_prof_speciality,
                       insured_occupation_protective_service, insured_occupation_sales, insured_occupation_tech_support,
                       insured_occupation_transport, insured_hobbies_basketball, insured_hobbies_board_games, insured_hobbies_bungee_jump,
                       insured_hobbies_camping, insured_hobbies_chess, insured_hobbies_crossfit, insured_hobbies_dancing, insured_hobbies_exercise,
                       insured_hobbies_golf, insured_hobbies_hiking, insured_hobbies_kayaking, insured_hobbies_movies, 
                       insured_hobbies_paintball, insured_hobbies_polo,insured_hobbies_reading, insured_hobbies_skydiving, 
                       insured_hobbies_sleeping, insured_hobbies_video_games, insured_hobbies_yachting, customer_loyalty, 
                       policy_state, single_limit, policy_deductible, policy_annual_premium, umbrella_premium,insured_relationship_not_family,
                       insured_relationship_others, insured_relationship_own_child, insured_relationship_unmarried, insured_relationship_wife)
        st.success('You Have {}'.format(result))
    if st.button("About"):
        st.text("Bootcamp")
        st.text("Built with Streamlit")
        st.text('Created By MEEEEE')
main()
