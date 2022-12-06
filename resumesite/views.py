from django.shortcuts import render
from .forms import ContactForm
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

# from xhtml2pdf import pisa

def home(request):
	return render(request, 'home.html', {})

def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			job=form.cleaned_data['job']
			about=form.cleaned_data['about']
			birth=form.cleaned_data['birth']
			gender=form.cleaned_data['gender']
			email=form.cleaned_data['email']
			linked_in=form.cleaned_data['linked_in']
			nationality=form.cleaned_data['nationality']

			skills_1=form.cleaned_data['skills_1']
			skills_2=form.cleaned_data['skills_2']
			skills_3=form.cleaned_data['skills_3']
			skills_4=form.cleaned_data['skills_4']
			skills_5=form.cleaned_data['skills_5']
			skills_6=form.cleaned_data['skills_6']


			mobile=form.cleaned_data['mobile']
			address=form.cleaned_data['address']

			education_10=form.cleaned_data['education_10']
			education_10_marks=form.cleaned_data['education_10_marks']

			education_12=form.cleaned_data['education_12']
			education_12_marks=form.cleaned_data['education_12_marks']

			education_ug=form.cleaned_data['education_ug']
			education_ug_marks=form.cleaned_data['education_ug_marks']

			experience_1_title=form.cleaned_data['experience_1_title']
			experience_1_dur=form.cleaned_data['experience_1_dur']

			experience_2_title=form.cleaned_data['experience_2_title']
			experience_2_dur=form.cleaned_data['experience_2_dur']

			data={'name':name}
			data['job']=job
			data['about']=about
			data['gender']=gender
			data['birth']=birth
			data['email']=email
			data['nationality']=nationality
			data['linked_in']=linked_in
			data['skills_1']=skills_1
			data['skills_2']=skills_2
			data['skills_3']=skills_3
			data['skills_4']=skills_4
			data['skills_5']=skills_5
			data['skills_6']=skills_6

			data['mobile']=mobile
			data['address']=address

			data['education_10']=education_10
			data['education_10_marks']=education_10_marks

			data['education_12']=education_12
			data['education_12_marks']=education_12_marks

			data['education_ug']=education_ug
			data['education_ug_marks']=education_ug_marks

			data['experience_1_title']=experience_1_title
			data['experience_1_dur']=experience_1_dur

			data['experience_2_title']=experience_2_title
			data['experience_2_dur']=experience_2_dur

			return render(request,'home.html',data)
	return render(request,'info.html',{'form':form})

# def viewPDF(request):
# 		return render(request,'home.html',data)




# def resume(request):
# 	template=loader.get_template('info.html')
# 	html=template.render()
# 	option={
# 		'page-size'=='Letter',
# 		'encoding'=='UTF-8'
# 	}
# 	pdf=pdfkit.from_string(html,False,option)
# 	response = HttpResponse(pdf,content_type='application/pdf')
# 	response['Content-Disposition']='attachments'
# 	return response