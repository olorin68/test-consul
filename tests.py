import testConstructor
import unittest

keys= ["A-GOT", "B-GOT"]
codesAndTexts = {
  "pos": {
    "code": 200,
    "texts": "get your text"
  },
  "neg": {
    "code": 400,
    "texts": "Some problem with your text, please fill it by string"
  },
  "error": {
    "code": 500,
    "texts": "something went wrong"
  },
  "infra": {
    "code": 504,
    "texts": "something went wrong"
  }
}
texts= ["test text", "text with 111", "абававра"]

class TestUM(unittest.TestCase):
    def setUp(self):
        testConstructor.clear_consul(keys)

    def tearDown(self):
        pass

    def test_pos(self):
        self.assertEqual(testConstructor.posTest(),
                         {'respCode': codesAndTexts['pos']['code'], 'respText': codesAndTexts['pos']['texts'], 'ConsulKeyVal': [{'A-GOT': 'test'}, {'B-GOT': 'get your text with 200 status code'}]})

    def test_pos_0(self):
        self.assertEqual(testConstructor.posTest(text=texts[0]),
                         {'respCode': codesAndTexts['pos']['code'], 'respText': codesAndTexts['pos']['texts'], 'ConsulKeyVal': [{'A-GOT': texts[0]}, {'B-GOT': 'get your text with 200 status code'}]})

    def test_pos_1(self):
        self.assertEqual(testConstructor.posTest(text=texts[1]),
                         {'respCode': codesAndTexts['pos']['code'], 'respText': codesAndTexts['pos']['texts'], 'ConsulKeyVal': [{'A-GOT': texts[1]}, {'B-GOT': 'get your text with 200 status code'}]})

    def test_pos_2(self):
        self.assertEqual(testConstructor.posTest(text=texts[2]),
                         {'respCode': codesAndTexts['pos']['code'], 'respText': codesAndTexts['pos']['texts'], 'ConsulKeyVal': [{'A-GOT': texts[2]}, {'B-GOT': 'get your text with 200 status code'}]})


    def test_neg(self):
        self.assertEqual(testConstructor.negTest(),
                         {'respCode': codesAndTexts['neg']['code'], 'respText': codesAndTexts['neg']['texts']})

    def test_neg_float(self):
        self.assertEqual(testConstructor.negTest(text=34343.33),
                         {'respCode': codesAndTexts['neg']['code'], 'respText': codesAndTexts['neg']['texts']})

    def test_neg_neg(self):
        self.assertEqual(testConstructor.negTest(text=-34343.33),
                         {'respCode': codesAndTexts['neg']['code'], 'respText': codesAndTexts['neg']['texts']})

    def test_error(self):
        self.assertEqual(testConstructor.errorTest(),
                         {'respCode': codesAndTexts['error']['code'], 'respText': codesAndTexts['error']['texts']})


if __name__ == '__main__':
    unittest.main()
