# -*- coding: utf -*-

from errbot import BotPlugin, arg_botcmd, webhook
import argparse
import requests

class CrackSh(BotPlugin):
    """ Interface for https://crack.sh API """

    def get_configuration_template(self):
        """ Configuration entries """

        config = {
            'email': '',
            'customer_id': '',
            'api_url': 'https://crack.sh/api',
            'status_url': 'https://crack.sh/status'
        }
        return config

    def _check_config(self, option):
        """ Check for option in config """

        if self.config is None:
            return None
        else:
            if option in self.config:
                return self.config[option]
            else:
                return None

    @arg_botcmd('format', type=str, help="Format of token", template="cracksh_submit")
    @arg_botcmd('token', type=str, help="Token to submit", template="cracksh_submit")
    @arg_botcmd('--customerid', dest='customer_id', type=str, default=None, help="Customer ID", template="cracksh_submit")
    @arg_botcmd('--email', dest='email', type=str, default=None, help="Email for updates", template="cracksh_submit")
    @arg_botcmd('--asap', dest='asap', type=int, default=0, help="Whether to rush a job", template="cracksh_submit")
    def cracksh_submit(self, msg, format=None, token=None, customer_id=None, email=None, asap=None):
        """ Submit a token to https://crack.sh
            Examples:
            !cracksh submit [format] [sometoken]
            !cracksh submit --email someone@somewhere.net [format] [sometoken]
            !cracksh submit --customerid lucas --asap 1 [format] [sometoken]
        """

        sess = requests.Session()
        head = {}
        url = self._check_config('api_url')
        payload = {'token': format + ':' + token, 'asap': asap}

        # Check for customer_id override
        if customer_id != None:
            payload['customer_id'] = customer_id
        elif self.config['customer_id'] != '':
            payload['customer_id'] = self.config['customer_id']

        # Check for email override
        if email != None:
            payload['email'] = email
        elif self.config['email'] != '':
            payload['email'] = self.config['email']

        try:
            response = sess.post(url, headers=head, data=payload, timeout=30)
            self.log.debug('URL sent: {}'.format(url))
        except Exception as e:
            self.log.debug(e)
        self.check_response(response)

        return {'subresp': response.json()}

    @arg_botcmd('reference', type=str, help="Reference ID", template="cracksh_status")
    def cracksh_status(self, msg, reference=None):
        """ Check the status of a submitted job
            Examples:
            !cracksh status [reference]
        """

        sess = requests.Session()
        head = {}
        url = self._check_config('status_url')
        payload = { 'id': reference }

        try:
            response = sess.get(url, headers=head, data=payload, timeout=30)
            self.log.debug('URL sent: {}'.format(url))
        except Exception as e:
            self.log.debug(e)
        self.check_response(response)

        return {'statresp': response.json()}

    @staticmethod
    def check_response(response):
        if response.status_code != 200:
            raise ValueError(
                'Request to API returned an error {0}, the response is: {1}'.format(response.status_code, response.text)
            )
