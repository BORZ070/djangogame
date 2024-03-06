import os
import django
import random
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogame.settings")
django.setup()


from temp_app.models import TableOne, TableTwo


start_time = time.time()


x = TableOne.objects.filter(tabletwo__info='xxx')
print(len(x))


# if TableOne.objects.all().count() < 100000:
#     for i in range(100000):
#         TableOne.objects.create(title='x', info=i)
#
#
# if TableTwo.objects.all().count() < 100000:
#     for i in range(100000):
#         try:
#             TableTwo.objects.create(table_id=i, title='x', info='xxx')
#         except Exception as exception:
#             print(exception)
#             print('Error id:', i)


end_time = time.time()
work_time = end_time - start_time
print(work_time)