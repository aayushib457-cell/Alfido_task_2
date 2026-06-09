import requests

print("Fetching User Data...\n")

# API URL
url = "https://randomuser.me/api/?results=5"

try:
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Save data into file
        with open("users.txt", "w", encoding="utf-8") as file:

            print("Users from API:\n")

            for user in data["results"]:

                name = user["name"]["first"] + " " + user["name"]["last"]
                email = user["email"]
                country = user["location"]["country"]

                # Filtering Logic
                if country:

                    print("Name:", name)
                    print("Email:", email)
                    print("Country:", country)
                    print("------------------------")

                    file.write(f"Name: {name}\n")
                    file.write(f"Email: {email}\n")
                    file.write(f"Country: {country}\n")
                    file.write("------------------------\n")

        print("\nData saved successfully in users.txt")

    else:
        print("Error: Unable to fetch data")

except Exception as e:
    print("Exception Occurred:", e)