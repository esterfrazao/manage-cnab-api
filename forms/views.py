from django.shortcuts import render
from django.template import loader
from files.models import File
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response


def index(request):
    """View Function that renders form page of site"""
    num_files = File.objects.all().count()
    context = {"numFiles": num_files}
    return render(request, "index.html", context=context)


# class FormView(StaticHTMLRenderer):
#     def render(self):
#         # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#         template = loader.get_template("forms/templates/index.html")
#         # template = loader.get_template("forms/index.html")
#         context = {
#             # 'latest_question_list': latest_question_list,
#         }

#         return super().render(template)
