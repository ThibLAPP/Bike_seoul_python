from django import forms
from .models import Bike
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class BikeForm(forms.ModelForm):

	class Meta:
		model = Bike
		fields = ('hour', 'temp', 'humidity', 'wind_speed', 'visibility', 
			'solar_rad', 'rainfall', 'snowfall', 'season',
			'holiday')
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'post'

		self.helper.layout = Layout(
			'hour',
			'temp',
			'humidity',
			'wind_speed',
			'visibility',
			'solar_rad',
			'rainfall',
			'snowfall',
			'season',
			'holiday',
			Submit('submit', 'Submit', css_class='btn-success')
		)

	


