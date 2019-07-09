from datetime import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import F, Q, When, Case
from .models import Project, ProjectCategory, ProjectImage, Reference
from mezzanine.conf import settings
from mezzanine.utils.views import render, paginate


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
