#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
import gmail

# external libraries
# N/A

#-----------------------------------------------------------------------


class PluginError(RuntimeError):
    pass


class PluginReceiver(object):

    plugins = {}

    def attach_plugin(self, plugin):
        if self.plugins[plugin.name]:
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

    def send_email(self, msg):
        gmail.send_email(self.address, self.password, msg)
