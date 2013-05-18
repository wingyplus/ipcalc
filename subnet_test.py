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

def test_word_must_return_tuple_3():
    my_ip = MyIPAddress('11111111.11111111.11111111.11111111')
    eq_(my_ip.words, (255, 255, 255, 255))

def test_addr_with_given_number_of_binary():
    my_ip = MyIPAddress('26')
    eq_(str(my_ip), '255.255.255.192')

def test_ip_network():
    ip = MyIPNetwork('192.168.5.0/26')

    ok_(isinstance(ip.addr, MyIPAddress))
    ok_(isinstance(ip.netmask, MyIPAddress))
    eq_(str(ip.addr), '192.168.5.0')
    eq_(str(ip.netmask), '255.255.255.192')
