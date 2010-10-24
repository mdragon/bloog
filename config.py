import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# If we're debugging, turn the cache off, etc.
# Set to true if we want to have our webapp print stack traces, etc
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
logging.info("Starting application in DEBUG mode: %s", DEBUG)

# Don't change default_blog or default_page to prevent conflicts when merging #  Bloog source code updates.
# Do change blog or page dictionaries at the bottom of this config module.

BLOG = {
    "bloog_version": "0.8",
    "html_type": "text/html",
    "charset": "utf-8",
    "title": "I don't want to get off on a rant here, but....",
    "author": "Matt Dragon",
    # This must be the email address of a registered administrator for the 
    # application due to mail api restrictions.
    "email": "mdragon@gmail.com",
    "description": "Technology, Programming, Complaints, etc.",
    "root_url": "http://blog.web20studios.com",
    "master_atom_url": "/feeds/atom.xml",
    # By default, visitors can comment on article for this many days.
    # This can be overridden by setting article.allow_comments
    "days_can_comment": 60,
    # You can override this default for each page through a handler's call to 
    #  view.ViewPage(cache_time=...)
    "cache_time": 0 if DEBUG else 3600,
	"js_debug": "true" if DEBUG else "false",

    # Use the default YUI-based theme.
    # If another string is used besides 'default', calls to static files and
    #  use of template files in /views will go to directory by that name.
    "theme": ["default"],
    
    # Display gravatars alongside user comments?
    "use_gravatars": True,
    
    # Do you want to be emailed when new comments are posted?
    "send_comment_notification": True,

    # If you want to use legacy ID mapping for your former blog platform,
    # define it here and insert the necessary mapping code in the
    # legacy_id_mapping() function in ArticleHandler (blog.py).
    # Currently only "Drupal" is supported.
    "legacy_blog_software": None,
    #"legacy_blog_software": "Drupal",
    #"legacy_blog_software": "Serendipity",
    
    # If you want imported legacy entries _not_ mapped in the file above to
    # redirect to their new permanent URL rather than responding on their
    # old URL, set this flag to True.
    "legacy_entry_redirect": False,
}

PAGE = {
    "title": BLOG["title"],
    "articles_per_page": 20,
    "navlinks": [
        #{ "title": "Articles", "description": "Bits of Info", 
         # "url": "/articles"} ,
        #{ "title": "Contact", "description": "Send me a note", 
          #"url": "/contact"},
    ],
    "featuredMyPages": {
        "title": "The Author",
        "description": "Ben is a 22 year-old software engineer and geek living in the San Francisco Bay Area.  He splits his time between work, hobby programming, video games, and the interwebs.",
        "entries": [
            { "title": "Git Hub", 
              "url": "http://github.com/bcherry", 
              "description": "My Hobby Code" },
            { "title": "Facebook", 
              "url": "http://www.facebook.com/bcherry", 
              "description": "That Social Thing" },
            { "title": "Twitter", 
              "url": "http://twitter.com/bcherry", 
              "description": "Rambling Tweets" },
            { "title": "LinkedIn", 
              "url": "http://www.linkedin.com/in/bcherryprogrammer", 
              "description": "Serious Professional Stuff" },
            { "title": "Google Profile", 
              "url": "http://www.google.com/profiles/bcherry", 
              "description": "Google Owns My Soul" },
        ]
    },
    #"featuredOthersPages": {
    #    "title": "Google App Engine",
    #    "description": "Developer Resources",
    #    "entries": [
    #        { "title": "Google App Engine", 
    #          "url": "http://code.google.com/appengine/", 
    #          "description": "The mothership" },
    #    ]
    #},
}
