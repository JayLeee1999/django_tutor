from django.shortcuts import render
from community.models import Article

def index(request):
    # article 테이블에서 최근글 3개를 조회
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
# order_by() 함수는 정렬(순서 변경) 할 때 사용 / -cdate > -는 내림차순 정렬
# 가장 최신글이 먼저 나오도록 정렬.. order_by('cdate') : 오래된 글이 먼저나오는 오름차순
# [:3] > 슬라이싱 .. 가장 최신 글 3개만 가져옴
    return render(request, 'index.html',{'latest_article_list':latest_article_list})
