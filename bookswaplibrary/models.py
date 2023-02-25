import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Member(models.Model):

    member = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    
    
class MemberCatalog(models.Model):

    catalogue_type = models.CharField(max_length=99)
    member = models.ForeignKey('Address', on_delete=models.CASCADE)
    booklist = models.ManyToManyField('BookInstance')


class Address(models.Model):
    
    LOCATIONS = (
        ('h', 'Home'),
        ('b', 'Business'),
        ('ps', 'Public Space'),
    )
    
    location_type = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        blank=True,
        default='e',
        help_text='Location Type',
    ) 
    street_no = models.CharField(max_length=9)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postcode = models.CharField(max_length=9)
    country = models.CharField(max_length=200)

class Book(models.Model):

    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
class BookInstance(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    
    CONDITION = (
        ('e', 'Excellent'),
        ('g', 'Good'),
        ('f', 'Fair'),
        ('m', 'Missing Pages'),
    )
    
    condition = models.CharField(
        max_length=1,
        choices=CONDITION,
        blank=True,
        default='e',
        help_text='Book condition',
    )
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    
class Exchange(models.Model):

    date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="owner")
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrower")
    books = models.ManyToManyField('BookInstance')
    exchange_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_exchanged = models.DateField(null=True, blank=True)
    
    RETURN_REQUIREMENTS = (
        ('r', 'Return'),
        ('n', 'Return Not Required'),
        ('e', 'Exchanged'),
        ('s', 'Sold'),
    )

    status = models.CharField(
        max_length=1,
        choices=RETURN_REQUIREMENTS,
        blank=True,
        default='r',
        help_text='Return Requirements',
    )
    