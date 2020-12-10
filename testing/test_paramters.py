import yaml


def test_hh():
    with open('../datas/cal.yml') as f:
        params = yaml.safe_load(f)

    print(params)
    print(params[2]['ids'])
