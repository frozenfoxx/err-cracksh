* -*- coding: utf -*-

from errbot import BotPlugin, arg_botcmd, webhook
import argparse
import requests

class CrackSh(BotPlugin):

    def get_configuration_template(self):
        """ Configuration entries """

        config = {
            'email': '',
            'customer_id': '',
            'api_url': 'https://crack.sh/api'
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

    @arg_botcmd('token', type=str, help="Token to submit", template="cracksh_submit")
    def submit(self, msg, token=None):