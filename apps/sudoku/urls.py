from django.conf.urls import url

from apps.sudoku.views import SudokuView

urlpatterns = [
    url(r'^generate', SudokuView.as_view()),
]
