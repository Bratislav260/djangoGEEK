from typing import Any
from django import forms
from posts.models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    content = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "python":
            raise forms.ValidationError("Такое нельзя")
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title.lower() == content.lower():
            raise forms.ValidationError("Такое нельзя")


class PostForm2(forms.Form):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "python":
            raise forms.ValidationError("Такое нельзя")
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title.lower() == content.lower():
            raise forms.ValidationError("Такое нельзя")


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False, max_length=100, min_length=2, widget=forms.TextInput(
            attrs={
                "placeholder": "search",
                "class": "form-control",
            }
        )
    )
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    orderings = (
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания (по убыванию)"),
        ("title", "По названию"),
        (-"title", "По названию по убыванию)"),
        ("rate", "По рейтингу"),
        (-"rate", "По рейтингу по убыванию)")
    )

    ordering = forms.ChoiceField(required=False, choices=orderings)
