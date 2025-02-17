"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework.documentation import include_docs_urls  # new
from rest_framework.schemas import get_schema_view  # new
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

API_TITLE = 'Blog API'  # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'  # new
schema_view = get_schema_view(title=API_TITLE)  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),  # API الأساسية
    path('api-auth/', include('rest_framework.urls')),  # تسجيل الدخول إلى API
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),  # مصادقة REST
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),  # تسجيل المستخدمين

    # مخطط OpenAPI (JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # توثيق Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),

    # توثيق Redoc (بديل)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
