#Function Based


from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from students.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'id_number', 'course_and_year', 'gender']

def student_list(request, template_name='students/student_list.html'):
    students = Student.objects.all()
    data = {}
    data['object_list'] = students
    return render(request, template_name, data)

def student_create(request, template_name='students/student_form.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_update(request, pk, template_name='students/student_form.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_delete(request, pk, template_name='students/student_confirm_delete.html'):
    student = get_object_or_404(Student, pk=pk)    
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    return render(request, template_name, {'object':student})
