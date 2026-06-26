from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Project, Membership


@login_required
def dashboard(request):
    owned = Project.objects.filter(owner=request.user)
    member_of = Project.objects.filter(membership__user=request.user).exclude(owner=request.user)
    return render(request, 'projects/dashboard.html', {
        'owned': owned,
        'member_of': member_of,
    })


@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        if not name:
            messages.error(request, 'Project name is required.')
            return redirect('projects:create')
        project = Project.objects.create(
            name=name,
            description=description,
            owner=request.user
        )
        Membership.objects.create(project=project, user=request.user, role='owner')
        messages.success(request, f'Project "{name}" created successfully!')
        return redirect('projects:detail', pk=project.pk)
    return render(request, 'projects/create.html')


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access to this project.')
        return redirect('projects:dashboard')
    members = project.get_members()
    return render(request, 'projects/detail.html', {
        'project': project,
        'members': members,
    })


@login_required
def invite_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.owner != request.user:
        messages.error(request, 'Only the project owner can invite members.')
        return redirect('projects:detail', pk=pk)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        try:
            user = User.objects.get(username=username)
            if Membership.objects.filter(project=project, user=user).exists():
                messages.warning(request, f'{username} is already a member.')
            else:
                Membership.objects.create(project=project, user=user, role='member')
                messages.success(request, f'{username} added to the project!')
        except User.DoesNotExist:
            messages.error(request, f'User "{username}" not found.')
    return redirect('projects:detail', pk=pk)


@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.owner != request.user:
        messages.error(request, 'Only the owner can delete this project.')
        return redirect('projects:detail', pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('projects:dashboard')
    return render(request, 'projects/delete.html', {'project': project})