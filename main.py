from pyscript import document, display
G7 = {"Georgina Samia",  "Zoe Songco", "Redd Morta", "Woojae Song"}
G8 = {"Sean Yeung", "Tua Mandap", "Travis Jose"}
G9 = {"Sydney De Leon", "Megan Tan", "Annika Marquez", "Loriz Santos", "Maia Rodolfo"}
G10 = {"Upper Division"}
members = (G7|G8|G9|G10)

def Enter(e):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    members.add("first + last")

document.querySelector("#output").innerText = str(members).strip("{}")