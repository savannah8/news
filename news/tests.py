from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
#set up method 
    def setUp(self):
        self.willen= Editor(first_name= 'Willen',last_name='Gitonga', email='willengitonga@gmail.com')

#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.willen,Editor))
    
#Testing the Save Method 
    def test_save_method(self):
        self.willen.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    



class ArticleTestClass(TestCase):
    def setUp(self):
          self.willen= Editor(first_name= 'Willen',last_name='Gitonga', email='willengitonga@gmail.com')
          self.willen.save_editor()

#creating a new tag and saving it 
          self.new_tag = tags(name ='testing')
          self.new_tag.save()

#creating a new article and save it
          self.new_article=Article(title='Test Article',post='This is a test post',editor=self.willen,tags=self.new_tag)
          self.new_article.save()


#deleting model instances 
    def tearDown(self):
          Editor.objects.all().delete()
          tags.objects.all().delete()
          Article.objects.all().delete()
    
#fucntion to get todays news 
    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date = '2018-03-17'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)



