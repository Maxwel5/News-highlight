import unittest
from app.models import News_sources,Articles

class NewsSourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('BBC','BBC News','British Broadcasting news','bbc.com','general','Britain','english')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'BBC')
        self.assertEquals(self.new_source.title,'BBC News')
        self.assertEquals(self.new_source.illustration,'British Broadcasting news')
        self.assertEquals(self.new_source.url,'bbc.com')
        self.assertEquals(self.new_source.group,'general')
        self.assertEquals(self.new_source.nation,'Britain')
        self.assertEquals(self.new_source.language,'english')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News_sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('BBC','Maxwel 5','The current village world-Internet has turned the world','A general study about the positive impact of the internet towards learning and more other effect in the world')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'BBC')
        self.assertEquals(self.new_article.narrator,'Maxwel 5')
        self.assertEquals(self.new_article.title,'The current village world-Internet has turned the world')
        self.assertEquals(self.new_article.illustration,'A general study about the positive impact of the internet towards learning and more other effect in the world')
        self.assertEquals(self.new_article.url,'bbc.com')
        self.assertEquals(self.new_article.image,'http://newsimg.bbc.co.uk/media/images/39665000/jpg/_39665271_office_203.jpg')
        self.assertEquals(self.new_article.date,'Tuesday, 6 January, 2004, 12:37 GMT')