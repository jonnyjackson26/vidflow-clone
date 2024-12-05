from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')  # Optional

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            User.objects.create(username=username, email=email, password=make_password(password))
            return JsonResponse({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            # Login successful
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            # Invalid credentials
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)




@csrf_exempt
def delete_account(request):
    if request.method == "DELETE":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            user = User.objects.get(username=username)
            user.delete()  # Deletes the user from the database
            return JsonResponse({"message": "Account deleted successfully."})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

#TODO: HASH PASSWORDS