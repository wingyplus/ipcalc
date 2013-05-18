import re

class MyIPAddress(object):

    def __init__(self, ip, has_netmask=True):
        self._ip, self._netmask = [self._tuple_from(addr) for addr in self._split(ip)]

    @property
    def addr(self):
        return '.'.join([str(d) for d in self._ip])

    @property
    def words(self):
        return self._ip

    @property
    def netmask(self):
        return '.'.join([str(d) for d in self._netmask])


    def _split(self, ip):
        if re.match(r'^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/\d{2}$', ip):
            addr, netmask = ip.split('/')
        else:
            addr, netmask = ip, '255.255.255.255'

        return addr, netmask


    def _tuple_from(self, ip):
        # matching pattern 11111111.11111111.11111111.11111111
        if re.match(r'^[0-1]{8}.[0-1]{8}.[0-1]{8}.[0-1]{8}$', ip):
            return tuple([255 and int(word, 2) for word in ip.split('.')])
        # matching pattern 255.255.255.255
        elif re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', ip):
            return tuple([int(d) for d in ip.split('.')])
        # matching pattern 255.255.255.255/32
        elif re.match(r'^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/\d{2}$', ip):
            return tuple([int(d) for d in ip.split('/')[0].split('.')])
        elif re.match(r'^\d{2}$', ip):
            binary_addr = '1' * int(ip) + '0' * (32 - int(ip))
            binary_addr_with_dot = re.sub(r'^([0-1]{8})([0-1]{8})([0-1]{8})([0-1]{8})$', r'\1.\2.\3.\4', binary_addr)

            return self._tuple_from(binary_addr_with_dot)