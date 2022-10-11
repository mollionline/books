from django.urls import path

from catalog.views.book_views import CreateBookAPIView
from catalog.views.user_views import SignInAPIView, user_info, LogoutView

urlpatterns = []

login_urls = [
    path('login/', SignInAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('user_info/', user_info)
]

book_urls = [
    path('book/create', CreateBookAPIView.as_view(), name='books')
]

urlpatterns += login_urls
urlpatterns += book_urls
