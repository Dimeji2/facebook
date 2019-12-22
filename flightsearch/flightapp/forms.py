from django import forms
class flight_details(forms.Form):
	Departure_City=forms.CharField(max_length=3,label='Departure City')
	Destination_City=forms.CharField(max_length=3,label='Destination City')
	Departure_Date=forms.DateField(label='Departure Date',widget=forms.SelectDateWidget())
	Return_Date=forms.DateField(label='Return Date',widget=forms.SelectDateWidget())
	Cabin_Class=forms.CharField(label='Cabin class')
	No_of_Adults=forms.IntegerField(label='No of Adults(>12 years old)')
	No_of_Children=forms.IntegerField(label='No of Children(2-12 years old)')
	No_of_Infants=forms.IntegerField(label='No of Infants(0-2 years old)')