from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    RoleViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()

router.register(
    r"users",
    UserViewSet,
    basename="user",
)

router.register(
    r"roles",
    RoleViewSet,
    basename="role",
)

router.register(
    r"profiles",
    UserProfileViewSet,
    basename="profile",
)

urlpatterns = router.urls