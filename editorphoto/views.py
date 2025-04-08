from django.shortcuts import render, redirect, get_object_or_404
from .models import UserImage
from .forms import ImageUploadForm
from PIL import Image, ImageDraw, ImageFont
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
import os




def editor_page(request):
    return HttpResponse("this is editor page")





@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('list')
    else:
        form = ImageUploadForm()
    return render(request, 'gallery/upload.html', {'form': form})





@login_required
def list_images(request):
    images = UserImage.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'gallery/list.html', {'images': images})






@login_required
def black_and_white(request, image_id):
    img = get_object_or_404(UserImage, id=image_id, user=request.user)
    path = img.original.path
    image = Image.open(path).convert('L')
    edited_path = path.replace('original', 'edited')
    image.save(edited_path)
    img.edited.name = edited_path.split('media/')[-1]
    img.save()
    return redirect('list')





@login_required
def add_watermark_view(request, image_id):
    img = get_object_or_404(UserImage, id=image_id, user=request.user)
    path = img.original.path
    image = Image.open(path).convert("RGBA")
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    text = "Watermark"
    w, h = draw.textsize(text, font)
    draw.text(((image.width - w) / 2, (image.height - h) / 2), text, font=font, fill=(255, 255, 255, 128))

    out = Image.alpha_composite(image, watermark).convert("RGB")
    edited_path = path.replace('original', 'edited')
    out.save(edited_path)

    img.edited.name = edited_path.split('media/')[-1]
    img.save()
    return redirect('list')
