x = int(input())
x_str = str(x)
x_str_invet = x_str[::-1]
pali_verify = True

for i in range(len(x_str)):
    if x_str[i] != x_str_invet[i]:
        pali_verify = False
        break