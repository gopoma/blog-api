from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('', views.PostViewSet, basename="posts")

urlpatterns = router.urls