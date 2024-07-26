import requests
print("__Welcome to the Weather Forecaster!__")
print("Just Enter the City you want the weather report for and click Enter:)\n")
city_name = input("Enter the name of the City : ")

def Gen_report(City):
    url = 'https://wttr.in/{}'.format(City)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
Gen_report(city_name)