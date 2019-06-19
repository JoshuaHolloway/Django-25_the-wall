from django.db import models
# ======================================================================================================================
class User(models.Model):
  name = models.CharField(max_length=255)
  # TODO: first/last-name, email, password
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Book: ({self.title})"
# ======================================================================================================================
class Comment(models.Model):
  message = models.TextField()
  author = models.ForeignKey(User, related_name="comments")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Author: ({self.message})"
# ======================================================================================================================