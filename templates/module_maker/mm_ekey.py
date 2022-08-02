import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey

# TODO: NEED TO FILL OUT DKEY FUNCTIONS / TEMPLATE RENDERING BECAUSE I FORGOT

class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = '{{ name }}'
        self.mtype = 'ekey'
        self.author = '{{ author }}'
        self.description = '{{ description }}'

        self.compatible_omodules = [

            {% for c in compatible_xmodules %}
            '{{ c }}',
            {% endfor %}
        ]

        self.compatible_interfaces = [

            {% for c in compatible_interfaces %}
            '{{ c }}',
            {% endfor %}
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-len',
                                dest='ekey_len',
                                type=int,
                                required=False,
                                default=32,
                                help='Length of encryption key')

        self.parser.add_argument('--ekey-val',
                                dest='ekey_value',
                                type=str,
                                required=False,
                                default=None,
                                help='Manually set encryption key')

        self.parser.add_argument('--ekey-b64',
                                dest='ekey_b64',
                                action='store_true',
                                help='Decode manually set encryption key from base64')

    def generate(self):

        if self.args.ekey_value is None:
            ekey_val = core.helpers.crypto.random_key(length=self.args.ekey_len)
        elif self.args.ekey_b64:
            ekey_val = self.args.ekey_val
        else:
            ekey_val = base64.b64decode(self.args.ekey_val)
        self.ekey_val = ekey_val
        return {
            'val' : ekey_val,
            'len' : self.args.ekey_len,
            'options' : self.args.__dict__,
        }
