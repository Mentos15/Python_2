from django.shortcuts import render
import requests

token = 'fc7c0f98fc7c0f98fc7c0f9811fc0caf23ffc7cfc7c0f98a2fce1c5315fd84654f552e8'
version = '5.103'

def TakeUserInfo(request):

    response = requests.get('https://api.vk.com/method/wall.get',
                            params = {
                                'access_token':token,
                                'v':version,
                                'domain':'rapnewrap'
                            })
    data = response.json()

    return render(request,'users.html',{'data':data})
