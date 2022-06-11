### Simple Task Tracker Application (v0.0)
GitHub Repo: [https://github.com/sannjayy/drf-simple-task-tracker](https://github.com/sannjayy/drf-simple-task-tracker/)

---
**Dev Stack:** 

- Python - 3.10.5
- Django - 4.0.5
- Django Rest Framework - 3.13

---
## Project Name: `project`
#### Static Directory: `static` ||  Media Directory: `media`

**Apps:** 
## Endpoints:
**Accounts/User Accounts:**  `/users/v1/` 
- **`/users/v1/auth/login/`** `:POST` *Login API `username` or `email`* 
- **`/users/v1/account/`** `:GET` *Fetch Authenticated user's Info*
- **`/users/v1/auth/logout/`** `:POST` *Logout endpoint.*
- **`/users/v1/auth/logout/all/`** `:POST` *Logout from all devices.*
- **`/users/v1/auth/token/verify/`** `:POST` *For verifying the access token.*
- **`/users/v1/auth/token/refresh/`** `:POST` *For refreshing the access token.*

---

**TaskTracker/Teams:**  `/api/v1/`
- **`/api/v1/teams/`** `:GET | :POST` List all the teams that associated with the **User, Team Leader & Team Members.** `:POST` can only performed by **user**. 

- **`/api/v1/teams/<SLUG>/`** `:GET | :PUT | :PATCH | :DELETE` Fetch the team that associated with the **User, Team Leader & Team Members**. *Team member* or *Team members* only can modify by the *Team Leader*. `:DELETE` only performed by the owner of the Team.



---
## Admin Panel Permissions:

**Accounts/User Accounts:** 

- `Create` *Only `admin`, `user` and `leader` can create new users.* 
- `Read` *Read Only for members*
- `Update` *`admin`, `user` and `leader` can update.*
- `Delete` *Only `admin`, `user` can delete.*

---
**Task Manager/Teams:** 

- `Create` *Only `User`.*
- `Read` *Associated `User`, `Leader` & `Members`.*
- `Update` *Only `User` or `Leader`.*
- `Delete` *Only `User`.*

**Task Manager/Tasks:** 

- `Create` *Only `User` or `Leader`.*
- `Read` *Associated with Team or Assisgned, `User`, `Leader` & `Members`.*
- `Update` *Only `Members`.*
- `Delete` *Only `User`.*
----



---
Developed by *Sanjay Sikdar*.
