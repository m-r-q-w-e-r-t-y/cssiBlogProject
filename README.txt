https://github.com/google/cssi-blogasaurus/blob/step-6-users-api/templates/new_post.html

https://github.com/google/cssi-blogasaurus/blob/step-6-users-api/templates/show_posts.html

https://github.com/google/cssi-blogasaurus/blob/step-6-users-api/main.py

The process is explained below:
  The main.py loads the new_post.html (the html files contains the form) (this the get(self) portion of BlogHandler on main.py)
  
  Once the forms are submited, the post() method of BlogHandler deals with what is in the forms. It places it in show_posts.html
  
  The content is fills in the spaces with {{ }}} in show_posts.html
