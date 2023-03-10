from django.urls import path, include
from . import views

urlpatterns = [
    # general
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('settings', views.settings, name="settings"),

    # mystery related
    path('create', views.create_mystery, name="create_mystery"),
    path('mysteries', views.mysteries, name="mysteries"),
    path('mystery/<int:myst_id>', views.view_mystery, name="view_mystery"),
    path('answer/<int:myst_id>', views.answer_mystery, name="answer_mystery"),
    path('review/<int:ans_id>', views.review_answer, name="review"),
    path('tag/<str:tag_name>', views.mysteries_by_tag, name="tag"),

    # auth
    path('accounts/login', views.log_in, name="login"),
    path('accounts/signup', views.sign_up, name="signup"),
    path('profile/my_account', views.profile, name="profile"),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
    path('logout', views.logout_view, name="logout"),
]
