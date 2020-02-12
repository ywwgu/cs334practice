

from cs334demo.config import Config


def main():
    config = Config()

    print(config.get_delay())
    print(config.get_secret())


if __name__ == '__main__':
    main()
