__*Token Submission*__

*Status*: {{ subresp["status"]|e }}

{% if subresp["status"] == 'error' %}

*Errors*: {{ subresp["error_msg"]|e }}

{% else %}

*Reference ID*: {{ subresp["reference"]|e }}
{% endif %}