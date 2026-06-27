from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from projects.models import Project, Membership


@login_required
def create_task(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access to this project.')
        return redirect('projects:dashboard')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status', 'todo')
        priority = request.POST.get('priority', 'medium')
        due_date = request.POST.get('due_date') or None
        assigned_to_id = request.POST.get('assigned_to') or None

        if not title:
            messages.error(request, 'Task title is required.')
            return redirect('tasks:create', project_pk=project_pk)

        Task.objects.create(
            project=project,
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            assigned_to_id=assigned_to_id,
            created_by=request.user,
        )
        messages.success(request, 'Task created successfully!')
        return redirect('projects:detail', pk=project_pk)

    members = project.get_members()
    return render(request, 'tasks/create.html', {
        'project': project,
        'members': members,
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access to this task.')
        return redirect('projects:dashboard')

    comments = task.comments.all().order_by('created_at')
    members = project.get_members()
    return render(request, 'tasks/detail.html', {
        'task': task,
        'project': project,
        'comments': comments,
        'members': members,
    })


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access to this task.')
        return redirect('projects:dashboard')

    if request.method == 'POST':
        task.title = request.POST.get('title', task.title).strip()
        task.description = request.POST.get('description', '').strip()
        task.status = request.POST.get('status', task.status)
        task.priority = request.POST.get('priority', task.priority)
        task.due_date = request.POST.get('due_date') or None
        task.assigned_to_id = request.POST.get('assigned_to') or None
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks:detail', pk=pk)

    members = project.get_members()
    return render(request, 'tasks/update.html', {
        'task': task,
        'project': project,
        'members': members,
    })


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if project.owner != request.user and task.created_by != request.user:
        messages.error(request, 'You cannot delete this task.')
        return redirect('tasks:detail', pk=pk)

    if request.method == 'POST':
        project_pk = project.pk
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('projects:detail', pk=project_pk)

    return render(request, 'tasks/delete.html', {'task': task})


@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access.')
        return redirect('projects:dashboard')

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['todo', 'in_progress', 'done']:
            task.status = status
            task.save()
    return redirect('projects:detail', pk=project.pk)