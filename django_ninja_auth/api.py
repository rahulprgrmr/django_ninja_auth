from ninja import NinjaAPI
from users.views import router as user_router

api = NinjaAPI()

api.add_router("/users", user_router)