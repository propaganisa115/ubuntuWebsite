**Tutorial instalasi**

requirements: python3

1. clone repo ini (perintah: git clone https://gitlab.com/propaganisa.reg/mainapi.git)
2. masuk ke direktori yang sudah di clone (perintah: cd mainapi)
3. aktifkan virtual environtment dengan (paerintah: source venv/bin/activate)
4. buat database pada mysql dengan nama "mainAPI"
   note: jika user mysql yg digunakan "root" dan password dikosongkan "", langsung ke step 5
   , tetapi jika user atau password berbeda maka perlu dilakukan modifikasi pada settings.py 
   dibagian variabel database, seperti dibawah, 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mainAPI',
            'USER': 'isi-dengan-user-anda',
            'PASSWORD': 'isi-dengan-password-anda',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

5. maju satu direktori, ke direktori mainapi(perintah: cd mainapi)
6. lakukan tahapan migrasi database, dengan perintah dibawah ini:

-     python manage.py migrate
-     python manage.py makemigrations app
-     python manage.py migrate


7. masih pada direktori yang sama jalankan server (perintah: python manage.py runserver)
