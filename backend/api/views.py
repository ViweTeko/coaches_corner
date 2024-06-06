"""This script provides Views for the API."""
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, PlayerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, Player

class NoteListCreate(generics.ListCreateAPIView):
    """View for listing and creating notes."""
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        """Return the notes created by the user."""
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        """Associate the author with the note."""
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    """View for deleting a note."""
    serializer_class = NoteSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        """Return the notes created by the user."""
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    """View for creating a new user."""
    queryset = User.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = UserSerializer

class PlayerList(generics.APIView):
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

class PlayerDetail(generics.APIView):
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

class thePlay(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, or deleting a specific player using generic view.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer