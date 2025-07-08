from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import io

def index(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        try:
            image = Image.open(image_file)
            if image.mode != 'RGB':
                image = image.convert('RGB')

            buffer = io.BytesIO()
            image.save(buffer, format='PDF')
            buffer.seek(0)

            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="converted.pdf"'
            return response
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'testapp/index.html')
