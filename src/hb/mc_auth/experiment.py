from mojang_api.servers.authserver import authenticate_user
response = authenticate_user("stevenyang0924mj@gmail.com","diamond_pickaxe_278",request_user=True)
print(response)