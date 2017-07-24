__*Job Status*__

*Status*: {{ statresp["status"]|e }}
{% if statresp["status"] == 'finished' %}

*Result*: {{ statresp["result"]|e }}
{% elif statresp["status"] == 'running' %}

*Progress*: {{ statresp["progress"]|e }}%
{% elif statresp["queued"] %}

*Progress*: approximately {{ statresp["progress"]|e }} hours to begin
{% elif statresp["error"] %}

*Details*: {{ statresp["error_msg"]|e }}
{% endif %}