# 計算量について

## 数学
- 最小公倍数(gcd)
計算量：log(min(a,b))
アルゴリズム：ユークリッドの互除法を用いる

- 最大公約数(lcm)
計算量：log(min(a,b))
アルゴリズム：a * b = gcd(a,b) * lcm(a,b)を利用する

## ソーティング
- クイックソート
計算量：N*log(N)

## 探索
- 二分探索：log(N)