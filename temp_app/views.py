from django.shortcuts import render
import random
import time
from temp_app.models import TableOne, TableTwo
from django.core.cache import cache


def temp_views(request):
    start_time = time.time()
    counter = cache.get('counter')
    if not counter:
        table_one = TableOne.objects.all()
        counter = 0
        for _ in table_one:
            counter += 1
        print(counter)
        cache.set('counter', counter, timeout=None)
    end_time = time.time()
    work_time = end_time - start_time
    return render(request, 'temp.html', {'work_time': work_time})

