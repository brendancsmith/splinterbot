#------------------------------ imports --------------------------------

# standard modules
# N/A

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


class EmptyPlugin(object):

    @staticmethod
    def _pass(*args, **kwargs):
        pass

    def __getattr__(self, name):
        return self._pass


class Gmail(AbstractPlugin):

    name = 'gmail'

    def __init__(self, address, password):
        super(Gmail, self).__init__()
        self.address = address
        self.password = password

    def send_email(self, msg, to=None):
        if to is None:
            to = self.address

        # avoid colons in the email message
        with GmailServer(self.address, self.password) as mailServer:
            print('sending: ' + msg)
            mailServer.sendmail(self.address, [to], msg)
