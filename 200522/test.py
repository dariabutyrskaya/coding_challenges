from main import upped

def test_upped(monkeypatch):
    # provided inputs
    s = 'sss'
    
    # creating iterator object
    iter_obj = iter([s])

    # using lambda statement for mocking
    monkeypatch.setattr('builtins.input', lambda name: next(iter_obj))

    assert upped("") == SSS, "Should return SSS"
