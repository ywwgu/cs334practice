

from cs334demo.hello import APP


def test_hello():
    APP.config['TESTING'] = True
    client = APP.test_client()

    result = client.get('/')
    assert b'Hello, World!' in result.data
