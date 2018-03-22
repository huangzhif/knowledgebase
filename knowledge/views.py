from django.shortcuts import render
from .models import knowledges
import logging



# Create your views here.
def knowledges_title(request):
    logger = logging.getLogger('django.request')
    logger.info("this is an error msg")

    know = knowledges.objects.all() #获取数据库知识表所有对象
    return render(request, "knowledge/titles.html", {"knows": know})
