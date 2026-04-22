clients  = [
    (1, "111", "a@x.com"),
    (2, "111", "b@x.com"),
    (3, "222", "c@x.com"),
    (4, "333", "c@x.com"),
    (5, "444", "d@x.com"),
]

phones = {}
emails = {}

for id, number, email in clients:
    phones.setdefault(number,set()).add(id)
    emails.setdefault(email,set()).add(id)
print(clients)

duplicets = []
for o in (phones, emails):
    for ids in o.values():
        if len(ids) > 1:
            duplicets.append(ids)
print(duplicets)

duplicets_ids = set()
for m in duplicets:
    duplicets_ids |= m

cliean_clients = []
for client in clients:
    if client[0] not in duplicets_ids:
        cliean_clients.append(client[0])
print(cliean_clients)