# Function for django templates(dropdown menu)
A function implemented via **templatetags** to render a menu with *n* child elements.
To add child branches, you need to use the following construction:
Between the \<li> tags, place an \<ul> element. Inside it, iterate through all the items using a loop, add them within \<li> tags, and so on. You can add an unlimited number of child elements.
Everything is edited in the django admin panel.
## Comment
I found this interesting because I wanted to make a large drop-down menu for my project.


