from django.conf.urls import url

from products import api_views

urlpatterns = [
	url(r'^get-products-dt/$', api_views.get_products_dt, name='get_products_dt'),
	url(r'^get-products/$', api_views.get_products, name='get_products'),
	url(r'^product/(?P<uuid>.+)/$', api_views.get_product, name='get_product'),
	url(r'^delete-product/(?P<uuid>.+)/$', api_views.delete_product, name='delete_product'),
	url(r'^add-product/$', api_views.add_product, name='add_product'),
	url(r'^update-product/(?P<uuid>.+)/$', api_views.update_product, name='update_product'),
	url(r'^upload-file/$', api_views.upload_file, name='upload_file'),
	url(r'^update-file/(?P<uuid>.+)/$', api_views.update_file, name='update_file'),
	url(r'^search-product/$', api_views.search_product, name='search_product'),
]