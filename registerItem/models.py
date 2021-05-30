from django.db import models
from account.models import User, Address

# Create your models here.
from stageproj3 import settings

AVAILABILITY = [
    ('Available', 'Available'),
    ('Given', 'Given'),

]


class Stock(models.Model):
    CATEGORY = [
        ('Computer Laptop', 'Computer Laptop & IPAD'),
        ('Computer Desktop', 'Computer Desktop'),
        ('4G Router', '4G Router & Moderm'),
        ('Printer', 'Printer'),
        ('Scanner', 'Scanner'),
        ('Television', 'Television, Projector & Screen'),
        ('Decoder', 'Decoder & stabilizer'),

    ]

    name = models.CharField(max_length=200, null=True, verbose_name='Assest Description')
    serialNumber = models.CharField(max_length=200, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    code = models.CharField(max_length=200, null=True, verbose_name='Tag Number')
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    availability = models.CharField(max_length=20, choices=AVAILABILITY, default='Available', verbose_name='Device Status')
    userRecord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.serialNumber


class Item(models.Model):
    STATUS = [
        ('Working', 'Working'),
        ('Not Working', 'Not Working'),
        ('Undermaintenance', 'Undermaintenance'),
        ('Retirement', 'Retirement'),

    ]

    device = models.OneToOneField(Stock, max_length=200, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='work')
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.device.name

