import itemdb

import os


def db_connect():
    """
    Performs database connection using database settings from settings.py
    """
    ytb_path = os.path.join(os.getcwd()+os.sep, "ytb.db")

    # dbname = "reddit_popular"
    # Open the database and make sure there is a table with appopriate indices
    ytb = itemdb.ItemDB(ytb_path)
    print('database started', 'ytb')
    return ytb


def create_table(db,tablename) -> None:
    """
    Creates database table
    """
#     tablename = setting['channelname']
#     db = ytb
    db.ensure_table(tablename, "!videoid", "status")


class Channel():
    """
    channel name
    cookie
    latest publish date
    prefer tag
    prefer des
    prefer title
    prefer thumbnail
    publish policy

    """


class Video():
    __tablename__ = 'product'
#     __table_args__ = (UniqueConstraint('quantity', 'url'),)

#     id = Column(Integer, primary_key=True)
#     platform = Column(String(), nullable=False)
