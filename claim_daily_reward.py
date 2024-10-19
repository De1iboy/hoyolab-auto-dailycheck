from genshin import Game, Client, InvalidCookies, AlreadyClaimed

async def claim(ltuid: str, ltoken: str, ltmid: str):
    target_games=[
        Game.GENSHIN, Game.STARRAIL,
        Game.ZZZ
    ]
    client=Client(
        lang="ko-kr",
        cookies={
            "ltuid_v2": ltuid,
            "ltoken_v2": ltoken,
            "ltmid_v2": ltmid
        }
    )

    for g in target_games:
        status="❌"

        try:
            await client.claim_daily_reward(game=g)
            status="✅"
        except(InvalidCookies, AlreadyClaimed) as e:
            status="🟡"
        
        _, day=await client.get_reward_info(game=g)
        rewards=await client.get_monthly_rewards(game=g)
        reward=rewards[day-1]

        print(f"Claimed[{status}]: {reward.name} x{reward.amount}")

if __name__ == "__main__":
    import os
    import asyncio

    ltuid1=os.getenv("GENSHIN_ACCOUNT_LTUID")
    ltoken1=os.getenv("GENSHIN_ACCOUNT_LTOKEN")
    ltmid1=os.getenv("GENSHIN_ACCOUNT_LTMID")
    ltuid2=os.getenv("STARRAIL_ACCOUNT_LTUID")
    ltoken2=os.getenv("STARRAIL_ACCOUNT_LTOKEN")
    ltmid2=os.getenv("STARRAIL_ACCOUNT_LTMID")
    ltuid3=os.getenv("ZZZ_ACCOUNT_LTUID")
    ltoken3=os.getenv("ZZZ_ACCOUNT_LTOKEN")
    ltmid3=os.getenv("ZZZ_ACCOUNT_LTMID")

    asyncio.run(claim(ltuid=ltuid1, ltoken=ltoken1, ltmid=ltmid1))
    asyncio.run(claim(ltuid=ltuid2, ltoken=ltoken2, ltmid=ltmid2))
    asyncio.run(claim(ltuid=ltuid3, ltoken=ltoken3, ltmid=ltmid3))
