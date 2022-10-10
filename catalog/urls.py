from django.urls import path

from catalog.views.user_views import SignInAPIView, user_info, LogoutView

urlpatterns = []

login_urls = [
    path('login/', SignInAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('user_info/', user_info)
]

urlpatterns += login_urls
