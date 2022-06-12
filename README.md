### Simple Task Tracker Application (v0.0)
GitHub Repo: [https://github.com/sannjayy/drf-simple-task-tracker](https://github.com/sannjayy/drf-simple-task-tracker/)

---
**Dev Stack:** 

- Python - 3.10.5
- Django - 4.0.5
- Django Rest Framework - 3.13

---
## Main Project Name: `project`

For assign **Role** based admin access can be done in the **Authentication and Authorization/Groups** default group names are: **User, Team Leader, Team Member** and **Super Admin**

For testing this project you can use a fresh database. Here is mine which are created on development time.

**Testing `Admin` Account:**
```
Email: admin@admin.com
Username: admin
Password: 123
```

**Testing `User` Account:**
```
Email: user@user.com
Username: user
Password: 123
```

**Testing `Team Leader` Account:**
```
Email: leader@leader.com
Username: leader
Password: 123
```

**Testing `Team Member` Account:**
```
Email: member@member.com	
Username: member
Password: 123
```
---
**Static Directory:** `/static` located on root directory.

**Media Directory:** `/media` located on root directory.

**Requirements:** `requirements.txt`

---
For background tasks implemented **Celery** and **Threading** Both.

Currently using on `Celery` if you wish to use `threading` open **app_task_tracker/emails.py** comment *line 20* and uncomment *line 19*
``` 
 # Util.send_mail(email_data, template_name='email/email_notification.html') # TODO: Uncomment If you wish to send emails using Threading
send_async_email_task.delay(email_data, template_name='email/email_notification.html') # Celery Task
```

**Running Celery:**
```
 celery -A project worker -l info -P eventlet
```
## Endpoints:

**1. Accounts/User Accounts:**  `/users/v1/` 
- **`/users/v1/auth/login/`** `:POST` 

*Login can be performed with **username** or **email**.*

- **`/users/v1/user/`** `:GET`

**Required Access Token:**
```
Bearer ACCESS_TOKEN_HERE
```

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
```
{
  "name": "string"
  "leader_id": 5
}

leader_id > Primary Key / User ID of Team Leader
```

- **`/api/v1/teams/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

`:PATCH | :PUT` 

**Team Leaders can perform only:**

```
{
  "member_ids": [1,2,3]
}

member_ids > Primary Key / User ID of Team Members.
```

**Team Leader:** only can modify by the *Team Members*. 

`:DELETE` only performed by the owner of the Task. 

---
**3. TaskTracker/Tasks:**  `/api/v1/`

- **`/api/v1/tasks/`** `:GET | :POST` 

List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **User**. 

```
{
    "team": 0,
    "title": "string",
    "description": "string",
    "priority": "low",
}

- team > primary key of Team.
```


- **`/api/v1/tasks/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

Search `/api/v1/tasks/?q=<QUERY>` by **title, description**

Filter records `/api/v1/tasks/?status=assigned` *[Options: `under review`, `assigned`, `in process`, `done`]*

Filter records `/api/v1/tasks/?priority=medium` *[Options: `low`, `medium`, `high`]*

`:PATCH | :PUT` 

**User:** Users can only update the Task's **Title** and **Description**
```
{
    "team": 0,
    "title": "string",
    "description": "string",
}
- team > primary key of Team.
```

**Team Leader:** Only can assign to members *[Status will be changed automaticly]*.

```
{
    "team": 0,
    "assigned_to": 0,
}

- team > primary key of Team.
- assigned_to > Primary Key / User ID of Team Member.
```

**Team Member:** Only can update the status.

```
{
    "team": 0,
    "status": "done"
}

- team > primary key of Team.
```
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

