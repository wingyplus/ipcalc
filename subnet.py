import re

class MyIPAddress(object):

    def __init__(self, ip):
        self._ip = ip

    @property
    def addr(self):
    	ip_t = self._tuple_from(self._ip)
        return '.'.join([str(d) for d in ip_t])

    @property
    def words(self):
        ip_t = self._tuple_from(self._ip)
        return ip_t

    def _tuple_from(self, ip):
        # matching pattern 11111111.11111111.11111111.11111111
        if re.match('^[0-1]{8}.[0-1]{8}.[0-1]{8}.[0-1]{8}$', ip):
            return tuple([255 and int(word, 2) for word in ip.split('.')])
        # matching pattern 255.255.255.255
        if re.match('^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', ip):
            return tuple([int(d) for d in ip.split('.')])
        # matching pattern 255.255.255.255/32
        elif re.match('^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/\d{2}$', ip):
            return tuple([int(d) for d in ip.split('/')[0].split('.')])