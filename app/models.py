class News_Sources:
    '''
    This class is meant to define sources objects
    '''

    def __init__(self,id,title,illustration,url,group,nation,language):
        self.id = id
        self.title = title
        self.illustration = illustration
        self.url = url
        self.group = group
        self.nation = nation
        self.language = language

class Articles:
    '''
    Defining articles in article class
    '''
    def __init__(self,id,narrator,title,illustration,url,image,date):
        self.id = id
        self.narrator = narrator
        self.title = title
        self.illustration = illustration
        self.url = url
        self.image = image
        self.date = date
