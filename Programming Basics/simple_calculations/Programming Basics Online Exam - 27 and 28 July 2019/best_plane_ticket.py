h = None
while True:
    plane_ticket = input()
    if plane_ticket == "End": break
    price_ticket = float(input())
    minutes = int(input())

    h_h = minutes // 60
    m_m = minutes % 60

    if h is None or h_h < h or (h_h == h and m_m < m):
        h = h_h
        m = m_m
        ticket = plane_ticket
        price = price_ticket * 1.96
    else: continue

print(f"Ticket found for flight {ticket} costs {price:.2f} leva with {h}h {m}m stay")
