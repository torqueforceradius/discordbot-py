token = "MTA5MjA4NzMwMzA3NTI3ODk3MQ.GIbdla.YRNMv9ajH8uBPIexc-fOdJDk9cJ9ChlpvXc2Ug"

import discord
import random

client = discord.Client(intents=discord.Intents.all())

word = ['achieve', 'expectation', 'common', 'practice', 'constantly', 'adventurer', 'explorer', 'feature', 'carry ~ about', 'remind ~ of', 'relatively', 'include', 'involve', 'excitement', 'regret', 'opportunity', 'solo', 'kayak', 'hit upon', 'set foot on', 'carry out', 'a number of~', 'enthusiasm', 'inspiration', 'perspiration', 'outstanding', 'anxious', 'perform', 'competition', 'pay off', 'fall in love with', 'toe', 'process', 'limitless', 'privilege', 'overcome', 'out of shape', 'nothing more than', 'make an effort']
wordict = {'achieve': '성취하다', 'expectation': '기대', 'common': '공통적인', 'practice': ['관행', '습관'], 'constantly': '끊임없이', 'adventurer': '모험가', 'explorer': '탐험가', 'feature': '특집으로 다루다', 'carry ~ about': '~을 가지고 다니다', 'remind ~ of': '~에게 ~을 상기시키다', 'relatively': '상대적으로', 'include': '포함하다', 'involve': '수반하다', 'excitement': '흥분', 'regret': '후회하다', 'opportunity': '기회', 'solo': '단독의', 'kayak': '카약', 'hit upon': '(우연히) 생각해내다', 'set foot on': '~에 발을 들여놓다', 'carry out': '수행하다', 'a number of~': ['여러 개의 ~', '여러 명의 ~'], 'enthusiasm': '열정', 'inspiration': '영감', 'perspiration': ['땀', '노력'], 'outstanding': '탁월한', 'anxious': '불안해하는', 'perform': ['수행하다', '공연하다'], 'competition': ['대회', '경연'], 'pay off': ['결실을 맺다', '보상 받다'], 'fall in love with': '-와 사랑에 빠지다', 'toe': '발가락', 'process': '과정', 'limitless': '무한한', 'privilege': '특권', 'overcome': '극복하다', 'out of shape': '변형된', 'nothing more than': '단지', 'make an effort': '노력하다'}

userinfo = {}
userdatabase = {}
usertestdata = {}

