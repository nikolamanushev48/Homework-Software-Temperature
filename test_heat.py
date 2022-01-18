import requests

from main import heatmin, heatmedium, heatmax

data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
temperatures = []


for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)


temperatures.sort()


def test_heatmin():
    assert heatmin() == temperatures[0]


def test_heatmedium():
    assert heatmedium() == temperatures[2]


def test_heatmax():
    assert heatmax() == temperatures[4]
