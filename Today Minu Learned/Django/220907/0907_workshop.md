1. accounts/
    ```django
    {% extends 'base.html' %}

    {% block content %}

    <h1>USER LIST</h1>
    <hr>
    {% for user in users %}

    <h1>{{ user.username }}</h1>
    <p>{{ user.email }}</p>
    <hr>

    {% endfor %}

    {% endblock content %}
    ```

    ```python
    from .models import User

    def user(request):
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'accounts/user.html', context)
    ```

2. accounts/login
    ```python
    from django.shortcuts import render, redirect
    from .forms import CustomUserChangeForm

    def signup(request):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()   # 회원가입 후 곧바로 로그인 진행
                auth_login(request, user)
                return redirect('articles:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    ```