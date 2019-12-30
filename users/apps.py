from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """
		
		it imports our signal
		
		"""
        import users.signals
