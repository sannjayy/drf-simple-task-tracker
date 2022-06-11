### Simple Task Tracker Application (v0.0)
GitHub Repo: [https://github.com/sannjayy/drf-simple-task-tracker](https://github.com/sannjayy/drf-simple-task-tracker/)

---
**Dev Stack:** 

- Python - 3.10.5
- Django - 4.0.5
- Django Rest Framework - 3.13

---
## Main Project Name: `project`

#### Static Directory: `/static` ||  Media Directory: `/media` located on root directory.

#### For Background Tasks **Celery** and **Threading** Both was implemented.
Currently using on `Celery` if you wish to use `threading` open **app_task_tracker/emails.py** comment *line 20* and uncomment *line 19*
``` 
 # Util.send_mail(email_data, template_name='email/email_notification.html') # TODO: Uncomment If you wish to send emails using Threading
send_async_email_task.delay(email_data, template_name='email/email_notification.html') # Celery Task
```

## Endpoints:

**1. Accounts/User Accounts:**  `/users/v1/` 
- **`/users/v1/auth/login/`** `:POST` 

*Login can be performed with **username** or **email**.*

- **`/users/v1/user/`** `:GET`

*Fetch Authenticated user's Info*

- `/users/v1/accounts/list/` `:GET`

List all accounts `/users/v1/accounts/list/?role=leader` will return all the leaders. Options: *[`user`, `leader`, `member` ]*

search users `/users/v1/accounts/list/?q=<QUERT>`  by **first_name, last_name, email, username**


- **`/users/v1/auth/logout/`** `:POST` 

*Logout endpoint.*

- **`/users/v1/auth/logout/all/`** `:POST` 

*Logout from all devices.*

- **`/users/v1/auth/token/verify/`** `:POST` 

*For verifying the access token.*
- **`/users/v1/auth/token/refresh/`** `:POST` 

*For refreshing the access token.*

---

**2. TaskTracker/Teams:**  `/api/v1/`

- **`/api/v1/teams/`** `:GET | :POST` 

List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **User**. 

- **`/api/v1/teams/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

`:PATCH | :PUT`

**Team Leader:** only can modify by the *Team Members*. 

`:DELETE` only performed by the owner of the Task. 

---
**3. TaskTracker/Tasks:**  `/api/v1/`

- **`/api/v1/tasks/`** `:GET | :POST` 

List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **User**. 

- **`/api/v1/tasks/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

Search `/api/v1/tasks/?q=<QUERY>` by **title, description**

Filter records `/api/v1/tasks/?status=assigned` *[Options: `under review`, `assigned`, `in process`, `done`]*

Filter records `/api/v1/tasks/?priority=medium` *[Options: `low`, `medium`, `high`]*

`:PATCH | :PUT` 

**User:** Users can only update the Task's **Title** and **Description**

**Team Leader:** Only can assign to members *[Status will be changed automaticly]*.

**Team Member:** Only can update the status.

`:DELETE` only performed by the owner of the task. 

---
## Admin Panel Permissions:

**1. Accounts/User Accounts:** 

- `Create` Only **Admin, User and Team Leader** can create new users.
- `Read` Read Only for **Team Members**.
- `Update` **Admin, User and Team leader** can update.
- `Delete` Only **Admin or User** can delete.

---
**2. Task Manager/Teams:** 

- `Create` Only **User**.
- `Read` Associated by **User, Team Leader & Team Members**.
- `Update` Only **User or Team Leader**.
- `Delete`  Only **User**.

**3. Task Manager/Tasks:** 

- `Create` Only **User** or **Team Leader**.
- `Read` Associated with Team or Assisgned, **User, Team Leader & Team Members**.
- `Update` Only **Team Members**.
- `Delete` Only **User**.
----



---
[![](https://img.shields.io/github/followers/sannjayy?style=social)](https://github.com/sannjayy)  
Developed by *Sanjay Sikdar*.   
- 📫 sanjay.sikdar2007@gmail.com

