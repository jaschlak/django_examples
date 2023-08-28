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