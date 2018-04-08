from django.contrib import admin
from post.models import Post
from post.models import Comment
# Register your models here.

#admin panaelinde postumuz gorunmuyordu. bunun icin postumuzu admin paneline bagladik


#bu kisim panelimi ozellestirmek icin yaptigim kisim
class PostAdmin(admin.ModelAdmin):

    #ornegin burada admin/post sayfamda title ve publishingdate olarak veri donecek.
    list_display = ['title','publishing_date','slug']

    #publishing date  e gore siraladim ama ona tiklayinca gitmiyordu. bunun icinde su kodu yazdim.
    list_display_links = ['publishing_date']

    #bircok post yazdigimda arama siralama vs gibi seyler lazim olacak. bunun icin de filtreleme kullanicam.
    #yayinlanma tarihine gore
    list_filter = ['publishing_date']

    #arama cubugu ekleyelim.baslik ve icerike gore arama yapacak
    search_fields = ['title','content']

    #burada title i admin panelinden degistirebilirim artik.
    list_editable =['title']

    class Meta:
        model=Post

# class CommentAdmin(admin.ModelAdmin):
#
#     list_display = ['post', 'name', 'content', 'created_date']
#
#     class Meta:
#         model = Comment
#
# admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)

