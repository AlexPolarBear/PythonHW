import os
import random
import asyncio
import aiohttp


async def download_file(url, file_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_path, 'wb') as f:
                f.write(await response.read())

async def main(count):
    os.makedirs("artifacts", exist_ok=True)
    tasks = []
    num_seeds = []

    for i in range(1, count+1):
        seed = str(random.randint(0, 5000)).zfill(4)
        
        if seed not in num_seeds:
            num_seeds.append(seed)
            url = f'https://firebasestorage.googleapis.com/v0/b/thisnightskydoesnotexist.appspot.com/o/images%2Fseed{seed}.jpg?alt=media'
            file_path = os.path.join("artifacts", f'nightsky{i}.jpg')
            tasks.append(asyncio.create_task(download_file(url, file_path)))
        else: 
            count += 1
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    count = int(input("Введите количество картинок: "))
    asyncio.run(main(count))
