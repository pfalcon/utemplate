{% args %}
{% for i in range(5) %}
| {{i}} | {{"%2d" % i ** 2}} |
{% endfor %}
