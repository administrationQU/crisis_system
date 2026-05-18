from django.shortcuts import render, get_object_or_404
from .models import Category, Topic, Step
from django.db.models import Q
from django.http import HttpResponse

def search(request):
    query = request.GET.get('q')

    topics = []
    not_found = False

    if query:
        topics = Topic.objects.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query)
        )

        if not topics.exists():
            not_found = True

    return render(request, 'search.html', {
        'topics': topics,
        'query': query,
        'not_found': not_found
    })


# 🏠 Home
def home(request):
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'categories': categories
    })


# 📂 Topics
def topics(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    topics = Topic.objects.filter(category=category)

    return render(request, 'topics.html', {
        'category': category,
        'topics': topics
    })


# 📋 Protocol
def protocol_view(request, topic_id):

    protocol = get_object_or_404(
        Protocol,
        topic_id=topic_id
    )

    steps = Step.objects.filter(
        protocol=protocol
    ).order_by('step_number')

    return render(request, 'protocol.html', {
        'protocol': protocol,
        'steps': steps
    })


# ❌ Error Pages
def custom_error_view(request, exception=None):

    status_code = 500

    if exception:
        status_code = getattr(exception, 'status_code', 404)

    context = {
        'status_code': status_code,
        'message': "حدث خطأ غير متوقع"
    }

    if status_code == 404:
        context['message'] = "عذراً، الصفحة التي تبحث عنها غير موجودة."

    elif status_code == 403:
        context['message'] = "ليس لديك صلاحية للوصول لهذه الصفحة."

    elif status_code == 500:
        context['message'] = "مشكلة في السيرفر، نحن نعمل على إصلاحها."

    return render(
        request,
        'error_page.html',
        context,
        status=status_code
    )