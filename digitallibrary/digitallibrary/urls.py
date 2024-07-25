"""
URL configuration for digitallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from digital_library_app import views as digital_lib_views
from rest_framework.routers import DefaultRouter
book_router = DefaultRouter()
book_router.register(r"Book", digital_lib_views.BookView)
# urlpatterns = [
#     # Планы
#     path("educational_plan/", include(educational_plan_router.urls)),
#     # Направления
#     path("direction/", include(direction_router.urls)),
#     path("subject_for_plan/", include(subject_for_plan_router.urls)),
#     path("type/", include(type_router.urls)),
#     path("tutor/", include(tutor_router.urls)),
#     path("semester/", include(semester_router.urls)),
#     path("competention/", include(competention_router.urls)),
#     path("subject_type/", include(subject_type_router.urls)),
#     path("attestation_form/", include(atestation_form_router.urls)),
# ]
urlpatterns = [
    path("admin/", admin.site.urls),
    path("digital_lib_app/",digital_lib_views.crud_view),
    path("books/",include(book_router.urls))
]
