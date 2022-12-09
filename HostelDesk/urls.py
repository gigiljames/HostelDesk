from django.contrib import admin
from django.urls import path
from . import views

app_name="HostelDesk"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change_password/',views.change_password,name="change_password"),
    path('login/',views.login,name="login"),
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('admin_module/',views.admin_module,name="admin_module"),
    path('admin_module/ahm/',views.ahm,name="ahm"),
    path('admin_module/rhm/',views.rhm,name="rhm"),
    path('admin_module/amm/',views.amm,name="amm"),
    path('admin_module/rmm/',views.rmm,name="rmm"),
    path('admin_module/expel_student/',views.expel_student,name="expel_student"),
    path('admin_module/view_enroll_admin_rollno/',views.view_enroll_admin_rollno,name="view_enroll_admin_rollno"),
    path('student_module/',views.student_module,name="student_module"),
    path('student_module/application_h/',views.application_h,name="application_h"),
    path('student_module/application_m/',views.application_m,name="application_m"),
    path('student_module/student_profile/',views.student_profile,name="student_profile"),
    path('hostel_manager_module/',views.hostel_manager_module,name="hostel_manager_module"),
    path('hostel_manager_module/view_enroll_h_rno/',views.view_enroll_h_rno,name="view_enroll_h_rno"),
    path('hostel_manager_module/view_enroll_h_rollno/',views.view_enroll_h_rollno,name="view_enroll_h_rollno"),
    path('hostel_manager_module/vacate_student/',views.vacate_student,name="vacate_student"),
    path('mess_manager_module/',views.mess_manager_module,name="mess_manager_module"),
    path('mess_manager_module/view_enroll_m/',views.view_enroll_m,name="view_enroll_m"),
    # path('fuc/',views.fuc,name="fuc"),
    path('mm_get_students/',views.mm_get_students,name="mm_get_students")
    
    # path('dash/',views.dash,name="dash"),
]
