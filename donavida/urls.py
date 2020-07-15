from django.conf.urls import url
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from donor.views import DonorViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Dona Vida API",
        default_version='v1',
        description="Dona Vida project with MongoDB"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()
router.register('donor', DonorViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
