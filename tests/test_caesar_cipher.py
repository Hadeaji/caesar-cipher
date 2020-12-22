from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,force

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual = encrypt('It was the best of times, it was the worst of times.',2)
    expected = 'Kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.'
    assert actual == expected

def test_decrypt():
    actual = decrypt('Kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.',2)
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected

def test_force():
    actual = force('Kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.')
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected