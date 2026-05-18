import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone # Import timezone to auto-populate the booking_date
from .models import Category, MenuItem, SliderImage, TableBooking

def index(request):
    categories = Category.objects.filter(is_active=True).prefetch_related('items')
    # Fetch all active custom slider images
    slides = SliderImage.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'menu/index.html', {'categories': categories, 'slides': slides})


@csrf_exempt # Allows our JavaScript fetch request to communicate safely
def book_table(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Map your frontend form keys to your TableBooking database model fields
            # NOTE: If your TableBooking field names are slightly different (e.g. phone instead of phone_number), 
            # match them exactly here!
            booking = TableBooking.objects.create(
                customer_name=data.get('name'),
                # Adjust these field names to match your exact TableBooking model variables:
                customer_phone=data.get('phone'), 
                number_of_guests=data.get('guests'),
                booking_time=data.get('time'),
                # If your model requires a specific date, we default it to today's date
                # from django.utils import timezone; booking_date=timezone.now().date()
                booking_date=timezone.now().date(),
                status='PENDING'
            )
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Booking saved to database!',
                'booking_id': booking.id
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)