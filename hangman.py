def hangman(word):
    rletters = list(word)
    stage = [
        '__________',
        '|     |   ',
        '|     o   ',
        '|    /|\  ',
        '|    / \  ',
        '|         ',
    ]

    board = ['_'] * len(word)

    wrong = 0
    win = False
    challenge = 1

    print('ハングマンにようこそ')
    
    while wrong < len(stage):
        print('\n')
        msg = '一文字を入力してください'
        user_input = input(msg)

        if user_input in rletters:
            cind = rletters.index(user_input)
            board[cind] = rletters[cind]
            rletters[cind] = '$'
            print('あたり')
            e = len(rletters)
            for i in board:
                print(i, end="")
            
            if '_' not in board:
                win = True
                break
        else:
            print('はずれ')
            for i in range(wrong + 1):
                print(stage[i])
            wrong += 1
        
    if win:
        print('あなたの勝ち')
    else:
        print('あなたの負け')


hangman('test')



