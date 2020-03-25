from django.shortcuts import render

# Create your views here.
tags = ['น้ำตก', 'น้ำพุร้อน', 'ธรรมชาติ', 'หน้าฝน', 'ตากหมอก']
obj1 = {
    'name' : 'บทความท่องเที่ยวภาคเหนือ',
    'author' : 'lockdoor',
    'price' : 100,
    'tags' : tags,
    'rating' : 4
}
obj2 = {
    'name' : 'บทความท่องเที่ยวภาคกลาง',
    'author' : 'lockdoor',
    'price' : 100,
    'tags' : tags,
    'rating' : 4
}

def north(request):
    return render(request, "index.html", obj1)

def central(request):
    return render(request, "index.html", obj2)