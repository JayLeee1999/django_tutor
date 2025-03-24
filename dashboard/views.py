
# DB 테이블에서 데이터 조회
# 비즈니스 로직
# 랜더링 데이터 만들기

from urllib import request
from django.shortcuts import render, redirect

from dashboard.forms import CountryDataForm

from .models import CountryData

def dashboard(request):
    data = CountryData.objects.all()

    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            # 나라 이름이 있으면 update, 없으면 저장
            country_name = form.cleaned_data['country']
            obj, creaetd = CountryData.objects.update_or_create(
                country=country_name, defaults=form.cleaned_data
            )
            print('obj, created : ", obj, created')
            return redirect('/dashboard')
            # form.save()
            # return redirect('/dashboard')
    else:
        form = CountryDataForm()

    context = {
        'dataset':data, 'form':form}

    return render(request, 'dashboard.html', context)

# DB 테이블에서 데이터 조회
# 비즈니스 로직
# 랜더링 데이터 만들기
