from config.wsgi import *

from core.erp.models import Categoria
from core.erp.models import Categoria, Producto

# listar

# query = Categoria.objects.all()
# print(query)

# cat = Categoria()
# cat.nombre = 'Cableado Estructurado'
# cat.descripcion = 'Cable UTP categoria 6'
# cat.save()

# cat = Categoria.objects.get(id=1)
# print(cat.nombre)

# cat = Categoria.objects.get(pk=3)
# cat.delete()

# obj = Categoria.objects.filter(nombre__icontains='cab')
# # # print(obj)