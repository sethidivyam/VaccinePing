# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:22:13 2021

@author: divya
"""
import requests
import time
import pyautogui as pg
import webbrowser as web
import pyttsx3

engine = pyttsx3.init()

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

date_int = '3-1-2022'
age = 17
pincode_list = [110009 , 110006 , 110084 , 110085 , 110088 ]

phone_list = [ '+919911713714' ]

def findAvailability(pin):
    URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date_int}'
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json.get("centers", [])
    for each in data:
        sessions = each.get("sessions", [])
        if sessions:
            x = sessions[0]
            if ((x["available_capacity_dose1"] > 0) and (x["min_age_limit"] <= age) and (x["vaccine"] == 'COVAXIN')):          
                counter += 1
                print(x["available_capacity_dose1"])
                print(each['district_name'])
                print(each['pincode'], '\n')
                
                for phone_no in phone_list: 
                    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text=vaccine is available at {each['district_name']} with pincode {each['pincode']}")       
                    engine.say(f"vaccine is available at {each['district_name']} with pincode {each['pincode']}")
                    engine.runAndWait()     
                    time.sleep(10)
                    pg.press("enter")
                    time.sleep(2)
                return True
        
    if counter == 0:
        print("No Available Slots")
        print(pin, '\n')
        return False

while True:
    time.sleep(5)
    for pincode in pincode_list:
        findAvailability(pincode)