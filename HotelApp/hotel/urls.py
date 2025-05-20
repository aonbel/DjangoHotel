from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import qazzy.views as views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('home', views.homepage, name="homepage"),
    path('about', views.aboutpage, name="aboutpage"),
    path('contact', views.contactpage, name="contactpage"),
    path('policy', views.policypage, name="policypage"),
    path('faq', views.faq, name="faq"),
    path('user', views.user_log_sign_page, name="userloginpage"),
    path('promocode-list', views.promocode_list, name="promocode_list"),
    path('feedback/list', views.feedback_list, name="feedback_list"),
    re_path(r'^user/login$', views.user_log_sign_page, name="userloginpage"),
    path('user/bookings', views.user_bookings, name="dashboard"),
    path('user/book-room', views.book_room_page, name="bookroompage"),
    path('user/book-room/book', views.book_room, name="bookroom"),
    re_path(r'^user/signup$', views.user_sign_up, name="usersignup"),
    path('staff/', views.staff_log_sign_page, name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page, name="staffloginpage"),
    path('staff/signup', views.staff_sign_up, name="staffsignup"),
    path('news', views.news_list, name="news_list"),
    path('staff/add_news', views.add_news, name="add_news"),
    path('news/<int:news_id>/', views.news_detail, name="news_detail"),
    path('vacancies', views.vacancy_list, name="vacancy_list"),
    path('staff/add_vacancy', views.add_vacancy, name="add_vacancy"),
    path('contacts', views.contact_list, name="contact_list"),
    path('staff/add_contact', views.add_contact, name="add_contact"),
    path('logout', views.logoutuser, name="logout"),
    re_path(r'^staff/panel$', views.panel, name="staffpanel"),
    re_path(r'^staff/allbookings$', views.all_bookings, name="allbookigs"),
    re_path(r'^staff/panel/add-new-location$', views.add_new_location, name="addnewlocation"),
    re_path(r'^staff/panel/edit-room$', views.edit_room),
    re_path(r'^staff/panel/add-new-room$', views.add_new_room, name="addroom"),
    re_path(r'^staff/panel/delete-room$', views.delete_room, name="deleteroom"),
    re_path(r'^staff/panel/view-room$', views.view_room),
    re_path(r'^staff/panel/add-new-promo$', views.add_new_promo, name="addnewpromo"),
    re_path(r'^user/add_feedback$', views.add_feedback, name="addfeedback"),
    re_path(r'^staff/panel/add-new-faq$', views.add_faq, name="addnewfaq"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)