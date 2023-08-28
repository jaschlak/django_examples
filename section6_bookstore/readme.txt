# Migrations

    When your Model changes you likely will need to update your database schema (structure). However, you don't want everything to break when you make a change. 
    To handle this relationship after making a model change you will need to migrate your model to change schema of the database
    
    ## Migration Commands
    
        # add current model configuration (shows in migrations folder of app)
        python manage.py makemigrations
        
        # migrate migrations that have not been migrated yet
        python manage.py migrate
        
        # Test insert/select data in db using interactive shell
            python manage.py shell
            from book_outlet.models import Book
            harry_potter = Book(title="Harry Potter 1 - The Philosopher's Stone", rating=5)         # creates an object in python, didn't push
            harry_potter.save()                                                                     # saves to db
            Book.objects.all()                                                                      # get all books from db in a python object
            Book.objects.all()[0].title
        
        # udpate data in db
            python manage.py shell
            harry_potter = Book.objects.all()[0]                                                    # give row a variable name    
            harry_potter.is_bestselling = True                                                      # edit row by row variable name
            harry_potter.save()                                                                     # update row in db (or save if didn't exists)
            
        # delete data in db
            harry_potter = Book.objects.all()[2]                                                    # set variable as 3rd row
            harry_potter.delete()
            
        # insert without python variable instance
        
            Book.objects.create(title="My Story",rating=2,author="Joey",is_bestselling=False)
            
        # get table/model values
        
            Book.objects.get(id=3)                                                                  # note: always returns one value or errors
            Book.objects.get(title="My Story")                                                      # note: always returns one value or errors
            Book.objects.filter(is_bestselling=True)
            Book.objects.filter(rating.lte=3)                                                       # filter using field lookups
            
        # get with or condition
        
            python manage.py shell
            from django.db.models import Q
            Book.objects.filter(Q(rating.lte=3 |) | Q(is_bestselling=True))
            