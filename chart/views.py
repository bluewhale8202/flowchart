from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Chart

def chart_list(request):
    charts = Chart.objects.all()
    return render(request, "chart/chart_list.html", {"charts": charts})


def question(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)
    return render(request, 'chart/question.html', {'chart': chart})


@csrf_exempt
def create_chart(request):
    if request.method == 'POST':
        request.POST['data']
        chart = Chart()
        chart.name = request.POST['name']
        chart.data = request.POST['data']
        chart.save()
        return redirect('chart_list')
    return render(request, 'chart/draw.html')


@csrf_exempt
def edit_chart(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)
    if request.method == 'POST':
        chart.name = request.POST['name']
        chart.data = request.POST['data']
        chart.save()
        return redirect('chart_list')
    return render(request, 'chart/draw.html', {"chart": chart})


from django.http import JsonResponse
import json
@csrf_exempt
def get_chart(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)
    return JsonResponse(json.loads(chart.data))


def delete_chart(request, chart_id):
    return render()
