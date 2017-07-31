{%- extends 'null.tpl' -%}

{%- block input %}
{{ cell.source | ipython2python }}
{%- endblock input %}

{% block output -%}
{% if 'text/plain' in output.data -%}
{{ output.data['text/plain'] | comment_lines }}
{% elif 'text' in output -%}
{{ output['text'] | comment_lines }}
{% endif -%}
{% endblock output -%}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}