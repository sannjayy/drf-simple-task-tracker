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
