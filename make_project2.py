import os 


def make_a_venv_model_and_setup_all_libs_with_django(venv_x):
    pkg_install=["pipenv==2024.0.1",
     "django==5.0.6",
"django-widget-tweaks==1.5.0",
"django-jazzmin==3.0.0",
"requests==2.31.0",
"beautifulsoup4==4.12.2",
"lxml==4.9.3",
"html5==0.0.9",
"Pillow==10.1.0",
"mysql-connector-python==8.1.0",
"mysql-connector-repackaged==0.3.1",
"djangorestframework==3.15.2","Markdown==3.6","django-filter==24.2",
"django-createsuperuserwithpassword==2.0.0",
"django-rosetta==0.10.0",
"whitenoise==6.6.0","django-cors-headers==4.4.0",
"django-phonenumber-field==7.3.0",
"django-parler==2.3","django-countries==7.5.1","django-import-export==4.1.1","django-countries==7.6.1","stripe==10.3.0"



    ]
   
    if os.path.exists(venv_x):
        print(venv_x+" found")
    else:
        print(venv_x+" NOT Found.....Creating")
        os.system("python -m venv "+venv_x)

    os.chdir(venv_x+"/Scripts")
    os.system("activate")
    print(venv_x+" ACTIVATED")
    for lib in range(len(pkg_install)):
        print("\nINSTALLING "+pkg_install[lib]+"\n")
        os.system("pip3 install "+pkg_install[lib])
        print("\n"+pkg_install[lib]+ " INSTALLED\n")
    


def default_settings():
   print("\n\nwriting settings module PART ONE\n\n")
   return "from pathlib import Path".replace("from pathlib import Path","""from pathlib import Path\nimport os""")+"'django.contrib.staticfiles',".replace("'django.contrib.staticfiles',","\n#'django.contrib.staticfiles','APP_NAME','widget_tweaks','stripe','phonenumber_field','import_export','django_countries','rest_framework','corsheaders' ")

def default_settings_1():
   print("\n\nwriting settings module MART TOW\n\n")
   return "STATIC_URL = 'static/'".replace("STATIC_URL = 'static/'","""+"""
                                           
                                           '''
   #ADDED INTO MIDDELWARE LIST:
   \n\n
   #"corsheaders.middleware.CorsMiddleware",
    #"django.middleware.common.CommonMiddleware",

#ADDED settings:

\n\n
#CORS_ALLOWED_ORIGINS=['','localhost:3000']

#CORS_ALLOWED_ORIGIN_REGEXES=Truw

#CORS_ALLOW_ALL_ORIGINS=True

#CORS_ALLOW_METHODS = (   "DELETE","GET","OPTIONS","PATCH","POST","PUT",)



'''
                                           
                                           
                                           """

STATIC_URL = 'static/'

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
print(f"the static path{str(STATICFILES_DIRS)}")

#STATIC_ROOT=BASE_DIR / 'static'
#print(f"the static path{str(STATIC_ROOT)}")


MEDIA_URL='/alt_stat/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static\\alt_stat')
print(f"the Media root path{str(MEDIA_ROOT)}")
""")





def make_a_write_action(proj_name):
   print(f"\n\nyour current path from make_a_write_action function\n\n")
   print(str(os.system("dir")))
   os.chdir(proj_name)
   print("\nadjusting the settings file\n")
   write_now=open("settings.py",'+a')
   write_now.write(default_settings())
   write_now.write(default_settings_1())
   write_now.close()





def make_a_django_project_and_create_alts_and_models(project_name,n_models):
    folder_list=["html","static","local","Gallery"]
    html_child=['add',"update","remove","view_all","view_filter","view_single"]
    static_making=["css","js","img"]
    html_parent=["home.html","js_sec","css_sec","include_model_3","include_model_4","include_model_5"]
    print("creating the Django project")
    os.system("django-admin startproject "+project_name)
    os.chdir(project_name)
    make_a_write_action(project_name)
    os.chdir('..')


    print("making LVL1 folders")
    
    for f1 in range(len(folder_list)):
        if folder_list[f1]=="html":
            os.mkdir(folder_list[f1])
            os.chdir(folder_list[f1])
            print("creating html childrens")
            for f2 in range(len(html_parent)):
                print(f"creating {html_parent[f2]}.html ")
                os.system(f"nul>{html_parent[f2]}.html")
                print(".....DONE")
            os.chdir("..")
        elif folder_list[f1]=="static":
            os.mkdir(folder_list[f1])
            os.chdir(folder_list[f1])
            print("creating html childrens")
            for f3 in range(len(static_making)):
                print(f"creating {static_making[f3]} folder ")
                os.mkdir(static_making[f3])
                print(".....DONE")
            os.chdir("..")
        
        
    else:
        os.mkdir(folder_list[f1])
        print(folder_list[f1]+" CREATED")


