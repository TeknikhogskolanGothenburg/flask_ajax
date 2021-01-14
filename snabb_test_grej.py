import json

def main():
    words = ['apa', 'banan', 'citron']
    json_str = json.dumps(words)
    print(type(words))


if __name__ == '__main__':
    main()
