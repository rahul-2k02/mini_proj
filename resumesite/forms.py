from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row

genders=(('','Choose your gender'),
	('Male','Male'),
	('Female','Female')
	)
class ContactForm(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Name'}))
	birth=forms.DateField(label="Date of Birth",widget=forms.TextInput(attrs={'placeholder':'mm/dd/yyyy'}))
	gender=forms.ChoiceField(label='Gender',help_text='Select Gender',choices=genders)
	nationality=forms.CharField(label='Nationality',widget=forms.TextInput(attrs={'placeholder':'Enter your Nationality'}))
	about=forms.CharField(label="About Yourself",help_text='Tell about yourself',widget=forms.TextInput(attrs={'placeholder':'What would you like to say..'}))
	job=forms.CharField(label='Job Role',widget=forms.TextInput(attrs={'placeholder':'Enter your Job Position'}))
	email=forms.EmailField(label='E-Mail',widget=forms.TextInput(attrs={'placeholder':'Enter your Email'}))
	mobile=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Mobile Number'}))
	linked_in=forms.CharField(label='LinkedIn',help_text='Enter your LinkedIn Username',widget=forms.TextInput(attrs={'placeholder':'LinkedIn UserID'}))
	address=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your address'}))
	skills_1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 1'}))
	skills_2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 2'}))
	skills_3=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 3'}))
	skills_4=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 4'}))
	skills_5=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 5'}))
	skills_6=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Skill 6'}))

	education_10=forms.CharField(label='10th Grade Institution',widget=forms.TextInput(attrs={'placeholder':'Where Did You Study?'}))
	education_10_marks=forms.CharField(label='10th Marks',widget=forms.TextInput(attrs={'placeholder':'How much did you Score?'}))

	education_12=forms.CharField(label='12th Grade Institution',widget=forms.TextInput(attrs={'placeholder':'Where Did You Study?'}))
	education_12_marks=forms.CharField(label='12th Marks',widget=forms.TextInput(attrs={'placeholder':'How much did you Score?'}))

	education_ug=forms.CharField(label='UG Institution',widget=forms.TextInput(attrs={'placeholder':'Where did you get your degree?'}))
	education_ug_marks=forms.CharField(label='UG Marks',widget=forms.TextInput(attrs={'placeholder':'How much did you Score?'}))


	experience_1_title=forms.CharField(label='Internship 1 Experience',widget=forms.TextInput(attrs={'placeholder':'Tell us about your experience..'}))
	experience_1_dur=forms.CharField(label='Duration',widget=forms.TextInput(attrs={'placeholder':'How long was your work?'}))

	experience_2_title=forms.CharField(label='Internship 2 Experience',required=False,widget=forms.TextInput(attrs={'placeholder':'Tell us about your experience..'}))
	experience_2_dur=forms.CharField(label='Duration',required=False,widget=forms.TextInput(attrs={'placeholder':'How long was your work?'}))



	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		# self.helper.label_class = ''
		# self.helper.field_class = 'col-md-6 col-xs-9'
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-6  mb-10'),
                Column('job', css_class='form-group col-md-6  mb-10'),
                Column('email', css_class='form-group col-md-6 mb-10'),
                Column('linked_in', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('about', css_class='form-group col-md-12  mb-10'),
                css_class='form-row  center'
			),			
			Row(
                Column('mobile', css_class='form-group col-md-6  mb-10'),
                Column('address', css_class='form-group col-md-6 mb-10'),
                Column('birth', css_class='form-group col-md-6 mb-10'),
                Column('gender', css_class='form-group col-md-6 mb-10'),
                Column('nationality', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_1', css_class='form-group col-md-2  mb-10'),
                Column('skills_2', css_class='form-group col-md-2 mb-10'),
                Column('skills_3', css_class='form-group col-md-2 mb-10'),
                Column('skills_4', css_class='form-group col-md-2 mb-10'),
                Column('skills_5', css_class='form-group col-md-2 mb-10'),
                Column('skills_6', css_class='form-group col-md-2 mb-10'),


                css_class='form-row  center'
			),

			Row(
                Column('education_10', css_class='form-group col-md-6 mb-10'),
                Column('education_10_marks', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('education_12', css_class='form-group col-md-6 mb-10'),
                Column('education_12_marks', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),

			Row(
                Column('education_ug', css_class='form-group col-md-6 mb-10'),
                Column('education_ug_marks', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),

			Row(
                Column('experience_1_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('experience_2_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),

			Submit('submit','Submit',css_class="btn-success",)
			)