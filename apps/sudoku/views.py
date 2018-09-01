from pytz import unicode
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sudoku.models import SudokuDetail
from apps.sudoku.serializers import sudokuSerializers
from apps.sudoku.utils import SudokuUtils


class SudokuView(APIView):
    authentication_classes = (SessionAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = SudokuUtils.init_sudoku(data=request.data)
        serializer = sudokuSerializers(queryset)
        return Response(serializer.data)


class SudokuStatusView(APIView):
    authentication_classes = (SessionAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = SudokuUtils.sudoku_status(pk=self.request.query_params('pk'))
        serializer = sudokuSerializers(queryset)
        return Response(serializer.data)
