""" This script provides data for the players to show in database"""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from config import db
#from models import Player
#from serializers import PlayerSerializer


class PlayerTable(db.Model):
    """This class will be the database model represented as Python class"""

    playerID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Float, unique=False, nullable=False)
    height = db.Column(db.Float, unique=False, nullable=False)
    school = db.Column(db.String(120), unique=False, nullable=False)

    def to_json(self):
        """ This function takes all fields and converts into JSON"""
        return {
                "id": self.playerID,
                "fisrtName": self.fisrt_name,
                "lastName": self.last_name,
                "school": self.school,
                "age": self.age,
                "weight": self.weight,
                "height": self.height,
                }


class PlayerList(APIView):
  """
  API endpoint for listing and creating players.
  """
  def getPlayer(self, request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
  """
  API endpoint for retrieving, updating, or deleting a specific player.
  """
  def get_object(self, pk):
    player = get_object_or_404(Player, pk=pk)
    return player

  def get(self, request, pk):
    player = self.get_object(pk)
    serializer = PlayerSerializer(player)
    return Response(serializer.data)

  def put(self, request, pk):
    player = self.get_object(pk)
    serializer = PlayerSerializer(player, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    player = self.get_object(pk)
    player.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
