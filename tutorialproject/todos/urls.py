from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('hello_python', views.hello_python_view, name='hello_python'),
    path('hello_html', views.hello_html_view, name="hello_html"),
    path('special', views.special_view, name="special"),
    path('add/<int:num1>+<int:num2>', views.hello_path, name="hello path"),
    path('postendpoint', views.post_example, name="post_example"),
    path('submit_example', views.submit_example, name="submit_example"),
    path('submit_django', views.submit_django_form, name="submit_django"),
    path('template_demo', views.template_view, name="template_demo"),
    path('todos', views.todos_view, name="todos"),
    path('hello_query', views.hello_query, name="hello query")
]