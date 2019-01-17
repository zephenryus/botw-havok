from havok.Header import Header


def main():
    files = [
        'assets/12-16.hktmrb',
        'assets/19-13.hknm2',
        'assets/Enemy_Assasin_Leader.hkrg',
        'assets/FldObj_FallingRock_A_01.hkrb',
        'assets/G-6-2.hksc',
        'assets/Npc_King_Vagrant.hkcl'
    ]

    for filename in files:
        with open(filename, 'rb') as infile:
            header = Header(infile)
            print(header)


if __name__ == "__main__":
    main()