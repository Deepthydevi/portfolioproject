from django.shortcuts import render, redirect
from .models import userprofile

# Create your views here.
def createprofile(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        DOB = request.POST.get('DOB')
        address = request.POST.get('address')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        graduation = request.POST.get('graduation')
        percentage= request.POST.get('percentage')
        university = request.POST.get('university')
        additionalcourses = request.POST.get('additionalcourses')
        skills = request.POST.get('skills')
        projecttitle = request.POST.get('projecttitle')
        projectdescription = request.POST.get('projectdescription')
        projectimg = request.FILES.get('projectimg')
        projectlink = request.POST.get('projectlink')
        companyname = request.POST.get('companyname')
        jobposition = request.POST.get('jobposition')
        aboutme = request.POST.get('aboutme')
        experience=request.POST.get('experience')
        user = userprofile(
            fullname=fullname,
            gender=gender,
            DOB=DOB,
            address=address,
            mobilenumber=mobilenumber,
            email=email,
            graduation=graduation,
            university=university,
            percentage=percentage,
            additionalcourses=additionalcourses,
            skills=skills,
            projecttitle=projecttitle,
            projectdescription=projectdescription,
            projectimg=projectimg,
            projectlink=projectlink,
            companyname=companyname,
            jobposition=jobposition,
            aboutme=aboutme,
            experience=experience
        )
        user.save()
    return render(request, 'create.html')

def listdetails(request):
    details = userprofile.objects.last()

    return render(request, 'resume.html', {'details': details})

def updatedetails(request, user_id):
    user = userprofile.objects.get(id=user_id)
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        DOB = request.POST.get('dob')
        address = request.POST.get('address')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        graduation = request.POST.get('graduation')
        percentage= request.POST.get('percentage')
        university = request.POST.get('university')
        additionalcourses = request.POST.get('additionalcourses')
        skills = request.POST.get('skills')
        projecttitle = request.POST.get('projecttitle')
        projectdescription = request.POST.get('projectdescription')
        projectimg = request.FILES.get('projectimg')
        projectlink = request.POST.get('projectlink')
        companyname = request.POST.get('companyname')
        jobposition = request.POST.get('jobposition')
        aboutme = request.POST.get('aboutme')
        experience=request.POST.get('experience')

        user.fullname=fullname
        user.gender=gender
        user.DOB=DOB
        user.address=address
        user.mobilenumber=mobilenumber
        user.email=email
        user.graduation=graduation
        user.university=university
        user.percentage=percentage
        user.additionalcourses=additionalcourses
        user.skills=skills
        user.projecttitle=projecttitle
        user.projectdescription=projectdescription
        user.projectimg=projectimg
        user.projectlink=projectlink
        user.companyname=companyname
        user.jobposition=jobposition
        user.aboutme=aboutme
        user.experience=experience
        user.save()
        return redirect('details')

    return render(request, 'update.html', {'user': user})


def deletedetails(request, user_id):
    user = userprofile.objects.get(id=user_id)
    user.delete()
    return render(request, 'delete.html', {'user': user})


