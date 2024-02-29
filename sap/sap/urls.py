
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from webapp.views import bienvenido
from personas.views import detalle_persona, nueva_persona, editar_persona,eliminar_persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detalle_persona ),
    path('nueva_persona', nueva_persona ),
    path('editar_persona/<int:id>', editar_persona ),
    path('eliminar_persona/<int:id>', eliminar_persona )

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
