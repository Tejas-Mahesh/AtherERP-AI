from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet,
    BranchViewSet,
    LocationViewSet,
)

router = DefaultRouter()

router.register(
    r"organizations",
    OrganizationViewSet,
    basename="organization",
)

router.register(
    r"branches",
    BranchViewSet,
    basename="branch",
)

router.register(
    r"locations",
    LocationViewSet,
    basename="location",
)

urlpatterns = router.urls