__*Token Submission*__
Token submitted.

*Status*: {{ subresp["status"]|e }}

*Reference ID*: {{ subresp["reference"]|e }}

{% if subresp["status"] == 'error' %}
*Errors*: {{ subresp["error_msg"]|e }}
{% endif %}