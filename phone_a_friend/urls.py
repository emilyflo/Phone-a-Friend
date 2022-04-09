from django.contrib import admin
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/questions', api_views.QuestionListView.as_view(), name='api_questions_list'),
    path('api/question/<int:pk>', api_views.QuestionDetailsView.as_view(), name='api_question_details'),
    path('api/responses', api_views.ResponseListView.as_view(), name='api_responses_list'),
    path('api/users', api_views.UserListView.as_view(), name='user_list'),
    # path('api/user/<int:id>/questions', api_views..as_view(), name='user_questions'),
]