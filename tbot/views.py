from django.shortcuts import render
from django.conf import settings
def tlink_views(request):
    base_link = settings.TGLINK
    with_id_link = settings.TGLINK
    user_id = request.user.id
    with_id_link += f'?start={user_id}'
    print(with_id_link)

    return render(request, 'telegram.html', {'base_link':base_link,
                                             'with_id_link':with_id_link})



