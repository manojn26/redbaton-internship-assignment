from django.contrib import admin
from django.urls import path,re_path
from .views import index,sign_up,logout,login_user,password_change,profile,bookmark,filldetails,marked_read,marked_read_details,deleteitem,bookmark_details


app_name = "Entry"

urlpatterns = [
    # 1. Creating User
    path("accounts/signup",sign_up,name="sign_up"),

    # 2. Login
    path("accounts/login",login_user,name="login_user"),

    # 3. Logout
    path("accounts/logout",logout,name="logout"),

    # 4. Password Change
    path("accounts/password-change",password_change,name="password_change"),

    # 12. Fill User Details
    path("filldetails/",filldetails,name="filldetails"),

    # 5. Index View
    path("index/",index,name="index"),

    # 6. Users Profile View
    path(r'profile/<user>', profile, name='profile'),

        # 7. Marked As Read
    path('marked-read/', marked_read, name="marked_read"),
    re_path(r'^index/marked-read/(?P<hid>[0-9]+)/$', marked_read_details, name="read"),
    
    # 8. Bookmarks or View All Bookmarks
    path('bookmark/', bookmark, name='bookmark'),
    # 9. Add Bookmark
    re_path(r'^index/bookmark/(?P<hid>[0-9]+)/$', bookmark_details, name="details"),
    # 10. Remove Bookmarks
    re_path(r'^bookmark/remove/(?P<hid>[0-9]+)$', bookmark_details, name="details"),
    
    # 11. Delete Item from a user's view.
    re_path(r'^index/deleteitem/(?P<hid>[0-9]+)/$', deleteitem, name="deleteitem")
    


]
