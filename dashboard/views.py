from django.shortcuts import render

from .models import CountryData

def dashboard(request):

    datas = CountryData.objects.all()
    context = {
        'dataset' : datas
    }
    return render(request, 'dashboard.html', context)
# DB 테이블에서 데이터 조회
# 비즈니스 로직
# 랜더링 데이터 만들기
