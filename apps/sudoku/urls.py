from django.conf.urls import url

from apps.sudoku.views import SudokuView, SudokuStatusView

urlpatterns = [
    url(r'^generate/$', SudokuView.as_view()),
    url(r'^status/$', SudokuStatusView.as_view()),
]
