# import socket

# esp32_ip = '172.29.132.108'
# esp32_port = 50005

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((esp32_ip, esp32_port))
#     data = s.recv(1024)

# print(f"Received {data!r}")


# method 2 
# import socket

# HOST = "172.29.135.102"
# PORT = 50004

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             if data:
#                 conn.sendall(data)
#                 print(data)

# # buffer flush flush input output
import numpy as np
import cmath

def FFT(P):
    n = len(P)
    if n <= 1:
        return P
    even = FFT(P[0::2])
    odd = FFT(P[1::2])
    T = [cmath.exp(-2j * np.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + [even[k] - T[k] for k in range(n // 2)]

def inverse_FFT(P):
    n = len(P)
    P = FFT([x.conjugate() for x in P])
    return [x.conjugate() / n for x in P]

def FFT_multiply(P, Q):
    n = len(P)
    P_fft = FFT(P)
    Q_fft = FFT(Q)
    result_fft = [P_fft[i] * Q_fft[i] for i in range(n)]
    return [int(x.real + 0.5) for x in inverse_FFT(result_fft)]

def max_self_match(S, alphabet):
    n = len(S)
    max_match = 0
    
    # Pad the strings to have length power of 2
    while (n & (n - 1)) != 0:
        n += 1
        S += ' '
    
    for c in alphabet:
        # Step 1: Create the polynomial f_c(x)
        f_c = [1 if char == c else 0 for char in S]
        
        # Create the reverse polynomial f_c^R(x)
        f_c_R = list(reversed(f_c))
        
        # Step 2: Polynomial Multiplication using FFT
        result = FFT_multiply(f_c, f_c_R)
        
        # Step 3: Find the maximum coefficient in the result
        for i in range(len(S)):
            max_match = max(max_match, result[i])
    
    print(max_match)
    return max_match

# Test the function with the string "ababa"
max_self_match("abcabc", ['a', 'b', 'c'])
