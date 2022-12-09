# broken
alpha = 0.25
beta = 0.125

G = 3
rtt_ms = [1, 2, 3, 4]
rtt_s = rtt_ms[0]
rtt_d = rtt_ms[0]/2

for rtt_m in rtt_ms:
    new_rtt_s = alpha*rtt_m + (1-alpha)*rtt_s
    new_rtt_d = beta*abs(rtt_m-rtt_s) + (1-beta)*rtt_d
    
    rtt_s = new_rtt_s
    rtt_d = new_rtt_d
    rto = rtt_s + max(G, 4*rtt_d)
    print(f"{rtt_m} | rtt_s = {rtt_s} | rtt_d = {rtt_d} | rto = {rto}")

# rto = max(rto,  rtt_s+4*rtt_d)
# print(f"first rto = {rto}")
# print(f"second rto = {2*rto}")