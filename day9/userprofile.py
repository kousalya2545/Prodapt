from typing import TypedDict,Optional,List

class UserProfile(TypedDict):
    id: int
    name: str
    email: str
    bio: Optional[str]

def format_user_profile(users: List[UserProfile])->List:
    return [f"{u['name']}({u['email']})" for u in users]

users = [
    {
        "id" : 1,
        "name":"Alice",
        "email":"kousalya@prodapt.com",
        "bio" : None 
    },
    {
        "id" : 2,
        "name":"Bob",
        "email":"kousalya1@prodapt.com",
        "bio" : "Life is fun with wires and laptops" 
    }
] 
print(format_user_profile(users))
# profile1 = UserProfile(id=1,name="Kousalaya", email="kousalya@prodat.com",bio="")
# print(profile1)
