import unittest, xmlrunner, json, requests, glob

def abstract_test(self, data, response):
    self.assertEqual(response.status_code, data['assert']['statusCode'])
    self.assertSetEqual(set(response.json().keys()), set(data['assert']['responseKeys']))
    self.assertLessEqual(response.elapsed.total_seconds(), data['assert']['responseTime'])

class TestClassMeta(type):
    def __init__(self, *args, **kwargs):
        [[setattr(self, test_name, lambda self: abstract_test(self, data, requests.request(**data['request']))) for test_name, data in json.loads(open(suite_name, 'r').read()).items()] for suite_name in glob.iglob('*.json')]

class Tests(unittest.TestCase, metaclass=TestClassMeta): pass
unittest.main(testRunner=xmlrunner.XMLTestRunner())
