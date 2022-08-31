# coding: utf-8
Article.objects.all()
article = Article()
article
article.title = 'first'
article.content = 'django!'
article.save()
article
article = Article(title = 'second', content = 'django!')
