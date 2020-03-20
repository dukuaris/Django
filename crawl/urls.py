from django.urls import path, re_path
from crawl import views


app_name = 'crawl'
urlpatterns = [

    # Example: /product/

    # Example: /crawl/product/ (same as /crawl/)
    path('product/', views.ProductLV.as_view(), name='product_list'),

    # Example: /crawl/archive/
    path('product/<int:pk>/', views.ProductDV.as_view(), name='product_detail'),

    # Example: /crawl/search/
    path('scrape/', views.CrawlFormView.as_view(), name='scrape'),

    # Example: /crawl/add/
    # path('add/', views.ProductCreateView.as_view(), name="add"),

    # # Example: /crawl/change/
    # path('change/',
    #      views.PostChangeLV.as_view(), name="change",
    # ),
    #
    # # Example: /crawl/99/update/
    # path('<int:pk>/update/',
    #      views.PostUpdateView.as_view(), name="update",
    # ),
    #
    # # Example: /crawl/99/delete/
    # path('<int:pk>/delete/',
    #      views.PostDeleteView.as_view(), name="delete",
    # ),
]
