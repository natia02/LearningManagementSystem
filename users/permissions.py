from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.student is not None


class IsLecturer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.lecturer is not None
