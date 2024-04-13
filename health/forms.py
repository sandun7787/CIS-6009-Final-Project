class DoctorForm(form.ModelForm):
    class Meta:
        model = Doctor
        exculde =('status','user','dob','dpj')