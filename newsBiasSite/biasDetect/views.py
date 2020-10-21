from django.shortcuts import render
from .forms import ArticleForm, CommentForm
from .utils.ai import newsScoringMachine
from .models import Comment

def newsIndex(request):
    form = ArticleForm()
    submit = ''

    commentForm = CommentForm()
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = Comment(
                author=commentForm.cleaned_data["author"],
                body=commentForm.cleaned_data["body"],
            )
            comment.save()
        submit = "Thank You! Your comment has been saved. To view your comment, go to the comments tab."

    # clear comment after saving
    commentForm = CommentForm()
    comments = Comment.objects.all()

    context = {
        "form": form,
        "commentForm" : commentForm,
        "comments": comments,
        "submit": submit,
    }
    return render(request, "newsIndex.html", context)



def newsScore(request):
    score = 'n/a'
    text = ''
    summary = ''
    scoreMachine = newsScoringMachine()

    if request.method == 'GET':
        form = ArticleForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data["body"]
            score = scoreMachine.scoreArticle(text = text)
            summary = scoreMachine.summarize(text = text)

    commentForm = CommentForm()
    comments = Comment.objects.all()
    context = {
        "text" : text,
        "score": score,
        "commentForm":commentForm,
        "comments":comments,
        "summary": summary,
    }
    return render(request, "newsScore.html", context)


def about(request):
    commentForm = CommentForm()
    context = {
        "commentForm":commentForm,
    }
    return render(request, "about.html", context)

def comments(request):
    
    commentForm = CommentForm()
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = Comment(
                author=commentForm.cleaned_data["author"],
                body=commentForm.cleaned_data["body"],
            )
            comment.save()

    # clear comment after saving
    commentForm = CommentForm()
    comments = Comment.objects.order_by('-created_on')

    context = {
        "commentForm" : commentForm,
        "comments": comments,
    }
    return render(request, "comments.html", context)