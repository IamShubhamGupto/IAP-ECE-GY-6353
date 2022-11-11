def get_bin(addr) -> list:
    bin_val = []
    for val in addr:
        bin_val.append(bin(val))
    return bin_val

def get_decimal(addr) ->list:
    decimal = []
    for i in range(4):
        decimal.append(int(str(addr[i]),2))
    return decimal

def get_network_address(ipaddr_bin, subnet_bin) -> list:
    network_bin = []
    for i in range(4):
        network_bin.append(bin(int(ipaddr_bin[i],2) & int(subnet_bin[i],2)))
    return network_bin

def get_broadcast_address(network_bin, subnet_bin) -> list:
    broadcast_bin = []
    for i in range(4):
        broadcast_bin.append(bin(int(network_bin[i],2) | ( ~ int(subnet_bin[i],2) )))
    return broadcast_bin

ipaddr = [ 182, 158, 212, 67]
subnet = [ 255, 255, 0 ,0]
ipaddr_bin = get_bin(ipaddr)
subnet_bin = get_bin(subnet)
print(f'ipaddr bin {ipaddr_bin}')
print(f'subnet bin {subnet_bin}')
network_bin = get_network_address(ipaddr_bin, subnet_bin)
broadcast_bin = get_broadcast_address(network_bin, subnet_bin)
print(f'network bin {network_bin}')
print(f'broadcast bin {broadcast_bin}')
network_val = get_decimal(network_bin)
broadcast_val = get_decimal(broadcast_bin)


print(f'network deci {network_val}')
print(f'broadcast deci {broadcast_val}')




