from django.shortcuts import render
# Create your vfrom django.shortcuts import render
from django.http import HttpResponse
import requests

url = "https://chatgpt53.p.rapidapi.com/"
url1 = "https://youtube-transcriptor.p.rapidapi.com/transcript"


def test(request):
    x = " "
    count=0
    video = request.GET.get("videoId")
    print(video)
    if video==None:
      count=1
    
    try:
      lst=video.split('https://www.youtube.com/watch?v=')
      print(lst[1])
      video1=lst[1]
      querystring = {"video_id": video1, "lang": "en"}
  
      headers1 = {
          "X-RapidAPI-Key": "695383fc8amshe2de6b6b8b42f69p12c710jsn0e38bfd74c27",
          "X-RapidAPI-Host": "youtube-transcriptor.p.rapidapi.com"
      }
      response1 = requests.get(url1, headers=headers1, params=querystring)
      print(response1.json())
      try:
          q1='&#39;'
          q2='&quot;'
          for i in response1.json()[0]['transcription']:
              try:
                  if q1 in i['subtitle']:
                    i['subtitle'].remove(q1)
                  if q2 in i['subtitle']:
                    i['subtitle'].remove(q2)
                  x = x + " " + i['subtitle']
                  #print(i['subtitle'], end=' ')
              except:
                  pass
  
      except:
          x = "This video has no subtitles"
            
  
      print("this is x",x)
    except:
      pass
    if count==1:
      summary=" "
    else:
      payload = {
          "messages": [{
              "role": "user",
              "content": "Hello"
          }, {
              "role": "assistant",
              "content": "Hi there! How may I assist you today?"
          }, {
              "role": "user",
              "content": ("Give a long summary this text: \n" + x),
          }]
      }
      headers = {
          "content-type": "application/json",
          "X-RapidAPI-Key": "695383fc8amshe2de6b6b8b42f69p12c710jsn0e38bfd74c27",
          "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
      }
      response = requests.post(url, json=payload, headers=headers)

      print(response.json())
      #print(type(response.json()))
      #print(len(response.json()))
    
      summary=response.json()['choices'][0]['message']['content']

    return render(
        request, 'index.html', {
            'transcript': x,
            'summary': summary
        })


def test1(request):
    x = " "
    video = request.GET.get("url")
    print(video)
    #video = 'LNHBMFCzznE'
    
    
    try:
      lst=video.split('https://www.youtube.com/watch?v=')
      print(lst[1])
      video1=lst[1]
      querystring = {"video_id": video1, "lang": "en"}
  
      headers1 = {
          "X-RapidAPI-Key": "695383fc8amshe2de6b6b8b42f69p12c710jsn0e38bfd74c27",
          "X-RapidAPI-Host": "youtube-transcriptor.p.rapidapi.com"
      }
      response1 = requests.get(url1, headers=headers1, params=querystring)
  
      try:
          for i in response1.json()[0]['transcription']:
              try:
                  x = x + " " + i['subtitle']
                  #print(i['subtitle'], end=' ')
              except:
                  pass
  
      except:
          x = "This video has no subtitles"
  
      print("this is x",x)
    except:
      pass
    payload = {
        "messages": [{
            "role": "user",
            "content": "Hello"
        }, {
            "role": "assistant",
            "content": "Hi there! How may I assist you today?"
        }, {
            "role": "user",
            "content": ("Give a long summary this text: \n" + x),
        }]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "695383fc8amshe2de6b6b8b42f69p12c710jsn0e38bfd74c27",
        "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    #print(type(response.json()))
    #print(len(response.json()))

    summary=response.json()['choices'][0]['message']['content']

    return render(
        request, 'testing.html', {
            'transcript': x,
            'summary': summary
        })
