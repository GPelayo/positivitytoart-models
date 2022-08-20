from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()

AnalyzedStatus = Enum('OK', 'ERROR', name='scraping_status')


class PositivityObject(Base, SerializerMixin):
    __abstract__ = True


class RedditArticlePost(PositivityObject):
    __tablename__ = 'reddit_article_post'

    article_id = Column(String, primary_key=True)
    url = Column(String)
    title = Column(String)
    date_posted = Column(Date)
    score = Column(Integer)
    is_read = Column(Boolean)

    def __init__(self, article_id, title, url):
        super(RedditArticlePost, self).__init__()
        self.article_id = article_id
        self.title = title
        self.url = url


class ArticleAnalysis(PositivityObject):
    __tablename__ = 'article_analysis'

    article_id = Column(String, primary_key=True)
    url = Column(String)
    headline = Column(String)
    date_written = Column(Date)
    description = Column(String)
    main_text = Column(String)
    analysis_status = Column(AnalyzedStatus)
    analysis_comments = Column(String)
    suggested_prompts = relationship('SuggestedPrompt')
    suggested_hashtags = relationship('SuggestedHashtag')

    def __init__(self, article_id, title, url):
        super(ArticleAnalysis, self).__init__()
        self.article_id = article_id
        self.headline = title
        self.url = url


class SuggestedPrompt(PositivityObject):
    __tablename__ = 'suggested_prompt'

    prompt_id = Column(String, primary_key=True)
    prompt_text = Column(String)
    article_id = Column(String, ForeignKey('article_analysis.article_id'))

    def __init__(self, prompt_id, prompt_text, article_post_id):
        super(SuggestedPrompt, self).__init__()
        self.prompt_id = prompt_id
        self.prompt_text = prompt_text
        self.article_post_id = article_post_id


class Hashtag(PositivityObject):
    __tablename__ = 'hashtag'

    hashtag_id = Column(String, primary_key=True)
    hashtag_text = Column(String)

    def __init__(self, hashtag_id, hashtag_text):
        super(Hashtag, self).__init__()
        self.hashtag_id = hashtag_id
        self.hashtag_text = hashtag_text


class SuggestedHashtag(PositivityObject):
    __tablename__ = 'suggested_hashtag'

    hashtag_id = Column(String, primary_key=True)
    article_id = Column(String, primary_key=True)

    def __init__(self, hashtag_id, article_id):
        super(SuggestedHashtag, self).__init__()
        self.hashtag_id = hashtag_id
        self.article_id = article_id


class InstagramImagePost(PositivityObject):
    __tablename__ = 'instagram_image_post'

    image_post_id = Column(String, primary_key=True)
    caption = Column(String)
    image_location = Column(String)
    image_location_type = Column(String)
