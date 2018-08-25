from pytz import unicode
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sudoku.utils import SudokuUtils


class SudokuView(APIView):
    authentication_classes = (SessionAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sudoku = SudokuUtils.init_sudoku()
        print(sudoku)
        return Response(sudoku)

