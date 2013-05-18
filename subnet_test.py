from nose.tools import eq_, ok_
from subnet import MyIPAddress, MyIPNetwork

def test_address_with_given_binary_address_1():
    my_ip = MyIPAddress('11111111.11111111.11111111.11111111')
    eq_(str(my_ip), '255.255.255.255')

def test_address_with_given_binary_address_2():
    my_ip = MyIPAddress('11111111.11111111.11111111.00000000')
    eq_(str(my_ip), '255.255.255.0')

def test_address_with_given_dec_address_1():
    my_ip = MyIPAddress('255.255.255.255')
    eq_(str(my_ip), '255.255.255.255')

def test_address_with_given_dec_address_2():
    my_ip = MyIPAddress('192.168.5.0')
    eq_(str(my_ip), '192.168.5.0')

def test_word_must_return_tuple_1():
    my_ip = MyIPAddress('1.1.1.1')
    eq_(my_ip.words, (1, 1, 1, 1))

def test_word_must_return_tuple_2():
    my_ip = MyIPAddress('11111111.11111111.11111111.11111111')
    eq_(my_ip.words, (255, 255, 255, 255))

def test_addr_with_given_number_of_binary():
    my_ip = MyIPAddress('26')
    eq_(str(my_ip), '255.255.255.192')

def test_bin_function():
    my_ip = MyIPAddress('255.255.255.255')
    eq_(my_ip.binary_words, ('0b11111111','0b11111111','0b11111111','0b11111111'))

def test_and_operator():
    ip1 = MyIPAddress('192.168.1.1')
    ip2 = MyIPAddress('255.255.255.0')

    result = ip1 & ip2

    ok_(isinstance(result, MyIPAddress))
    eq_(str(result), '192.168.1.0')

def test_or_operator():
    ip1 = MyIPAddress('192.168.1.1')
    ip2 = MyIPAddress('0.0.0.255')

    result = ip1 | ip2

    ok_(isinstance(result, MyIPAddress))
    eq_(str(result), '192.168.1.255')

def test_invert_operator():
    ip1 = MyIPAddress('24')

    result = ~ip1

    ok_(isinstance(result, MyIPAddress))
    eq_(str(result), '0.0.0.255')

def test_ip_network():
    ip = MyIPNetwork('192.168.5.0/26')

    ok_(isinstance(ip.addr, MyIPAddress))
    ok_(isinstance(ip.netmask, MyIPAddress))
    eq_(str(ip.addr), '192.168.5.0')
    eq_(str(ip.netmask), '255.255.255.192')

def test_default_netmask():
    ip = MyIPNetwork('192.168.5.0')

    eq_(str(ip.netmask), '255.255.255.255')

def test_ip_network_prefix():
    ip = MyIPNetwork('192.168.5.130/24')

    ok_(isinstance(ip.network, MyIPAddress))
    eq_(str(ip.network), '192.168.5.0')

def test_ip_broadcast():
    ip = MyIPNetwork('192.168.0.1/24')

    ok_(isinstance(ip.broadcast, MyIPAddress))
    eq_(str(ip.broadcast), '192.168.0.255')

def test_broadcast_for_c_network_class():
    ip = MyIPNetwork('192.168.0.1/25')

    eq_(str(ip.broadcast), '192.168.0.127')
