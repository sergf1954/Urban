import asyncio


async def start_strongman(name, power):
    ball = 1
    Number_of_balls = 5
    print(f"Силач - {name} начал соревнование")
    while ball < 6:
        y = Number_of_balls / power
        await asyncio.sleep(y)
        print(f'Силач {name} поднял шар {ball}')
        ball +=1
    print(f"Силач - {name} закончил соревнование")


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())