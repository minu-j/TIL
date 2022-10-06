from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.CharField('', max_length=10)
    issue_b = models.CharField('', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


PICK_CHOICE = (
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
)
class Comment(models.Model):
    article = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
    pick = models.CharField(max_length=50, choices=PICK_CHOICE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content