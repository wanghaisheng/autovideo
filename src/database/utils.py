import logging
import secrets
from datetime import datetime, timedelta
from typing import Optional

from cachetools import TTLCache, cached
# from src.database.models import Price, Product, db_connect
from src.settings import CACHE_MAXSIZE, CACHE_TTL, LAST_N_DAY_DATA
from src.utils.constants import POPULAR_BEER_BRANDS, POPULAR_BEER_STYLES, POPULAR_BEERS, RESULTS_NOT_FOUND_GIFS

logger = logging.getLogger(__name__)

# engine = db_connect()
# session = sessionmaker(bind=engine)()

ONE_YEAR_IN_DAYS = 365


# @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL))
# def get_product_price_history(product_id: int) -> Optional[query.Query]:
#     logger.info(f'Getting price history for product_id: "{product_id}".')

#     try:
#         return session.query(Price) \
#             .filter(Price.product_id == product_id) \
#             .order_by(Price.updated_on) \
#             .limit(ONE_YEAR_IN_DAYS)

#     except ProgrammingError as exception:
#         logger.exception(exception)
#         raise

#     finally:
#         session.close()


# @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL))
# def get_product_based_on_query(search_string: str) -> Optional[list[Product]]:
#     """
#     Primary search API for Burplist
#     """
#     logger.info(f'Searching database with user query: "{search_string}".')

#     try:
#         return session.query(Product).filter(
#             or_(
#                 func.similarity(Product.platform, search_string) > 0.6,
#                 func.similarity(Product.style, search_string) > 0.5,
#                 func.similarity(Product.brand, search_string) > 0.4,
#                 func.similarity(Product.name, search_string) > 0.2,
#             ),
#             and_(Product.updated_on >= datetime.utcnow() - timedelta(days=LAST_N_DAY_DATA)),
#         ).order_by(Product.price_per_quantity).limit(50).all()

#     except ProgrammingError as exception:
#         logger.exception(exception)
#         raise

#     finally:
#         session.close()


# def get_random_beer_style() -> str:
#     return secrets.choice(POPULAR_BEER_STYLES)


# def get_random_beer_brand() -> str:
#     return secrets.choice(POPULAR_BEER_BRANDS)


# def get_random_beer() -> str:
#     return secrets.choice(POPULAR_BEERS)


# def get_random_results_not_found_gif() -> str:
#     gif = secrets.choice(RESULTS_NOT_FOUND_GIFS)
#     return f"""
#         <p align="center">
#             <img alt="No Results Found GIF" class="img" width="50%" height="50%" src="{gif}">
#         </p>
#     """


def add_video_thumb_pair_basic(thumbpath,videopath,filename,start_index):

    tablename = setting['channelname']
    db = ytb
    db.ensure_table(tablename, "!videoid", "status")
            
              

    # filename = os.path.splitext(f)[0]

    if os.path.exists(thumbpath):
        video = db.count(
            tablename, "videoid ==?", b64e(filename))
        print('check video stauts', video)
        if video == 1:
            status = db.select_one(tablename, "videoid ==?",
                                    b64e(filename))["status"]

            if status == 1:
                print('task completed', status, video)
            else:

                print('task added but not uploaded')

        elif video == 0:
            print('task not added before')
            tags = setting['prefertags']
            des = setting['preferdes']
            filename=filename.split(os.sep)[-1]
            title = isfilenamevalid(filename)
            if len(filename) > 100:
                title = filename[:90]
            nowtime = time.time()
            update_time = int(nowtime)
            videoid = b64e(filename)
            olddata = {}
            olddata["videoid"] = videoid
            #Oct 19, 2021
            today = date.today()
            publish_date =datetime(today.year, today.month, today.day, 20, 15), 

            if start_index <int(setting['dailycount']):
                release_offset='0-1'
            else:
                release_offset=str(int(start_index)/30)+'-'+str(int(start_index)/int(setting['dailycount']))
            

            olddata["publish_date"] = release_offset
            olddata["thumbpath"] = thumbpath
            olddata["update_time"] = update_time
            olddata["title"] = title
            olddata["des"] = des
            olddata["videopath"] = videopath
            olddata["tags"] = tags
            olddata["status"] = 0
            db.put(tablename, olddata)
            print('add 1 new videos for upload', filename)
    else:
        pass

def getvideos4uploadByChannel(channelname):

    tablename = setting['channelname']
    db = ytb
    db.ensure_table(tablename, "!videoid", "status")

    print('starting upload process')
    with ytb:
        donevideos = db.select(tablename, "status ==?", 1)
        print('already upload videos:', len(donevideos))

        videos = db.select(tablename, "status ==?", 0)
        print('awaiting upload videos:', len(videos))