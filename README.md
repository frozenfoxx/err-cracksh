# errbot-cracksh
Errbot plugin to query [https://crack.sh](https://crack.sh)'s API.

# Prerequisites
* Python 3+

# Installation
* `!repos install https://github.com/frozenfoxx/errbot-cracksh`
* `!plugin config CrackSh {'api_url': 'https://crack.sh/api', 'customer_id': '', 'email': ''}`

# Configuration
Default configuration:
* `!plugin config CrackSh {'api_url': 'https://crack.sh/api', 'customer_id': '', 'email': ''}`

You can customize your installation with the following keys:
* __customer_id__: your customer ID if a paying customer.
* __email__: your email address for status updates.
* __api_url__: the API URL for [https://crack.sh](https://crack.sh).

Email and Customer ID can be overriden per-command if desired using `--email` and `--customerid` respectively.

# Usage
* __Submit a token for work:__ `!cracksh submit [format] [sometoken]`
* __Submit a token with an email override:__ `!cracksh submit --email [user]@[domain] [format] [sometoken]`
* __Submit a token for a customer with ASAP priority:__ `!cracksh submit --customerid [customer ID] --asap 1 [format] [sometoken]`
* __Check status of a job:__ `!cracksh status [reference]`