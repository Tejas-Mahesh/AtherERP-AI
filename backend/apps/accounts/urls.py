from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    UserViewSet,
    UserProfileViewSet,
    RoleViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()

router.register(
    r"users",
    UserViewSet,
    basename="users",
)

router.register(
    r"profiles",
    UserProfileViewSet,
    basename="profiles",
)

router.register(
    r"roles",
    RoleViewSet,
    basename="roles",
)

urlpatterns = router.urls + [

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]