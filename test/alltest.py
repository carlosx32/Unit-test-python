import unittest
from unittest import suite
from unittest import runner
from unittest import result

import componente1test
import componente2test


if __name__=='__main__':
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTest(loader.loadTestsFromModule(componente1test))
    suite.addTest(loader.loadTestsFromModule(componente2test))
    runner=unittest.TextTestRunner(verbosity=2)
    result=runner.run(suite)