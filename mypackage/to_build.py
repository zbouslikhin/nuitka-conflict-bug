from asyncio import run

async def main_test():
    print("h")


def main():
    run(main_test())


if __name__ == "__main__":
    main()