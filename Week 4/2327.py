# 2327. Number of People Aware of a Secret
def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    MOD = 10**9+7
    # dp[i][j]: # people who have known the secret for exactly j days, at day i+1
    dp = [[0]*forget for _ in range(n)]
    for i in range(n):
        for j in range(forget):
            if i==0 and j==0:
                dp[i][j] = 1%MOD
            elif j==0:
                dp[i][j] = sum(dp[i-1][delay-1:forget-1])%MOD
            else:
                dp[i][j] = dp[i-1][j-1]%MOD

    return sum(dp[-1])%MOD

def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    MOD = 10**9+7
    # dp[i]: # people who start sharing the secret at day i+1
    dp = [0]*n
    dp[0] = 1

    share = 0
    for i in range(1, n):
        share = (share+dp[i-delay] if i-delay>=0 else 0)%MOD  # ppl who start sharing today
        share = (share-dp[i-forget] if i-forget>=0 else share)%MOD  # ppl who forget today
        dp[i] = share
    
    return sum(dp[-forget:])%MOD