def add_the_Links_content(model_name):
    print(f"printing all items with SINGULAR for {model_name}")
    return f"""
    
    #path('all_{str(model_name).lower()}',{model_name}_API_VIEW.as_view(),name='all_{str(model_name).lower()}s'),\n
    #path('single_{str(model_name).lower()}',Single_{model_name}_API_VIEW.as_view(),name='single_{str(model_name).lower()}'),\n
       """

def add_the_views_content(model_name):
    print(f"Create the views and SINGLE VIEWS for "+model_name)
    return f"""



class {model_name}_API_VIEW(APIView):

    #serializer_class= {model_name}_Serializer



    def post(self,r):
        #r.data={model_name}.objects.first()
        posted_data=r.data
        print(f"the posted data")
        ser_posted_data={model_name}_Serializer(data=posted_data)
        if ser_posted_data.is_valid(raise_exception=True):
            print("data posted successfully done")
          
            return Response(ser_posted_data.data,status=HTTP_201_CREATED)
        else:
            print("->"*10)
        
            for e in ser_posted_data._errors:
              print(str(ser_posted_data._errors[e]))
            print("->"*10) 
            return Response(ser_posted_data.data,status=HTTP_400_BAD_REQUEST)

    def get(self,r,user_code):
        all_data={model_name}.objects.all()
        print("We got all data "+str(all_data))
        ser_users={model_name}_Serializer(all_data).data
        return Response(data=ser_users,status=HTTP_200_OK)
    

    

            
class Single_{model_name}_API_VIEW(APIView):

    #serializer_class= {model_name}_Serializer



    def post(self,r):
        #r.data={model_name}.objects.first()
        posted_data=r.data
        print(f"the posted data")
        ser_posted_data={model_name}_Serializer(data=posted_data)
        if ser_posted_data.is_valid(raise_exception=True):
            print("data posted successfully done")
          
            return Response(ser_posted_data.data,status=HTTP_201_CREATED)
        else:
            print("->"*10)
        
            for e in ser_posted_data._errors:
              print(str(ser_posted_data._errors[e]))
            print("->"*10) 
            return Response(ser_posted_data.data,status=HTTP_400_BAD_REQUEST)

    def get(self,r,user_code):
        called_item={model_name}.objects.get(pk=user_code)
        print("We got the data of "+str(called_item.name))
        ser_users={model_name}_Serializer(called_item).data
        return Response(data=ser_users,status=HTTP_200_OK)
    

    def put(self,r,user_code):
        called_item={model_name}.objects.get(pk=user_code)
        old_data=called_item.objects
        
        ser_maker={model_name}_Serializer(called_item,r.data)
        if ser_maker.is_valid(raise_exception=True):
            ser_maker.save()
            return Response(data=ser_maker.data,status=HTTP_200_OK)
        else:
            print("errors report:"+str(ser_maker._errors))
            return Response(data=ser_maker.errors,status=HTTP_400_BAD_REQUEST)

    
    def delete(self,r,user_code):
        called_item={model_name}.objects.get(pk=user_code)
        old_data=called_item.delete()
        print("item deleted")
        return Response({str({'message':'item deleted'})},status=HTTP_400_BAD_REQUEST)



        \n\n








"""

def add_the_serlizer_content(model_name):
    print(f"making a serializer of {model_name}")
    return f"""

\n\n\n
class {model_name}_Serializer(ModelSerializer):

      
      class Meta:
            model = {model_name}
            fields = ('','','','','')



"""




