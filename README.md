Ogonek
---
![alt text](http://i.imgur.com/NhpxtJo.png "Ogonek")
---

### What is this?
---
This project is created using [Django](https://www.djangoproject.com/). The website will be similar to a blog in the aspect that it will feature posts and articles.  Each article will allow for comments through Facebook, though I may expand upon the avilable options for commenting.  I will be allowing writers to feature their work on the site.  

### What can a post contain?
---
A post contains a title, a body of text, and an image.  Once again, I may expand upon these options.  The subject of which the post will be written will be entirely up to the writer, however I will maintain the right to remove anything that I feel is overly offensive, or illegal.

### What is Ogonek?
---
THE Ogonek is a small tail added to vowels in the Latin alphabet.  Ogonek is the name of a small orginization that produces content.

### How can I get involved?
---
The development team will remain very small in the beginning so our interest in finding development members, at the moment, is very small.  We are currently looking for people who will be interested in writers who wish to produce content for this website.

If you are interested in getting involved in this project, please email me at: zackazt@gmail.com

---
### Deployment
---
###### My plan is to use a mixture of AWS and Digital Ocean for deployment. 
---
## Currently In Progress:
* **Ability to filter through posts by genre.**
* **A page for User profiles where they can link to their professional profiles, and receive credit for their work.**
* **A markdown tutorial/reference will be placed in the create post area.**

# Checklist

| Area                    | Description                                                | Complete? |
|-------------------------|:----------------------------------------------------------:|:---------:|
| Users                   | User model, user image, extra user credentials...          | Partial   |
| Profiles                | Formatting, displaying all aspects of user's credentials.  | Partial   |
| Layout                  | The design is still pretty boring.  Needs some motion.     | Partial   |
| Authentication          | Verify password field, verify email is authentic.          | Partial   |
| API                     | Implement an API that can be used cross platform.          | No        |
| Ads                     | Discrete ads, not overbearing, that can add to the design. | No        |


###### The following log starts from 5/15/16
### Log:
* Created another password field in order to verify the password.  This way if there is a typo, the user will not be stuck with a password they do not know.
* Created First Name and Last Name entries when registering for an account.  These fields are mandatory.
* User is added as staff after registering. In the future I will make it to where they are not staff until they verify their email address.
* Created user profiles.
* Designed the forms.
* Added capabilities for users to have profile pictures.
* Added links to user profiles int he navigation area, along with various places throughout the site.
* Added ability to rate posts out of 5 stars.
* Need to start planning for deployment in order to get feedback.



