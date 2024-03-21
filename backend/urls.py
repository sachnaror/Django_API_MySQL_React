from django.contrib import admin
from django.urls import include, path
from employee_app import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('employees', views.EmployeeAPI)
router.register('departments', views.DepartmentsAPI)
router.register('deptemp', views.DeptEmpAPI)
router.register('deptmanager', views.DeptManagerAPI)
router.register('salaries', views.SalariesAPI)
router.register('titles', views.TitlesAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