Ekqhd = "\U0001F44D"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.id in userinfo:
        useranswer = message.content.replace(' ', '')
        if type(wordict[userinfo[message.author.id]]) == str:
            realanswer = wordict[userinfo[message.author.id]].replace(' ', '')
            maxlen = len(useranswer) if len(useranswer) < len(realanswer) else len(realanswer)
            matchtimes = 0
            for a in range(0, maxlen):
                if useranswer[a] == realanswer[a]:
                    matchtimes += 1
            if 100 * (matchtimes/maxlen) >= 60:
                await message.channel.send(f'{message.author.mention} {Ekqhd} 정답입니다! \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.')
                del userinfo[message.author.id]
            else: 
                correctable = await message.channel.send(f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.')
                if userinfo[message.author.id] not in userdatabase[message.author.id][0]:
                    await correctable.edit(content=f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.\n허접쉑ㅋㅋ')
                    userdatabase[message.author.id][0].append(userinfo[message.author.id])
                else: await correctable.edit(content=f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.\n틀린거 또 틀리기 있기 없기??')
                del userinfo[message.author.id]
        else:
            elementmatch = 0
            for element in wordict[userinfo[message.author.id]]:
                realanswer = str(element).replace(' ', '')
                maxlen = len(useranswer) if len(useranswer) < len(realanswer) else len(realanswer)
                matchtimes = 0
                for a in range(0, maxlen):
                    if useranswer[a] == realanswer[a]:
                        matchtimes += 1
                if 100 * (matchtimes/maxlen) >= 60:
                    await message.channel.send(f'{message.author.mention} {Ekqhd} 정답입니다! \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.')
                    del userinfo[message.author.id]
                    elementmatch = 1
            if elementmatch == 0:
                correctable = await message.channel.send(f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.')
                if userinfo[message.author.id] not in userdatabase[message.author.id][0]:
                    await correctable.edit(content=f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.\n허접쉑ㅋㅋ')
                    userdatabase[message.author.id][0].append(userinfo[message.author.id])
                else: await correctable.edit(content=f'{message.author.mention} 오답입니다. \'{userinfo[message.author.id]}\'의 뜻은 \'{wordict[userinfo[message.author.id]]}\'였습니다.\n틀린거 또 틀리기 있기 없기??')
                del userinfo[message.author.id]

    if message.author.id in usertestdata:
        usertestdata[message.author.id][0] += 1
        testword = word[usertestdata[message.author.id][0]]
        useranswer = message.content.replace(' ', '')
        if type(wordict[testword]) == str:
            realanswer = wordict[testword].replace(' ', '')
            maxlen = len(useranswer) if len(useranswer) < len(realanswer) else len(realanswer)
            matchtimes = 0
            for a in range(0, maxlen):
                if useranswer[a] == realanswer[a]:
                    matchtimes += 1
            if 100 * (matchtimes/maxlen) >= 60:
                await message.channel.send(f'{message.author.mention} {Ekqhd} 정답입니다! \'{testword}\'의 뜻은 \'{wordict[testword]}\'였습니다.')
                usertestdata[message.author.id][2] += 1
            else: 
                await message.channel.send(f'{message.author.mention} 오답입니다. \'{testword}\'의 뜻은 \'{wordict[testword]}\'였습니다.')
                usertestdata[message.author.id][1].append(word[usertestdata[message.author.id][0]])
                usertestdata[message.author.id][3] += 1
        else:
            elementmatch = 0
            for element in wordict[testword]:
                realanswer = str(element).replace(' ', '')
                maxlen = len(useranswer) if len(useranswer) < len(realanswer) else len(realanswer)
                matchtimes = 0
                for a in range(0, maxlen):
                    if useranswer[a] == realanswer[a]:
                        matchtimes += 1
                if 100 * (matchtimes/maxlen) >= 60:
                    await message.channel.send(f'{message.author.mention} {Ekqhd} 정답입니다! \'{testword}\'의 뜻은 \'{wordict[testword]}\'였습니다.')
                    usertestdata[message.author.id][2] += 1
                    elementmatch = 1
            if elementmatch == 0:
                correctable = await message.channel.send(f'{message.author.mention} 오답입니다. \'{testword}\'의 뜻은 \'{wordict[testword]}\'였습니다.')
                usertestdata[message.author.id][1].append(word[usertestdata[message.author.id][0]])
                usertestdata[message.author.id][3] += 1
        if usertestdata[message.author.id][0] == len(word) - 1:
            correctrate = 100 * usertestdata[message.author.id][2] / (usertestdata[message.author.id][2] + usertestdata[message.author.id][3])
            if correctrate >= 90: await message.channel.send(f'{message.author.mention} 수고하셨습니다. 테스트가 끝났습니다.\n틀린 단어: {usertestdata[message.author.id][1]}\n{usertestdata[message.author.id][2]}개 정답 / {usertestdata[message.author.id][3]}개 오답, 정답률 {correctrate}%\n정말 대단합니다!!!!!!')
            elif correctrate >= 70: await message.channel.send(f'{message.author.mention} 수고하셨습니다. 테스트가 끝났습니다.\n틀린 단어: {usertestdata[message.author.id][1]}\n{usertestdata[message.author.id][2]}개 정답 / {usertestdata[message.author.id][3]}개 오답, 정답률 {correctrate}%\n잘 하셨습니다!')
            elif correctrate >= 50: await message.channel.send(f'{message.author.mention} 수고하셨습니다. 테스트가 끝났습니다.\n틀린 단어: {usertestdata[message.author.id][1]}\n{usertestdata[message.author.id][2]}개 정답 / {usertestdata[message.author.id][3]}개 오답, 정답률 {correctrate}%\n좀 노력이 필요하겠어요..')
            else: await message.channel.send(f'{message.author.mention} 수고하셨습니다. 테스트가 끝났습니다.\n틀린 단어: {usertestdata[message.author.id][1]}\n{usertestdata[message.author.id][2]}개 정답 / {usertestdata[message.author.id][3]}개 오답, 정답률 {correctrate}%\n병신')
            del usertestdata[message.author.id]
        else: await message.channel.send(f'{message.author.mention} 다음 단어의 뜻을 작성하세요: {word[usertestdata[message.author.id][0]+1]}')


    if message.content.startswith('ek'):
        if message.author.id not in userinfo and message.author.id not in usertestdata:
            ranum = random.randint(0, len(word)-1)
            userinfo[message.author.id] = word[ranum]
            await message.channel.send(f'{message.author.mention} 다음 단어의 뜻을 작성하세요: {word[ranum]}')
        if message.author.id not in userdatabase: userdatabase[message.author.id] = [[], 0, 0]

    if message.content.startswith('Z테스트'):
        if message.author.id not in userinfo:
            usertestdata[message.author.id] = [-1, [], 0, 0]
            await message.channel.send(f'{message.author.mention} 챌린지 모드를 시작합니다.\n다음 단어의 뜻을 작성하세요: {word[0]}')

    if message.content.startswith('Z룰렛'):
        members = ["김강석", "김기태", "윤지섭", "김기훈", "박윤성", "김태양", "강태호"]
        rulet = await message.channel.send(f'룰렛을 돌리겠습니다.. 두구두구..')
        await rulet.edit(content = f"룰렛을 돌리겠습니다.. 두구두구..\n{members[random.randint(0, len(members)-1)]}(이)가 당첨되었습니다! 축하합니다!!")

    if message.content.startswith('Z운세'):
        koi = ["죽었다 깨나도 안 됨", "전생하면 가능", "15층에서 떨어져서 살 확률로 여친이 생김", "뭘 바라니..", "앞으로 10년 간 바지 속 물건이 신상", "20년 내로 가능함!!", "밖에 나가봐라", "자신감을 가져보셈", "아마도 될까?", "존슨이 곧 기뻐할것", "매력뿜뿜", "모르겠다", "얼굴은 잘생겼냐?", "거울을 봐라", "니 자신을 알라", "센스쟁이가 되어라", "카톡고백같은거 하지 좀 마", "되겠냐?", "기다리는 사람이 있다", "그녀의 태도를 보아라"]
        mon = ["길 가다 100원을 주울 수 있음", "자판기에 1000원권 넣었는데 아무것도 안됨", "당장 나가서 구걸을 하면 5만원을 벌 수 있다!"]
        hak = ["중간고사에서 1등급 맞을 수 있다!", "희망이 없어... (Endgame)", "멍청이"]
        await message.channel.send(f'{message.author.mention}님의 운세를 봐드릴게요.\n연애운: {koi[random.randint(0, len(koi)-1)]}\n금전운: {mon[random.randint(0, len(mon)-1)]}\n학업운: {hak[random.randint(0, len(hak)-1)]}')

    if message.content.startswith('Z음챗'):
        # 보이스 채널 ID를 가져옵니다.
        channel_id = message.author.voice.channel.id
        # 해당 채널에 연결합니다.
        vc = await client.get_channel(channel_id).connect()

    if message.content.startswith('고양이'):
        with open(f'cat{random.randint(1, 10)}.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith('print wrong answer'): await message.chennel.send(f"{userdatabase[message.author.id][0]}")
    if message.content == "print userdatabase": await message.channel.send(f"{userdatabase}")

    print(f"{message.channel}의 {message.author}: {message.content}")
    

client.run(token)
