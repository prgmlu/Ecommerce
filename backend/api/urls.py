from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'product', views.ProductViewSet, 'Product')

urlpatterns = router.urls
