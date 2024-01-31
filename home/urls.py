
from django.urls import path, include
from home import views

app_name = 'home'

bucket_urls = [
    path('', views.BucketHome.as_view(), name='bucket'),
    path('delete_bucket/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_bucket'),
    path('download_bucket/<str:key>/', views.DownloadBucketObject.as_view(), name='download_bucket'),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]