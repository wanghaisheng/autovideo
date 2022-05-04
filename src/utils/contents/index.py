from src.settings import CONTACT_EMAIL

# This page contains all the html contents corresponding to `src/index.py`

# Header
# ^^^^^^
HEADER = """
$('#favicon32,#favicon16').remove();
$('head').append('<link rel="icon" type="image/x-icon" href="/static/favicon/burplist.png">')
"""

# Footer
# ^^^^^^
FOOTER = f"""
$('FOOTER').html('✉️ <a href="mailto:tiktokadownloader@gmail.com" target="_blank">Contact</a> | 💡 <a href="/feedback">Feedback</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
"""


LOAD_CSS = r"""
<style>
.img {
    width: auto;
    height: auto;
    max-width: 400;
    max-height: 300px;
    border:2px solid #fff;
    -moz-box-shadow: 10px 10px 5px #ccc;
    -webkit-box-shadow: 10px 10px 5px #ccc;
    box-shadow: 10px 10px 5px #ccc;
    -moz-border-radius:25px;
    -webkit-border-radius:25px;
    border-radius:25px;
}
</style>
"""

LANDING_PAGE_HEADING = r"""
<h1 align="center"><strong>Autovideopublish</strong></h1>
"""

PRODUCT_HUNT_FEATURED_BANNER = r"""
<div align="center"><a href="https://www.producthunt.com/posts/burplist?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-burplist" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=304966&theme=light" alt="Burplist - Free price comparison tool for craft beers | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a></div>
"""

LANDING_PAGE_SUBHEADING = r"""
<h3 align="center">Search Engine for Craft Beers 🍻 in Singapore</h1>
<p align="center">
    <img alt="Cheers" class="img" width="50%" height="50%" src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
"""

LANDING_PAGE_DESCRIPTION_English = r"""
# What is Autovideopublish?

This project aims to automate the upload process for YouTube/Tiktok Videos. Since videos can only be publicly uploaded 
through the YouTube Data API by using a Google Workspaces Account (not free!), 
This approach also bypasses API restrictions (e.g. Rate Limits/Endcards can't be set through the API).
There are tons of tools existing but not for me .

🔎 A free **video publish tool** for influencers.
get hundreds of prepared Youtube and tiktok videos published automatically
📊 **Handsoff** to type title,description,set tags and schedule time to public
❤️ Saving  **10X** time than manually upload through youtube upload portal.
💯 proxy support auto detect whether need a proxy
💯 cookie and profile support for those multiple channels under same google account
💯 schedule time publish.you can explictly specify a date and time for each video or you can set publish policy and daily public count,for example,daily count is 4,you got 5 videos,then first 4 will be published 1 day after the upload date ,the other 1 will be 2 days after the upload date

## How to use?

📚  install requirements 
📚  load default setting, modify as you like setup channel upload setting
📚  check network and setup proxy
📚  

## Is this free?

🥳 Short answer: Yes.
🙌 Long answer: _Yessssssssssss_.
"""


LANDING_PAGE_DESCRIPTION_Chinese = r"""
# What is Autovideopublish?

This project aims to automate the upload process for YouTube/Tiktok Videos. Since videos can only be publicly uploaded 
through the YouTube Data API by using a Google Workspaces Account (not free!), 
This approach also bypasses API restrictions (e.g. Rate Limits/Endcards can't be set through the API).
There are tons of tools existing but not for me .

🔎 一款up主发布youtube视频的小工具.
🔎 A free **video publish tool** for influencers.
get hundreds of prepared Youtube and tiktok videos published automatically
📊 **Handsoff** to type title,description,set tags and schedule time to public
❤️ Saving  **10X** time than manually upload through youtube upload portal.
💯 proxy support auto detect whether need a proxy
💯 cookie and profile support for those multiple channels under same google account
💯 schedule time publish.you can explictly specify a date and time for each video or you can set publish policy and daily public count,for example,daily count is 4,you got 5 videos,then first 4 will be published 1 day after the upload date ,the other 1 will be 2 days after the upload date

## How to use?

📚  install requirements 
📚  load default setting, modify as you like setup channel upload setting
📚  check network and setup proxy
📚  

## Is this free?

🥳 Short answer: Yes.
🙌 Long answer: _Yessssssssssss_.
"""
