from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html1 =""" <!doctype html>
           <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Главная страница!</title>
                </head>
                <body>
	                <h1>
		                Это главная страница сайта.
		                Скоро тут будет какая то важная и нужная информация!
	                </h1>		
                </body>
           </html>"""

html2 =""" <!doctype html>
           <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>О нас</title>
                </head>
                <body>
	                <h1>
		                Это страница с контактной информацией компании
		                
	                </h1>		
                </body>
           </html>"""


# Create your views here.
def index(request):
    logger.info('Index page loaded successfully')
    return HttpResponse(html1)

def about(request):
    logger.info('About page loaded successfully')
    return HttpResponse(html2)
