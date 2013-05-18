import re

class MyIPAddress(object):

    def __init__(self, ip):
        self._ip = self._tuple_from(ip)

    @property
    def words(self):
        '''
        return tuple of decimal ip
        '''
        return self._ip

    @property
    def binary_words(self):
        '''
        return tuple of binary ip
        '''
        return tuple([bin(decimal_addr) for decimal_addr in self._ip])

    def _tuple_from(self, ip):
        # matching pattern 11111111.11111111.11111111.11111111
        if re.match(r'^[0-1]{8}.[0-1]{8}.[0-1]{8}.[0-1]{8}$', ip):
            return tuple([255 and int(word, 2) for word in ip.split('.')])
        # matching pattern 255.255.255.255
        elif re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', ip):
            return tuple([int(d) for d in ip.split('.')])
        # matching pattern 32
        elif re.match(r'^\d{1,2}', ip):
            to_binary_str = lambda ip: '1' * int(ip) + '0' * (32 - int(ip))
            binary_addr = re.sub(r'^(\d{8})(\d{8})(\d{8})(\d{8})$', r'\1.\2.\3.\4', to_binary_str(ip))

            return self._tuple_from(binary_addr)

    def __and__(self, other):
        '''
        return MyIPAddress object result from calculate and bit
        '''
        result = []
        for i in range(4):
            result.append(str(int(self.binary_words[i], 2) & int(other.binary_words[i], 2)))
        return MyIPAddress(".".join(result))

    def __or__(self, other):
        '''
        return MyIPAddress object result from calculate or bit
        '''
        result = []
        for i in range(4):
            result.append(str(int(self.binary_words[i], 2) | int(other.binary_words[i], 2)))
        return MyIPAddress(".".join(result))

    def __invert__(self):
        return MyIPAddress(".".join([str(int(binary_word, 2) ^ int('0b11111111', 2)) for binary_word in self.binary_words]))

    def __str__(self):
        return ".".join([str(word) for word in self._ip])

class MyIPNetwork(object):

    def __init__(self, ip_network):
        # matching pattern 255.255.255.255/32
        if re.match(r'^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/\d{1,2}', ip_network):
            self._addr, self._netmask = [MyIPAddress(ip) for ip in ip_network.split('/')]
        else:
            self._addr, self._netmask = [MyIPAddress(ip) for ip in (ip_network, '255.255.255.255')]

        self._wildcard = ~self._netmask
        self._network = self._addr & self._netmask
        self._broadcast = self._addr | self._wildcard

    @property
    def addr(self):
        return self._addr

    @property
    def netmask(self):
        return self._netmask

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast
