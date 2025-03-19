from django.shortcuts import render
from .models import Article
# . = 현재 .. = 상위폴더  / 현재 동일한 폴더에 있는 models .. views 랑 community 안에 있음
from .forms import Form

# from community.forms import Form
# from community.models import Article
# Create your views here.
def articlelist(request):
    # Article 클래스와 연결된 테이블의 모든 레코드를 조회
    article_list = Article.objects.all()
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


def index(request):
    # article 테이블에서 최근글 3개를 조회
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
# order_by() 함수는 정렬(순서 변경) 할 때 사용 / -cdate > -는 내림차순 정렬
# 가장 최신글이 먼저 나오도록 정렬.. order_by('cdate') : 오래된 글이 먼저나오는 오름차순
# [:3] > 슬라이싱 .. 가장 최신 글 3개만 가져옴
    return render(request, 'index.html',{'latest_article_list':latest_article_list})