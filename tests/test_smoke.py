import mlops_bdd100k

def test_smoke():
    assert isinstance(mlops_bdd100k, object)

    assert len(mlops_bdd100k.__version__) > 0
