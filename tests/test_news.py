import unittest
from app.models import News_sources

class NewsSourcesTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Sources('bbc-news','BBC News','Use BBC News for all news','http://www.bbc.co.uk/news','general','gb','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'bbc-news')
        self.assertEquals(self.new_source.name,'BBC News')
        self.assertEquals(self.new_source.description,'Use BBC News for all news')
        self.assertEquals(self.new_source.url,'http://www.bbc.co.uk/news')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'gb')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        self.new_article = Articles('BBC','Maxwel 5','The current village world-Internet has turned the world','A general study about the positive impact of the internet towards learning and more other effect in the world')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'bbc-news')
        self.assertEquals(self.new_article.author,'Jennings Brown')
        self.assertEquals(self.new_article.title,'Man Claims He Invented Bitcoin, Is Ordered to Pay Billions in Bitcoin')
        self.assertEquals(self.new_article.description,'A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto, inventor of bitcoin, has been ordered to pay half of his cryptocurrency bounty to a man believed to be his former colleague. Read more...')
        self.assertEquals(self.new_article.url,'"https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816')
        self.assertEquals(self.new_article.image,'"https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png')
        self.assertEquals(self.new_article.date,'2019-08-28T16:50:00Z')
        self.assertEquals(self.new_article.content,'A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto, inventor of bitcoin, has been ordered to pay half of his cryptocurrency bounty to a man believed to be his former colleague.\r\nA U.S. district court ruled on Tuesday tha… [+2903 chars]'