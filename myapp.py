import streamlit as st

#Initializing Role
if "role" not in st.session_state:
    st.session_state.role = None

#Defined the available Roles
ROLES = [None, "Requester", "Responder", "Admin"]

# Loging page
def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


#Add logout

def logout():
    st.session_state.role = None
    st.rerun()

# Define all pages
role = st.session_state.role

# Define account pages
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")


# Define the request pages
request_1 = st.Page(
    "request/request_1.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Requester"),
)
request_2 = st.Page(
    "request/request_2.py", title="Request 2", icon=":material/bug_report:"
)

# Define the remaining pages

respond_1 = st.Page(
    "respond/respond_1.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Responder"),
)
respond_2 = st.Page(
    "respond/respond_2.py", title="Respond 2", icon=":material/handyman:"
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")


# Group pages into convenint list
account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

# Add title that will show on all pages
st.title("Request manager")

# Adding the logo
st.logo("images/logo3.jpg", icon_image="images/logo4.jpg")


# Initializing dictionary of pages
page_dict = {}

# Build the dictionary of allowed pages by checking the user's role.
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = request_pages
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages
    
# Check if the user is allowed to access any pages and add the account pages if they are.
# If page_dict is not empty, then the user is logged in. The | operator merges the two # # dictionaries, adding the account pages to the beginning.
if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
   
# Fallback to the login page if the user isn't logged in.
else:
    pg = st.navigation([st.Page(login)])

# Execute the page returned by st.navigation.
pg.run()
