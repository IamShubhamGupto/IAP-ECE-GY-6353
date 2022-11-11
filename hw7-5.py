
alpha = 0.125
beta = 0.25
rtt_s = 511
rtt_d = 62.4
rto = 200
rtt_ms = [611.728, 521.166, 537.835]

for rtt_m in rtt_ms:
    new_rtt_s = alpha*rtt_m + (1-alpha)*rtt_s
    rtt_d = beta*abs(rtt_m-rtt_s) + (1-beta)*rtt_d
    rtt_s = new_rtt_s
    print(f"rtt_s = {rtt_s} | rtt_d = {rtt_d}")

rto = max(rto,  rtt_s+4*rtt_d)
print(f"first rto = {rto}")
print(f"second rto = {2*rto}")