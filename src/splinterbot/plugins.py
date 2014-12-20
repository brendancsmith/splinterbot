#------------------------------ imports --------------------------------

# standard modules
from datetime import datetime

# intra-project modules
from gmail import GmailServer

# external libraries
# N/A

#-----------------------------------------------------------------------


class PluginError(RuntimeError):
    pass


class PluginReceiver(object):

    plugins = {}

    def attach_plugin(self, plugin):
        if (plugin.name in self.plugins) and \
           (self.plugins[plugin.name] is not None):
            raise PluginError('Plugin {0} is already loaded on {1}'.format(
                              plugin.name, self))
        else:
            self.plugins[plugin.name] = plugin


class AbstractPlugin(object):

    name = None


class Gmail(AbstractPlugin):

    name = 'gmail'

    def __init__(self, address, password):
        super(Gmail, self).__init__()
        self.address = address
        self.password = password

    @staticmethod
    def timestamp():
        #TODO: use the datetime formatter
        return str(datetime.now())

    def send_email(self, msg, to=None):
        if to is None:
            to = self.address

        # avoid colons in the email message
        with GmailServer(self.address, self.password) as mailServer:
            mailServer.sendmail(self.address, [to], msg)
