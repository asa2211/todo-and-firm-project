from rest_framework import generics, permissions

from .models import ToDoModel, CustomUser
from .serializer import UserSerializer, TodoSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AdminUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(roles='3')


class ManagerUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(roles='2')


class TodoCreateView(generics.CreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoCurrentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoCompletedView(generics.ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = ToDoModel.objects.all()
        user_id = self.request.user
        if user_id:
            queryset = queryset.filter(user=user_id, completed=True)
        return queryset
