from typing import List, Any
from django.conf.urls import url
from core.erp.views import vistaCategoria

urlpatterns = [
    url('prueba/',vistaCategoria)
]