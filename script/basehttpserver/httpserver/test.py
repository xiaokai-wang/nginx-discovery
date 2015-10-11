import unittest
import httpServer

class TestDict(unittest.TestCase):
	def setUp(self):
	        print 'setUp...'

	def tearDown(self):
	        print 'tearDown...'

	def test_case1(self):
		httpServer.concurrency("0","127.0.0.1","10000","server200")	
