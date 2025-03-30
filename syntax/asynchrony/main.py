import asyncio
import time

async def func():
    print('func')
    await asyncio.sleep(1)

def main():
    asyncio.run(func())

if __name__ == '__main__':
    main()

# Пример двух асинхронных функций
async def func1():
    print('func1')
    await asyncio.sleep(1)

async def func2():
    print('func2')
    await asyncio.sleep(1)

def main1():
    asyncio.run(func())

async def main():
    start_time = time.time()
    await asyncio.gather(func1(), func2())
    finish_time = time.time()
    print(finish_time - start_time)

if __name__ == '__main__':
    asyncio.run(main())