def add_the_admin_content(model_name):
    print(f"making a ADMIN model of {model_name}")
    return f"""
\n\n\n
class {model_name}_ADMIN_CLASS(admin.ModelAdmin):pass

admin.site.register({model_name},{model_name}_ADMIN_CLASS)\n\n\n
"""




def add_the_form_model_content(model_name):
     print(f"building a model form for {model_name}")
     return '''
              
              
              \n\n\n
class Form_of_'''+str(model_name)+'''(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = '''+str(model_name)+'''
            fields = ()



               
            '''


def add_the_models_content(model_name):
    

    print(f"making {model_name} model")
    return f"""
               
               \n\n\n
class {model_name}(Model):
      # '','','','','','' 
      #field=OneToOneField({model_name}_Rel, related_name='rel_1',blank=True,null=True, on_delete=CASCADE)
      name=CharField(default="{model_name} model",verbose_name='field', max_length=40)

      def __str__(self):pass
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = '{model_name}'
            verbose_name_plural = '{model_name}'
             
              
                """








def make_a_django_app_and_insert_it_into_the_project(project_name,app_name,n_models):
    py_files_alts=['l.py','form_model.py','serialization.py','signal.py',
                   'Action_1.py',
                   'Action_2.py',
                   'Action_3.py',
                   'Action_4.py',
                   'Action_5.py',
                   ]
    print("Creating the django app")
    os.system("dir")
    os.system("pip3 install django")
    os.system("django-admin startapp "+app_name)
    print("Application created")
    os.chdir(app_name)
    for py in range(len(py_files_alts)):
      make_file=open(py_files_alts[py],'w+')
      print(f"\n\nfile {py_files_alts[py]} created\n\n")
      print("Adding model items into models.py\n"+str(model_items))

    write_cont=open('models.py','+a')
    for m in range(len(model_items)):
        write_cont.write(add_the_models_content(model_items[m]))
    write_cont.close()


    write_cont=open('views.py','+a')
    write_cont.write("""
      
      from .models import *
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic.edit import *
#from django.views.generic import *
from django.urls import *

#from django.contrib.sessions.request.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from .form_model import *
from django.shortcuts import *
from .Action_1 import *
from datetime import date,time
from datetime import datetime as dt
      

""")
    for m in range(len(model_items)):
      write_cont.write(add_the_views_content(model_items[m]))
    write_cont.close()



    write_cont=open('l.py','+a')
    write_cont.write("\n from .views impoert *\nfrom django.urls import *\n\n\n urlpatterns=[ \n\n #add the path links here \n\n ]")
    for m in range(len(model_items)):
          
        write_cont.write(add_the_Links_content(model_items[m]))
          
    write_cont.close()

    write_cont=open('form_model.py','+a')
    write_cont.write("\nfrom .models import *\n")
    for m in range(len(model_items)):
        write_cont.write(add_the_form_model_content(model_items[m]))
    write_cont.close()

    write_cont=open('serialization.py','+a')
    write_cont.write("\nfrom .models import *\n")
    for m in range(len(model_items)):
        write_cont.write(add_the_serlizer_content(model_items[m]))
    write_cont.close()

    write_cont=open('admin.py','+a')
    write_cont.write("\nfrom .models import *\n")
    write_cont.write("\nfrom django.contrib import admin\n")
    for m in range(len(model_items)):
        write_cont.write(add_the_admin_content(model_items[m]))
    write_cont.close()


      

      
      

      
    
    os.chdir("..")






def write_the_following_actions():pass

make_venv=input("create your venv model:")

make_a_venv_model_and_setup_all_libs_with_django(make_venv)

dj_project=input("create your Django project:")
dj_app=input("create your Django APP:")
max_models=int(input("maximum number of models:"))

model_items=[]


for m in range((max_models)):
    
    model_items.insert(m,input(f"adding the model number {str(m+1)}:"))
    print("item number "+str(m)+" was added ")



print(f"all models\n{str(model_items)}")

make_a_django_project_and_create_alts_and_models(dj_project,max_models)
make_a_django_app_and_insert_it_into_the_project(dj_project,dj_app,max_models)


print("\nCALLING THE FRONT END PHASE\n")
os.system("cd ../../..")
os.system("python call_of_meran.py")