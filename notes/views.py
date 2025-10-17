from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Notes
from .forms import *

def  notes_list(request):
    notes = Notes.objects.all().order_by('-created_at')
    return render(request, 'notes/notes_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    comments = note.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.note = note  
            comment.save()
            messages.success(request, "Your comment has been added successfully, Thanks for your Commentt")
            return redirect('note_detail', pk=note.pk)
    else:
        form = CommentForm()  
    
    return render(request, "notes/note_detail.html", {
        "note": note, 
        'comments': comments, 
        'form': form
    })

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, "Your note Have been added successfuly")
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form':form})

def note_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST,  instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, "Your selected Note Have been edited successfuly")
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, "Your Selected Note Have been Deleted successfuly")
        return redirect('notes_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})