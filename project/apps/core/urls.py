from django.conf.urls import url, include
from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
urlpatterns += router.urls

