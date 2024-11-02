from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/', contact_view, name='contact-page'),
    path('blog_grid/',bloggrid_view,name='blog-grid-page'),
    path('blog/',blog_view,name='blog-page'),
    path('service/',services_view,name='service-page'),
    path('about/',about_view,name='about-page'),
    path('blog_detail/',blogdetail_view,name='blog-detal-page'),
    path('career/',career_view,name='career-page'),
    path('cart/',cart_view,name='cart-page'),
    path('checkout/',checkout_view,name='checkout-page'),
    path('computer_repair/',comprepair_view,name='comprepair-page'),
    path('contact_2/',contact_2_view,name='contact2-page'),
    path('data_recovery/',datarec_view,name='data-page'),
    path('error/',error_view,name='error-page'),
    path('faq/',faq_view,name='faq-page'),
    path('home_dark/',homedark_view,name='home-dark-page'),
    path('home/',home_view,name='home-page'),
    path('make_appointment/',make_view,name='makeapp-page'),
    path('mobile_service/',mobileserver_view,name='mobile-service-page'),
    path('network_solution/',network_view,name='network-page'),
    path('news/',news_view,name='new-page'),
    path('price/',price_view,name='price-page'),
    path('privacy_policy/',policy_view,name='policy-page'),
    path('service_detail/',servicedetal_view,name='service-detal-page'),
    path('service_list/',servicelist_view,name='service-list-page'),
    path('shop_details/',shopdetal_view,name='shop-detal-page'),
    path('shop/',shop_view,name='shop-page'),
    path('techn_support/',tech_view,name='tech-page'),
    path('term_condition/',term_view,name='term-page'),
]
    