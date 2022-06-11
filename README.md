### Simple Task Tracker Application (v0.0)
GitHub Repo: [https://github.com/sannjayy/drf-simple-task-tracker](https://github.com/sannjayy/drf-simple-task-tracker/)

---
**Dev Stack:** 

- Python - 3.10.5
- Django - 4.0.5
- Django Rest Framework - 3.13

---
## Project Name: `project`
#### Static Directory: `/static` ||  Media Directory: `/media` located on root directory.

**Apps:** 
## Endpoints:

**1. Accounts/User Accounts:**  `/users/v1/` 
- **`/users/v1/auth/login/`** `:POST` 

*Login can be performed with **username** or **email**.*

- **`/users/v1/account/`** `:GET`

*Fetch Authenticated user's Info*

- **`/users/v1/auth/logout/`** `:POST` 

*Logout endpoint.*

- **`/users/v1/auth/logout/all/`** `:POST` 

*Logout from all devices.*

- **`/users/v1/auth/token/verify/`** `:POST` 

*For verifying the access token.*
- **`/users/v1/auth/token/refresh/`** `:POST` 

*For refreshing the access token.*

---

**2. TaskTracker/Tasks:**  `/api/v1/`

- **`/api/v1/tasks/`** `:GET | :POST` 

List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **User**. 

- **`/api/v1/tasks/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

**Team Leader** only can modify by the *Team Members*. 

`:DELETE` only performed by the owner of the Team. 

---

**3. TaskTracker/Teams:**  `/api/v1/`

- **`/api/v1/teams/`** `:GET | :POST` 

List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **User**. 

- **`/api/v1/teams/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` 

`:GET` can be performed by associated with the **User, Team Leader & Team Members**. 

**Team Leader** only can modify by the *Team Members*. 

`:DELETE` only performed by the owner of the Task. 

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

