import requests,json

def joke():
    print('\n','*'*90,'\n')

    print('\t\tANGER GENERATOR APP(jokes)')
    print()
    res = requests.get("https://icanhazdadjoke.com/", headers= {"Accept":"application/json"})
    connection = res.ok
    result = res.json()
    print(result['joke'])
    print('\n','*'*90,'\n')

def news():

    print('\n','*'*90,'\n')

    print('\t\tNEWS GENERATOR APP')
    print()
    print()
    def NewsFromBBC():
    
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "a2fffbd9a540482e8249b0472d17c14a"
        }
        main_url = " https://newsapi.org/v1/articles"
    
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        article = open_bbc_page["articles"]

        results = []
        
        for ar in article:
            results.append(ar["title"])
        for i in range(len(results)):
            
            
            print('\t',i + 1, results[i])
        print('\n','*'*90,'\n')
    


    NewsFromBBC()

def weather():
    print('\n','*'*90,'\n')

    print('\t\tWeather APP')
    print()
    try:
        api_key = "b606d883e1a9835b274360e3bc8713a1"
        
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        city_name = input("Enter city name : ")
        print()
        
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
        response = requests.get(complete_url)
        
        x = response.json()
    
        if x["cod"] != "404":
        
            
            main = x["main"]
        
        
            current_temperature = main["temp"]
            current_pressure = main["pressure"]
            current_humidity = main["humidity"]
            
            weather = x["weather"]
        
            weather_description = weather[0]["description"]
        
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidity) +
                "\n weather = " +
                            str(weather_description))
        
        else:
            print(" City Not Found ")
    except:
        print('no of requests exhuasted')

    print('\n','*'*90,'\n')


print('''
 _____  ____   ___  ___    _   _  ____   _____ 
|_   _||  _ \ |_ _|/ _ \  | | | |/ ___| | ____|
  | |  | |_) | | || | | | | | | |\___ \ |  _|  
  | |  |  _ <  | || |_| | | |_| | ___) || |___ 
  |_|  |_| \_\|___|\___/   \___/ |____/ |_____|
                    
                    -By  The ERRORs
''')

print()
print('''
    Descrition:
        This is a simple tool created by The ERRORs.feel it!!!

    commands                    description
    ------------------------------------------------------------------

    feednews        -   Feeds You The Treanding news in BBC.

    feedjokes       -   Feeds You The Crazy Jokes You Ever Heard Before.

    feedweather     -   Feeds You The Weather Report Of Current Time.

    help            -   Provides You Brief Discription Of This Cool Tool

    exit            -   quits the tool.

''')
while 1:
    command = input(">")
    commands = ["feednews","feedjokes","feedweather","help","exit"]
    if command in commands:
        if command=="feednews":
            news()
        elif command=="feedjokes":
            joke()
        elif command=="feedweather":
            weather()
        elif command=="exit":
            break
        elif command=="help":
            print('''
    commands                    description
    ------------------------------------------------------------------

    feednews        -   Feeds You The Treanding news in BBC.

    feedanger       -   Feeds You The Crazy Jokes You Ever Heard Before.

    feedweather     -   Feeds You The Weather Report Of Current Time.

    help            -   Provides You Brief Discription Of This Cool Tool
            ''')
    else:
        print("command not found \n")
print("\nThank You For Using Our tool \n")