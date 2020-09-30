#   Author - Christopher Wagner 
#   
#   This script will aquire information regarding the top 200 tracks and 
#   print the information into a file for the user.
#   The text files can then be used in other scripts to analyze the characterstics 
#   of a top 200 track on spotify.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://spotifycharts.com")  #Opens URL and displays screen

def get_track_info():
    """Funcition will retrieve information from spotify about a track and store the rank, title/artist, and stream count in a tuple"""
    #Gets Container of Info
    body = driver.find_element_by_class_name("chart-table")
    
    #loads sets of track name,position, and streams
    each_track = body.find_elements_by_class_name("chart-table-track")
    each_position = body.find_elements_by_class_name("chart-table-position")
    each_track_streams = body.find_elements_by_class_name("chart-table-streams")
    each_track.pop(0)
    each_track_streams.pop(0)

    #Create tuple by zipping together items from lists
    track_info = zip(each_position,each_track,each_track_streams)
    return track_info

def format_to_file(tuple_data):
    """Function will create and write to a file titled by the date, formatting information neatly"""
    today = date.today()
    day = today.strftime("%b-%d-%Y")
    file = open("Spotify200-Charts-"+day+".txt","w")
    file.write(" Rank               Title          \n\n")
    for position, track, streams in tuple_data:
        file.writelines("Rank: {}   Title: {}       Streams:  {} \n".format(position.text, track.text, streams.text))
        #Uncomment following line to print to console
        #print("Rank: {}   Title:  {}   Streams:  {}".format(position.text, track.text, streams.text))


info = get_track_info()
format_to_file(info)    
driver.quit()