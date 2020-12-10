import os

import yaml


class Test1:

    def test_aa(self):
        assert 1==1
        # print(os.getcwd())
        #
        # with open("../datas/contactdata.yml",encoding="utf-8") as f:
        #     contactdata = yaml.safe_load(f)
        #     for i in contactdata[0]:
        #         print(i)
        sex = "女"
        print(f"//*[@text='{sex}']")
