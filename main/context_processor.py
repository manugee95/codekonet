from .models import AppInfo, Category

def slick(request):
    info = AppInfo.objects.get(pk=1)
    categ = Category.objects.all()

    context = {
        'info':info,
        'categ':categ
    }

    return context 