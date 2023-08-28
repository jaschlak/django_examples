
# Setup

    # create site "my_site"
    django-admin startproject my_site
    
    # create app "blog"
    python manage.py startapp blog
    
    # run server
    python manage.py runserver
    
## Routes

    /                       Loads starting page (latest blog)
    /posts                  Load page with all blog posts
    /post/my-first-post     Load first blog post
    /post/<slug>            Load specific blog post