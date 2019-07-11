#Oyunu oynamak için;
[![Open my game in browser][shell_img]][shell_link]

[shell_img]: http://pixelartmaker.com/art/d6aad27db8ee3e9.png
[shell_link]: https://cstech-245800.appspot.com/


# Tutorial
Google Cloud uygulamasını bulut üzerinde çalıştırmak için;
https://cloud.google.com/python/django/appengine

Bu proje Python-django uygulamasıdır. lokalde çalıştırmak için pycharm uygulaması ile yeni bir django application başlatmak gereklidir. daha sonra views.py ve gameController.py proje içerisine kopyalanarak uygulama çalışır hale getirilir.
Oluşturduğunuz proje ek olarak index fonksiyonumuzu görmesi gerektiği için urls.py dosyasında admin satırının üzerine 

url(r'^$', index),

kısmı eklenmelidir.

urls.py örneği;


from cstech.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),

]

Uygulamayı test etmek için New Game butonuna basarak oynayabilirsiniz.