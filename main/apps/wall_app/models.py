from django.db import models
# ======================================================================================================================
# class User(models.Model):
#   name = models.CharField(max_length=64)
#   # TODO: first/last-name, email, password
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#
#   def __repr__(self):
#     return f"Book: ({self.name})"
# ======================================================================================================================
class Comment(models.Model):
  message = models.TextField()
  # author = models.ForeignKey(User, related_name="comments")
  #
  # # Recall, had issue with not being able to populate the comment with a value
  # # -The error is related to the foriegn key.
  # # -Recall that they said you need to create the one object before the many object
  # # -Before I remebered this I found the below hack, which I did not test yet.
  # # -Temporary solution: Comment out the User table and the line about foriegn keys
  # #https://stackoverflow.com/a/46088589
  # #author = models.ForeignKey(User, related_name="comments", null = True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Comment: ({self.message})"
# ======================================================================================================================