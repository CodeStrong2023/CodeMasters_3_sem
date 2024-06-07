#hotel_reservations\hotel_reservations\urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Importando las vistas de las aplicaciones
from reservations.views import RoomViewSet, ClientViewSet, ReservationViewSet, RateViewSet, AvailabilityViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'clients', ClientViewSet)  # Cambio "customers" a "clients"
router.register(r'reservations', ReservationViewSet)
router.register(r'rates', RateViewSet)
router.register(r'availabilities', AvailabilityViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="APIs del sistema de reservas del hotel",
        terms_of_service="",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservations.urls')),
    path(
        'swagger<format>.json|.yaml',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
