import requests

temperatures = []


def heatmin():
    return temperatures[0]


def heatmedium():
    return temperatures[2]


def heatmax():
    return temperatures[4]


data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')

for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)


temperatures.sort()
