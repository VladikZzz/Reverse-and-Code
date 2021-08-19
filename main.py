string = input()
string = string[::-1]
alpha_small = 'abcdefghijklmnopqrstuvwxyz'
alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
out_s = ''

for j in range(len(string)):
    for i in range(len(alpha_big)):
        if string[j] == alpha_small[i]:
            out_s += str(i + 1) + " "
            break
        if string[j] == alpha_big[i]:
            out_s += str(i + 1) + " "
            break

print(out_s)