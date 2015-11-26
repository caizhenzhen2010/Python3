import unittest,my_math

class ProductTest(unittest.TestCase):
    
    def testIntergers(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                p=my_math.product(x, y)
                self.failUnless(p==x*y,'Interger multiplication failed!')
    def testFloater(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                x/=10.0
                y/=10.0
                p=my_math.product(x, y)
                self.failUnless(p==x*y,'Flaot multiplication failed!')
                
if __name__=='__main__':
    unittest.main()               