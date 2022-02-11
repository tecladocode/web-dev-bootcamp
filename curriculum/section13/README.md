---
name: Authentication in Flask Apps
---

# Authentication in Flask Apps

## Plan

1. What are cookies and sessions?
2. Registering users with Flask
   1. Provide starter code with home and protected route
3. Logging in and populating the session
    1. Handle unauthorized requests
4. How to encrypt passwords with passlib
5. Sessions are not encrypted, so don't store secrets that you don't want the user to see in it
   1. User can reads the contents of the session, but user can't change the contents of the session easily
   2. You can store user secrets, just not app secrets
   3. https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session
## Other notes

