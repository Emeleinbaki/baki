# def base(request):
#     footer_socials = Social.objects.all()
#
#     try:
#         places = Address.objects.get(main_place=True)
#     except ObjectDoesNotExist:
#         places = Address.objects.first()
#
#     params = {'footer_socials': footer_socials,
#               # 'emails': emails, 'footer': footer,
#                'places': places,
#               # 'subcategories': subcategories
#                 }
#
#     return params