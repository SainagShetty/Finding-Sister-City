from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import os
#import sys  
#sys.path.append(os.path.abspath(os.path.dirname('__file__')+'/'))
from SisterCityApp.newsanalytics import news_rank



# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def searchCity(request):
    cityVal=request.POST['cityinput']
    climateWt=request.POST['climate-value2']
    cultureWt=request.POST['culture-value2']
    demogWt=request.POST['demographics-value2']
    economyWt=request.POST['economy-value2']
    politicsWt=request.POST['politics-value2']
    proximityWt=request.POST['proximity-value2']
    print(cityVal)
    print(climateWt)
    print(cultureWt)
    print(demogWt)
    print(economyWt)
    print(politicsWt)
    print(proximityWt)
    return render(request, 'results.html')

def searchSpecific(request):
    cityone=request.POST['cityone']
    citytwo=request.POST['citytwo']
    citythree=request.POST['citythree']
    cityfour=request.POST['cityfour']
    cityfive=request.POST['cityfive']
    searchQuery=request.POST['searchQuery']
    cityList=[cityone,citytwo,citythree,cityfour,cityfive]
    newsrankObj=news_rank.newsrank()
    bestCity=newsrankObj.getTopCity(searchQuery,cityList)
    print(searchQuery)
    top1city=bestCity
    return render(request, 'refinedSearchResults.html',{'topcity':top1city})    
	   
		
		
		
			 