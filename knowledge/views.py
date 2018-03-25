from django.shortcuts import render,get_object_or_404
from .models import knowledges
import logging

# Create your views here.
def knowledges_title(request):
    logger = logging.getLogger('django.request')

    logger.info('adf')
    know = knowledges.objects.all() #获取数据库知识表所有对象
    #
    return render(request, "knowledge/titles.html", {"knows": know})

def knowledges_details(request,knowledge_id):
    #knows = knowledges.objects.get(id=knowledge_id) #获取某条知识内容
    knows = get_object_or_404(knowledges,id=knowledge_id)
    return render(request,"knowledge/content.html",{"knows":knows})  #返回前端
