1. N:1 True or False

   1) **T** - 부모 테이블 데이터의 PK를 참조하는 값

   2) **F** - FK로 직접 참조하지 않고 _set을 이용하여 역참조한다.

   3) **T** - 참조하는 PK값을 가진 데이터가 삭제된 경우 어떻게 작동할지를 정의해야 하는 필수 인자이다.

   4) **F** - PK 외 특정할 수 있는 값을 설정해도 무관하다.

2. ForeignKey column name

    `question_id`, `articles_comment`

3. N:1 model manager

    `question`

4. next parameter

   1) redirect되는 next이후의 url이 GET방식으로 요청되어 POST방식으로만 접근이 가능한 delete 실행이 거절되며, 405오류가 발생한다.

   2)   ```python
        @login_required
        @require_POST
        def delete(request, pk):
            article = Article.objects.get(pk=pk)
            if request.user.is_authenticated:
                if request.user == article.user:
                    article.delete()
                    return redirect('articles:index')
            return redirect('articles:detail', article.pk)
        ```
