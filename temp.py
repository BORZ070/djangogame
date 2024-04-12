def parent_detail(request, order_number_id):
    order_number = Order_number.objects.get(id=order_number_id)
    return render(request, 'order_number_detail.html', {'order_number': order_number})


<h1>{{ order_number.name }}</h1>

<h2>order_item:</h2>
<ul>
  {% for order_item in order_number.order_item_set.all %}
    <li>{{ order_item.name }}</li>
  {% endfor %}
</ul>