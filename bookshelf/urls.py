from django.urls import path
from . import views

urlpatterns = [
    # 1. The Dashboard (Home page)
    path('', views.dashboard, name='dashboard'),

    # 2. Favorites Page
    path('favorites/', views.favorites, name='favorites'),

    # 3. Add Book Page
    path('add/', views.add_book, name='add_book'),

    # 4. Quick Action URL: Move book from To Read -> Reading
    # <int:book_id> acts as a placeholder. E.g., 'start-reading/3/' runs the view for book ID 3.
    path('start-reading/<int:book_id>/', views.start_reading, name='start_reading'),

    # 5. Quick Action URL: Mark book as Completed (and give it a rating)
    path('complete-reading/<int:book_id>/', views.complete_reading, name='complete_reading'),
]
