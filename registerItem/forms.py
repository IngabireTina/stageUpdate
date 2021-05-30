from django.forms import ModelForm
from .models import Item
from .models import Stock
from .models import User


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'serialNumber', 'code', 'category', 'availability']
        # fields = '__all__'


class SectorStockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SectorStockForm, self).__init__(*args, **kwargs)
        self.fields['userRecord'].queryset = User.objects.filter(username=self.request.user.username)
        self.fields['userRecord'].empty_label = None


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Stock.objects.exclude(availability='Given')
        self.fields['device'].widget.attrs['readonly'] = True


# ========================== SECTOR IT MANAGER DEVICE ASSIGN FORM =====================

class SectorItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SectorItemForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Stock.objects.exclude(availability='Given')
        self.fields['device'].widget.attrs['readonly'] = True
        # self.fields['address'].queryset = Item.objects.filter(address__name=self.request.user.address)
        # self.fields['address'].empty_label = None


class UpdateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     # self.request = kwargs.pop('request')
    #     # super(UpdateItemForm, self).__init__(*args, **kwargs)
    #     # self.fields['device'].queryset = Stock.objects.exclude(availability='Given')
    #     self.fields['device'].widget.attrs['readonly'] = True


class ReportItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['device', 'address']
        # fields = ['address', 'person', 'description', 'title', 'device']

    def __init__(self, *args, **kwargs):
        super(ReportItemForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['person'].widget.attrs['readonly'] = True
            # self.fields['device'].widget.attrs['readonly'] = True
            self.fields['title'].widget.attrs['readonly'] = True
            # self.fields['address'].widget.attrs['readonly'] = True


    def clean_device(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.device
        else:
            return self.cleaned_data.get('device', None)

