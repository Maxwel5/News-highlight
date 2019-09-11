class News_Sources:
    '''
    This class is meant to define sources objects
    '''

    def __init__(self,id,title,description,url):
        self.id = id
        self.title = title
        self.description = description
        self.url = url

class Articles:
    '''
    Defining articles in article class
    '''
    def __init__(self,id,author,title,description,url,image,date,content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
        self.content = content
