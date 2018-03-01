from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=120,verbose_name='Title')
    content=models.TextField('Content')
    publishing_date=models.DateTimeField('Publishing Date',auto_now_add=True)
    image=models.ImageField(null=True,blank=True)

#verbose_name ile bize gorunecegi ismi veriyoruz.

#yazdigim her post admin panelinde bana postobject olarak gorunuyor.
#ama ben post[1,2...] olarak gorunmesini istiyorum. bunun icin asagidaki kodu yazdim.
    #bu kod ile posta koydugum baslik gelecek. post object yazmayacak.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})
        #return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create')
    def get_update_url(self):
        return reverse('post:update',kwargs={'id':self.id})
    def get_delete_url(self):
        return reverse('post:delete',kwargs={'id':self.id})

    class Meta:
        ordering=['-publishing_date','id']