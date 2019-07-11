from datetime import datetime
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render as django_render
from mezzanine.conf import settings
from mezzanine.utils.views import render, paginate

from .models import Project, ProjectCategory, ProjectImage, Reference


def project_list(request, category=None, template='kartoza_project/project_list.html'):
    """
    Display a list of project that are filtered by category.
    Custom templates are checked for using the name
    ``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
    """
    settings.use_editable()
    templates = []
    projects = Project.objects.all()
    if category is not None:
        category = get_object_or_404(ProjectCategory, slug=category)
        projects = projects.filter(categories=category)
        templates.append(u'kartoza_project/project_list_%s.html' %
                         unicode(category.slug))

    # requires Django VERSION >= (1, 4):
    projects = projects.prefetch_related('categories')

    projects = paginate(projects, request.GET.get('page', 1),
                        settings.PROJECTS_PER_PAGE,
                        settings.MAX_PAGING_LINKS)
    context = {'projects': projects, 'category': category}
    templates.append(template)
    return render(request, templates, context)


def project_detail(request, slug,
                   template='kartoza_project/project_detail.html'):
    """
    Custom templates are checked for using the name
    ``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
    person's slug.
    """
    project = get_object_or_404(Project, slug=slug)
    images = ProjectImage.objects.filter(project=project).order_by('id')
    references = Reference.objects.filter(project=project).order_by('name')

    context = {
        'project': project,
        'images': images,
        'references': references
    }
    templates = [u'kartoza_project/project_detail_%s.html' % unicode(slug), template]
    return render(request, templates, context)


def project_list_ongoing(request, template='kartoza_project/project_list.html'):
    templates = []
    projects = Project.objects.all().exclude(
        date_start__isnull=True,
        date_end__isnull=True
    )
    projects = projects.filter(
        Q(date_end__isnull=False, date_end__gt=datetime.now().date()) |
        Q(date_end__isnull=True, date_start__isnull=False)
    )
    # requires Django VERSION >= (1, 4):
    projects = projects.prefetch_related('categories')

    projects = paginate(projects, request.GET.get('page', 1),
                        settings.PROJECTS_PER_PAGE,
                        settings.MAX_PAGING_LINKS)
    context = {'projects': projects}
    templates.append(template)
    return render(request, templates, context)


def view_project(request, project_id):
    if request.method == 'GET':
        project = Project.objects.filter(pk=project_id).first()
        images = ProjectImage.objects.filter(
                 project__id=project.id).all()
        clients = project.clients.values('name', 'title', 'logo').all()
        # form = ProjectForm(project
        return django_render(
            request,
            'view_project.html',
            {'project': project,
             'consultants': project.consultants.all(),
             'staff_involved': project.staff_involved.all(),
             'clients': clients,
             'images': images}
        )


def get_reference(request):
    if request.method == 'POST':
        reference = ''
        reference_id = request.POST['reference_id']
        if len(reference_id) > 0:
            reference = Reference.objects.filter(pk=int(reference_id))
            reference_json = serializers.serialize('json', reference)
        return HttpResponse(reference_json)
