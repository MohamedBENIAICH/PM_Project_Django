from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student


@api_view(['POST'])
def save_student(request):
    # Log the incoming request data to the console
    print(f"Received data: {request.data}")

    # Extract data from the request
    name = request.data.get('name')
    image = request.data.get('imageUri')
    is_present = request.data.get('isPresent')

    # Check if data is missing
    if not name or not image or is_present is None:
        return Response({"error": "Missing required data"}, status=400)

    # Save data to database
    student = Student.objects.create(name=name, image=image, is_present=is_present)

    print(f"Student saved: {student.id}")  # Log the saved student ID

    return Response({"message": "Student saved successfully"}, status=201)
