
def get_bytes(num):
    bin_val = hex(num >> 24 & 0xff), hex(num >> 16 & 0xff), hex(num >> 8 & 0xff), hex(num & 0xFF)
    print_ip(bin_val)
    return bin_val

def print_ip(binary_values):
    print(int(binary_values[0], 16), ".", int(binary_values[1], 16), ".", int(binary_values[2], 16), ".", int(binary_values[3], 16), sep="")

test = get_bytes(0xc394a801)





# print(int(test[0]))