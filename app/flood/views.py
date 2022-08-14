import datetime

from django.shortcuts import render
import requests
import json


def main_page(request):
    url = "https://environment.data.gov.uk/flood-monitoring/id/stations?_limit=250"

    payload = {}
    headers = {}
    response = None
    len_stations = 0
    try:
        response = requests.request("GET", url, headers=headers, data=payload).json()
        len_stations = len(response['items'])
        print(response)
    except Exception as error:
        print("something happened\n", error)

    return render(request, "mainpage.html", context={"stations": json.dumps(response), 'len_stations': len_stations})


def station_page(request):
    if request.GET:
        station_id = request.GET.get('id', "")
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        url = f"https://environment.data.gov.uk/flood-monitoring/id/stations/{station_id}/readings?since={yesterday}&_sorted&parameter=level"

        payload = {}
        headers = {}
        response = None
        try:
            response = requests.request("GET", url, headers=headers, data=payload).json()
            x_data = []
            y_data = []
            for measure in response['items']:
                x_data.append(measure['dateTime'])
                y_data.append(measure['value'])

        except Exception as error:
            print("something happened\n", error)

    return render(request, "stationpage.html", {'measurements': response, 'x': x_data, 'y': y_data})
