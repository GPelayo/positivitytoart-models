from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Boolean, Column, Date, DateTime, Enum, ForeignKey, Integer, String, Table
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


class Hashtag(PositivityObject):
    __tablename__ = 'hashtag'

    hashtag_id = Column(String, primary_key=True)
    hashtag_text = Column(String)

    def __init__(self, hashtag_id, hashtag_text):
        super(Hashtag, self).__init__()
        self.hashtag_id = hashtag_id
        self.hashtag_text = hashtag_text


class ArtStyle(PositivityObject):
    __tablename__ = 'art_style'

    art_style_id = Column(String, primary_key=True)
    name = Column(String)
    hashtags = relationship('hashtags')

    def __init__(self, art_style_id, name):
        super(PositivityObject, self).__init__()
        self.name = name
        self.art_style_id = art_style_id


class SuggestedHashtag(PositivityObject):
    __tablename__ = 'suggested_hashtag'

    hashtag_id = Column(String, primary_key=True)
    article_id = Column(String, primary_key=True)

    def __init__(self, hashtag_id, article_id):
        super(SuggestedHashtag, self).__init__()
        self.hashtag_id = hashtag_id
        self.article_id = article_id

# image_post_artstyles = Table('image_post_art_style', Base.metadata, Column('art_style_id'), ForeignKey(art_syle.id))


class InstagramImagePost(PositivityObject):
    __tablename__ = 'instagram_image_post'

    image_post_id = Column(String, primary_key=True)
    caption = Column(String)
    image_location = Column(String)
    image_location_type = Column(String)
    #artyles add tables here