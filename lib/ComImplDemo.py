from .DinfoPythonService import BaseCom
import json


class ComImplDemo(BaseCom):
    def sparkExecute(self, inputData, paramMap):
        print("实现sparkExecute")
        py_out = len(json.dumps(inputData)) + len(json.dumps(paramMap))
        return py_out
