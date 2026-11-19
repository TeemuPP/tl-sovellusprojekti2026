import requests

GROUP_ID = 34

url = "http://172.20.241.167/luedataa_kannasta_groupid_csv.php"

try:
    response = requests.get(
        url,
        params={"groupid": GROUP_ID},
        timeout=15
    )

    response.raise_for_status()

    filename = f"mittaukset_group{GROUP_ID}.csv"

    with open(filename, "wb") as file:
        file.write(response.content)

    print("HTTP status:", response.status_code)
    print("Data tallennettu:", filename)

except requests.exceptions.RequestException as error:
    print("Virhe:", error)