from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Article
# . = 현재 .. = 상위폴더  / 현재 동일한 폴더에 있는 models .. views 랑 community 안에 있음
from .forms import Form

# from community.forms import Form
# from community.models import Article
# Create your views here.
def articlelist(request):
    # Article 클래스와 연결된 테이블의 모든 레코드를 조회
    article_list = Article.objects.all().order_by('-cdate')
    # for a in article_list:
    #     print('이름:', a.name, '제목:', a.title)
    print(article_list)
    return render(request, 'list.html', {'article_list':article_list})

def write(request):
# 비즈니스 로직 구현
    hello = '안녕 장고'
    # 사용자 요청 method post일때
    if request.method == 'POST':
        # request.POST 데이터를 폼객체로 생성
        form = Form(request.POST)
        # print(form)
        # form 데이터 유효성 검증
        if form.is_valid():
            # DB 테이블에 저장
            form.save()
        return redirect(reverse('community:list'))
    else:
        form = Form() # Form() 객체 생성
    return render(request, 'write.html',
                  {'hello_django':hello, 'form':form}) 
                  # request, template,


# return render(request, 'write.html', {'키':파이썬변수})

def viewdetail(request, num=1):
    article_detail = Article.objects.get(id=num) # 하나 갖고 올때는 get
    # 모든 것을 갖고 오면 all.. id가 num 인거 하나 갖고 올게~
    print(article_detail)
    return render(request, 'view_detail.html',{'article_detail':article_detail})

