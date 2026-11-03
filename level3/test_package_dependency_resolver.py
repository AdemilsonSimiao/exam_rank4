import unittest
from py_package_dependency_resolver import package_dependency_resolver

class TestPackageDependencyResolver(unittest.TestCase):
    def test_package_resolver(self):
       self.assertEqual(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}), ["driver", "database", "app"])
       self.assertEqual(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}), ["A", "B", "C"])
       self.assertEqual(package_dependency_resolver({}), [])
       self.assertEqual(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}), [])
       self.assertEqual(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}), ["api", "web", "backend", "frontend"])
