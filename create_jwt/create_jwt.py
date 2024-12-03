import jwt
import time
import requests

# Carregar a chave privada
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAq64j5O8P4j2wCQXYejWNmvvs66gQ7/JKUU5UM3zVdqQy2VUk
O+vj0zYCyJA+/RxvettC4JjfdTNVkJVrgEtHMtV+sI/984PgxGwtSevhk3AMfBOo
S2xFSrwyhzVULTUW6td4EXIeTKyLGtnlinBiL7fWfCRO/jf0kLyObgYp8DhL4sBc
kbS+i36VfX2Df6bNYjxe3OPOK3Bb78s2lZyHJQ31Ab+Ccu29CZ24S9M/UjyxtWaA
hhj353PB2U0gXa2sTlAgKc7dW/lbL505fG6q8pSfGDo/st+q7CIQ4w+VaEZ02C9t
b/DH/n+45gC0DZTY5ZuIhuZQLoFKd92O0s6txQIDAQABAoIBAH70t/aEEurrU1JY
0E0PbTg/NGTQVDYcpniZxAqPNgwWQMQXAkSNnFyEhGpswSfL72Sa4EnWwuiYnZ3d
4TFueahN2PIYiWObEowusw8HMDknkxPuNXYRCuzJX1Q9S5JiwB/KVzAPg/iPYA7r
M6O8l99Rw3rqHsBAAMtHpMwYIstQn2OfFQz7uhRedySBrfxIyVili5S4slhsDNHZ
V6NzgMoyozR6WrphscEjWxU1HjmdpfIeLUbEl/9GhVuRRgTWtSAUSXrOBqjghBFa
KRrcC5yDEH73PijSFkwA6SbFqppshXcJDkRlOB47UQL9Z5dChNL20bLoZyzJmSWs
t8zu1gECgYEA4cKyJ3LvPnlDmogjpJiPblVdxGbw29SjHM/fprKXbqDx4iaV+MLk
eF5ycNCyDX2ZpWdfcg/pDKoYbDXL74I28PR3qno/qtjVrJB4RZbcjG461sRhWjnd
ym5loWgNV6Ri7VrUCanC9KTijgPrFtcbSoS5yNu4cXEk8T8n4Ykj3UkCgYEAwq0J
bcRVu3xWeMmcCKoehoMHfKghDiOX45rGPYATsddBcY+zuevkhidhjwVluCI+pRyQ
UHFcIKIxTjCySVWxFHrXesL1Xq2HV9BB+JpolmaGABj7pdTgEzYHNIgzFZ6UVoky
dLDcyvb3GM47QKSL1Rbz+sdasesqHU2jhOwoOJ0CgYA/LWD1sTBKZ10HzblLwnXB
Bpqq77PPkP3kfje0Sp4eE2QdSXcGmmOdW7Di6UQqik+I/hizrsglByS2g4eCiwoc
/AzQ5E0U3oFNPVCrCMDHe8FzgJlNyovKroI6XQf+0r3sdlKIMb2hANN1spsDVUcJ
34KuNu6ysFsKOAZNEze6IQKBgDT7OtGw2VRJJo+A7wI8qkoZZvQ6HaTncvLysHkU
XkfMOXdakKNM28jW9uohoelXCI2PFIeQEm6fNaP+BMeIlsToGbTDUlwOBgOUHiA2
hbhI9rcYFYSwRrtzvMpDNwPvQJe8hwrTB4QFaoJJvj59icDYmlXp43kAc1m+Q35t
dxTRAoGBAMf3TaDMAtHedTNJkQzZkMIc8oQLjRlf2WTjPyVb3egAe68IrctXlT2D
9hm1hmCF03br7jdrXIjcaDTI1FmIqvsl21fAEbTzp7FzMmuMzGDcG4YVlDMM9MjU
IL5Ia/AAeONHN0NAeYAsHV5RKjqnPl3vceX0kk1qxbZqU4Gro085
-----END RSA PRIVATE KEY-----'''

# Definir o payload do JWT
payload = {
    'iat': int(time.time()),  # Hora atual
    'exp': int(time.time()) + (10 * 60),  # Expira em 60 minutos
    'iss': '1036921'  # Substitua pelo ID do seu aplicativo
}

# Gerar o JWT
try:
    token = jwt.encode(payload, private_key, algorithm='RS256')
    print(f'JWT: {token}')
except Exception as e:
    print(f'Erro ao gerar JWT: {e}')
