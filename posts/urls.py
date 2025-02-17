# from django.urls import path
# from .views import PostList, PostDetail
# from .views import UserList, UserDetail, PostList, PostDetail  # new


# urlpatterns = [
#     path('users/', UserList.as_view()),  # new
#     path('users/<int:pk>/', UserDetail.as_view()),  # new
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]


from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()  # أو يمكن استخدام DefaultRouter
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls  # استخدام المسارات التي أنشأها الراوتر تلقائيًا
