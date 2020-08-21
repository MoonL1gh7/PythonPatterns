def secret_controller(request):
    request['secret_key'] = 'SECRET_KEY'


front_controllers = [
    secret_controller
]
