from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment
from tasks.models import Task


@login_required
def add_comment(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    project = task.project
    if not project.is_member(request.user) and project.owner != request.user:
        messages.error(request, 'You do not have access.')
        return redirect('projects:dashboard')

    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if body:
            Comment.objects.create(task=task, author=request.user, body=body)
            messages.success(request, 'Comment added!')
        else:
            messages.error(request, 'Comment cannot be empty.')

    return redirect('tasks:detail', pk=task_pk)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        messages.error(request, 'You can only delete your own comments.')
        return redirect('tasks:detail', pk=comment.task.pk)

    if request.method == 'POST':
        task_pk = comment.task.pk
        comment.delete()
        messages.success(request, 'Comment deleted.')
        return redirect('tasks:detail', pk=task_pk)

    return redirect('tasks:detail', pk=comment.task.pk)