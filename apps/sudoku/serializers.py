from rest_framework import serializers

from apps.sudoku.models import SudokuDetail


class sudokuSerializers(serializers.ModelSerializer):
    class Meta:
        model = SudokuDetail
        fields = '__all___'
