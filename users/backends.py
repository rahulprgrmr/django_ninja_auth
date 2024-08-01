from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # TODO: Implement authentication logic here
        User = get_user_model()
        if not User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).exists():
            return None
        user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).first()

        if not user.check_password(password):
            return None

        return user
        

    def get_user(self, user_id):
        # TODO: Implement user retrieval logic here
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None