from replit import db
import discord, requests, threading, random, time, socks, ctypes, os
from discord.ext import commands
from discord.ext.commands import cooldown

token = 'OTEyMDUzMTgwMjUzMjI5MDk2.YZqVtw.koQcwXKaTwu7RvdUEz75AkNg8ng'
Prefix = "$"

#Help
async def help(ctx):
    if ctx.channel.id == commandchannel:
        embed = discord.Embed(color=0x00b8ff)
        embed.add_field(name='**Followers**', value=f'`{prefix}tfollow` `(channel)`', inline=True)
        embed.add_field(name='**Unfollows**', value=f'`{prefix}tunfollow` `(channel)`', inline=True)
        embed.add_field(name='**Friend Requests**', value=f'`{prefix}tfriend` `(channel)`', inline=True)
        embed.add_field(name='**Chat Spam**', value=f'`{prefix}tspam` `(channel)` `(message)`', inline=True)
        embed.add_field(name='**Trolling**', value=f'`{prefix}ttroll` `(channel)`', inline=True)
        embed.add_field(name='**Reports**', value=f'`{prefix}treport` `(channel)`', inline=True)
        embed.add_field(name='**Raids**', value=f'`{prefix}traid` `(channel)`', inline=True)
        embed.add_field(name='**Hosts**', value=f'`{prefix}thost` `(channel)`', inline=True)
        embed.add_field(name='**Live Views**', value=f'`{prefix}tview` `(channel)`', inline=True)
        embed.set_author(name='Basic Services | Twitch Tool')
        await ctx.send(embed=embed)
    else:
        await ctx.message.delete()

#Twitch Followers
async def tfollow(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            bronze = discord.utils.get(ctx.guild.roles, name='Bronze')
            if bronze in ctx.author.roles:
                max_amount += 25
            silver = discord.utils.get(ctx.guild.roles, name='Silver')
            if silver in ctx.author.roles:
                max_amount += 100
            gold = discord.utils.get(ctx.guild.roles, name='Gold')
            if gold in ctx.author.roles:
                max_amount += 325
            crystal = discord.utils.get(ctx.guild.roles, name='Crystal')
            if crystal in ctx.author.roles:
                max_amount += 625
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                max_amount += 975
            owner = discord.utils.get(ctx.guild.roles, name='Owner')
            if owner in ctx.author.roles:
                max_amount += 20
            max_amount += 25
            if amount is None:
                amount = max_amount
            elif amount > max_amount:
                amount = max_amount
            if amount <= max_amount:
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Followers**", description=f"Sending **{amount}** Twitch Followers to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
                
                logembed = embed=discord.Embed(title="**Twitch Followers**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Followers to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                amount = amount
                queue.append(f'tfollow-{channel}-{amount}')

                def follow():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08",
                                'version': 1
                            }
                        },
                        'operationName': "FollowButton_FollowUser",
                        'variables': {
                            'input': {
                                'disableNotifications': False,
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )
            for i in range(amount):
                threading.Thread(target=follow).start()
        else:  
            await ctx.message.delete()

#Twitch Unfollows
async def tunfollow(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            bronze = discord.utils.get(ctx.guild.roles, name='Bronze')
            if bronze in ctx.author.roles:
                max_amount += 40
            silver = discord.utils.get(ctx.guild.roles, name='Silver')
            if silver in ctx.author.roles:
                max_amount += 160
            gold = discord.utils.get(ctx.guild.roles, name='Gold')
            if gold in ctx.author.roles:
                max_amount += 390
            crystal = discord.utils.get(ctx.guild.roles, name='Crystal')
            if crystal in ctx.author.roles:
                max_amount += 600
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                max_amount += 825
            owner = discord.utils.get(ctx.guild.roles, name='Owner')
            if owner in ctx.author.roles:
                max_amount += 5000
            max_amount += 25
            if amount is None:
                amount = max_amount
            elif amount > max_amount:
                amount = max_amount
            if amount <= max_amount:
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Unfollows**", description=f"Removing **{amount}** Twitch Followers from `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Unfollows**", description=f"{ctx.author.mention} Removed `{amount}` Twitch Followers from **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)

                def unfollow():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)
                    
                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880",
                                'version': 1
                            }
                        },
                        'operationName': "FollowButton_UnfollowUser",
                        'variables': {
                            'input': {
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )
                for i in range(int(amount)):
                    threading.Thread(target=unfollow).start()
        else:  
            await ctx.message.delete()

#Twitch Friends
async def tfriend(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            bronze = discord.utils.get(ctx.guild.roles, name='Bronze')
            if bronze in ctx.author.roles:
                max_amount += 15
            silver = discord.utils.get(ctx.guild.roles, name='Silver')
            if silver in ctx.author.roles:
                max_amount += 55
            gold = discord.utils.get(ctx.guild.roles, name='Gold')
            if gold in ctx.author.roles:
                max_amount += 105
            crystal = discord.utils.get(ctx.guild.roles, name='Crystal')
            if crystal in ctx.author.roles:
                max_amount += 215
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                max_amount += 425
            owner = discord.utils.get(ctx.guild.roles, name='Owner')
            if owner in ctx.author.roles:
                max_amount += 2000
            max_amount += 10
            if amount is None:
                amount = max_amount
            elif amount > max_amount:
                amount = max_amount
            if amount <= max_amount:
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Friend Requests**", description=f"Sending **{amount}** Twitch Friend Requests to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Friend Requests**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Friend Requests to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                queue.append(f'tfriend-{channel}-{amount}')

                def friends():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "380d8b19fcffef2fd8654e524444055dbca557d71968044115849d569d24129a",
                                'version': 1
                            }
                        },
                        'operationName': "FriendButton_CreateFriendRequest",
                        'variables':{
                            'input': {
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )
                for i in range(int(amount)):
                    threading.Thread(target=friends).start()
        else:  
            await ctx.message.delete()

#Twitch Raids
async def traid(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                max_amount += 10
                if amount is None:
                    amount = max_amount
                elif amount > max_amount:
                    amount = max_amount
                if amount <= max_amount:
                    len(queue) + 1

                embed=discord.Embed(title="**Twitch Raids**", description=f"Sending **{amount}** Twitch Raids to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Raids**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Raids to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                queue.append(f'traid-{channel}-{amount}')

                def raid():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        "Authorization": f"OAuth {token}"
                    }
                    r = requests.get(
                        "https://id.twitch.tv/oauth2/validate",
                        headers=headers
                    )
                    sourceid = r.json()['login']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "22a78bb2a257874ae80ae914a667f7fdd65eeab678e4ae39d38f3d1e220c1811",
                                'version': 1
                            }
                        },
                        'operationName': "chatRaidChannelIDs",
                        'variables': {
                            'sourceID': sourceid,
                            'targetID': channel
                        }
                    }

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )

                    targetid = r.json()['data']['target']['id']
                    sourceid = r.json()['data']['source']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "f4fc7ac482599d81dfb6aa37100923c8c9edeea9ca2be854102a6339197f840a",
                                'version': 1
                            }
                        },
                        'operationName': "chatCreateRaid",
                        'variables': {
                            'input': {
                                'sourceID': sourceid,
                                'targetID': targetid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )

                    time.sleep(11)

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "878ca88bed0c5a5f0687ad07562cffc0bf6a3136f15e5015c0f5f5f7f367f70a",
                                'version': 1
                            }
                        },
                        'operationName': "GoRaid",
                        'variables': {
                            'input': {
                                'sourceID': sourceid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )

                for i in range(int(amount)):
                    threading.Thread(target=raid).start()
                    #time.sleep(5)
            else:
                embed=discord.Embed(title="**Error**", description=f"This is a **Premium** only command.", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()

#Twitch Hosts
async def thost(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                max_amount += 20
                if amount is None:
                    amount = max_amount
                elif amount > max_amount:
                    amount = max_amount
                if amount <= max_amount:
                    len(queue) + 1

                embed=discord.Embed(title="**Twitch Hosts**", description=f"Sending **{amount}** Twitch Hosts to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Hosts**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Hosts to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                queue.append(f'thost-{channel}-{amount}')

                def host():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    headers = {
                        "Authorization": f"OAuth {token}"
                    }
                    r = requests.get(
                        "https://id.twitch.tv/oauth2/validate",
                        headers=headers
                    )
                    sourceid = r.json()['login']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "11432338da6c191c4df21630d2d87008a383a038045b2cc5e37ea3ca65ca4fe8",
                                'version': 1
                            }
                        },
                        'operationName': "RaidUpsell_Channel",
                        'variables': {
                            'sourceChannelLogin': sourceid,
                            'targetChannelLogin': channel
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers
                    )

                    targetid = r.json()['data']['targetChannel']['id']
                    channelid = r.json()['data']['sourceChannel']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "6c0a490991ca61a2cafa59e89eb4a70b9973d025767b1601b5922da56fe677ea",
                                'version': 1
                            }
                        },
                        'operationName': "chatCommandHost",
                        'variables': {
                            'input': {
                                'channelID': channelid,
                                'targetID': targetid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers
                    )
                for i in range(int(amount)):
                    threading.Thread(target=host).start()
            else:
                embed=discord.Embed(title="**Error**", description=f"This is a **Premium** only command.", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete

#Twitch Spam
async def tspam(ctx, channel, *, message):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            spam = discord.utils.get(ctx.guild.roles, name='Premium')
            if spam in ctx.author.roles:
                amount = 30
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Chat Spam**", description=f"Spamming **{channel}** with the message `{message}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Chat Spam**", description=f"{ctx.author.mention} Spammed `{channel}` with the message **{message}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                queue.append(f'tspam-{channel}-{amount}')

                def spam():

                    lines = open('spam.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08",
                                'version': 1
                            }
                        },
                        'operationName': "FollowButton_FollowUser",
                        'variables': {
                            'input': {
                                'disableNotifications': False,
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )

                    headers = {
                        "Authorization": f"OAuth {token}"
                    }
                    r = requests.get(
                        "https://id.twitch.tv/oauth2/validate",
                        headers=headers
                    )
                    name = r.json()['login']

                    proxy = proxy.split(":")
                    s = socks.socksocket()
                    s.set_proxy(socks.HTTP, proxy[0],int(proxy[1]))
                    s.connect(("irc.chat.twitch.tv", 6667))
                    s.send("PASS {}\r\n".format("oauth:" + token).encode("utf8"))
                    s.send("NICK {}\r\n".format(name).encode("utf8"))
                    s.send("JOIN {}\r\n".format(channel).encode("utf8"))
                    s.send(('PRIVMSG #' + channel + f' : {message} \r\n').encode('utf8'))
                    s.close()

                for i in range(int(amount)):
                    threading.Thread(target=spam).start()
            else:
                embed=discord.Embed(title="**Error**", description=f"This is a **Gold** & **Premium** only command.", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
        else:  
            await ctx.message.delete()

#Twitch Troll
async def ttroll(ctx, channel):

    message = 'Trolled by --.gg/basics'

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            premium = discord.utils.get(ctx.guild.roles, name='Premium')
            if premium in ctx.author.roles:
                amount = 25
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Trolling**", description=f"Trolling `{channel}` 25 times", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)

                logembed = embed=discord.Embed(title="**Twitch Trolling**", description=f"{ctx.author.mention} Trolled `{channel}` **25 times**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                queue.append(f'ttroll-{channel}-{message}')

                def troll():

                    lines = open('spam.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08",
                                'version': 1
                            }
                        },
                        'operationName': "FollowButton_FollowUser",
                        'variables': {
                            'input': {
                                'disableNotifications': False,
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        json=data, headers=headers, proxies=proxies
                    )

                    headers = {
                        "Authorization": f"OAuth {token}"
                    }
                    r = requests.get(
                        "https://id.twitch.tv/oauth2/validate",
                        headers=headers
                    )
                    name = r.json()['login']

                    proxy = proxy.split(":")
                    s = socks.socksocket()
                    s.set_proxy(socks.HTTP, proxy[0],int(proxy[1]))
                    s.connect(("irc.chat.twitch.tv", 6667))
                    s.send("PASS {}\r\n".format("oauth:" + token).encode("utf8"))
                    s.send("NICK {}\r\n".format(name).encode("utf8"))
                    s.send("JOIN {}\r\n".format(channel).encode("utf8"))
                    s.send(('PRIVMSG #' + channel + f' : {message} \r\n').encode('utf8'))
                    s.close()

                for i in range(int(amount)):
                    threading.Thread(target=troll).start()
            else:
                embed=discord.Embed(title="**Error**", description=f"This is a **Premium** only command.", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()

#Twitch Report
async def treport(ctx, channel, amount: int=None):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            max_amount = 0
            bronze = discord.utils.get(ctx.guild.roles, name='Bronze')
            if bronze in ctx.author.roles:
                max_amount += 10
            silver = discord.utils.get(ctx.guild.roles, name='Silver')
            if silver in ctx.author.roles:
                max_amount += 40
            gold = discord.utils.get(ctx.guild.roles, name='Gold')
            if gold in ctx.author.roles:
                max_amount += 100
            crystal = discord.utils.get(ctx.guild.roles, name='Crystal')
            if crystal in ctx.author.roles:
                max_amount += 320
            premium = discord.utils.get(ctx.guild.roles, name='premium')
            if premium in ctx.author.roles:
                max_amount += 500
            max_amount += 5
            if amount is None:
                amount = max_amount
            elif amount > max_amount:
                amount = max_amount
            if amount <= max_amount:
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Reports**", description=f"Sending **{amount}** Twitch Reports to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
                
                logembed = embed=discord.Embed(title="**Twitch Reports**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Reports to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                amount = amount
                queue.append(f'treport-{channel}-{amount}')

                def report():

                    lines = open('tokens.txt', 'r').read().splitlines()
                    token = random.choice(lines)

                    proxies = open("proxy.txt", "r").read().splitlines()
                    proxy = random.choice(proxies)

                    headers = {
                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

                    r = requests.post(
                        "https://gql.twitch.tv/gql",
                        data=data, headers=headers
                    )

                    channelid = r.json()[0]['data']['user']['id']

                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        "Authorization": f"OAuth {token}",
                        "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                        "Content-Type": "application/json"
                    }
                    proxies = {
                        "http": "http://"+proxy,
                        "https": "http://"+proxy,
                    }
                    data = {
                        'extensions': {
                            'persistedQuery': {
                                'sha256Hash': "dd2b8f6a76ee54aff685c91537fd75814ffdc732a74d3ae4b8f2474deabf26fc",
                                'version': 1
                            }
                        },
                        'operationName': "ReportUserModal_ReportUser",
                        'variables': {
                            'input': {
                                'content': "LIVESTREAM_REPORT",
                                'contentID': "",
                                'description': "report context: USER_REPORT\n\nvideo > terrorism_mass_violence\n\ndescription: They threatened to shoot someone and talking like a terrorist.",
                                'extra': "",
                                'reason': "terrorism_mass_violence",
                                'targetID': channelid
                            }
                        }
                    }
                    r = requests.post(
                        'https://gql.twitch.tv/gql',
                        json=data, headers=headers, proxies=proxies
                    )

                for i in range(int(amount)):
                    threading.Thread(target=report).start()
        else:
            await ctx.message.delete()

#Twitch Live Views
@commands.cooldown(0, 000, type=commands.BucketType.user)
async def tview(ctx, channel):

    headers = {
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+channel+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'

    r = requests.post(
        "https://gql.twitch.tv/gql",
        data=data, headers=headers
    )
    if '[{"data":{"user":null}' in r.text:
            embed=discord.Embed(title="**Error**", description=f"**{channel}** is not a valid Twitch name.", color=0x00b8ff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
            embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
            await ctx.send(embed=embed)
    else:
        if ctx.channel.id == commandchannel:
            views = discord.utils.get(ctx.guild.roles, name='View Access')
            if views in ctx.author.roles:
                amount = 30
                len(queue) + 1

                embed=discord.Embed(title="**Twitch Live Views**", description=f"Sending **{amount}** Twitch Live Views to `{channel}`", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
                
                logembed = embed=discord.Embed(title="**Twitch Live Views**", description=f"{ctx.author.mention} Sent `{amount}` Twitch Live Views to **{channel}**", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                await ctx.guild.get_channel(logs).send(embed=logembed)
                amount = amount
                queue.append(f'tview-{channel}-{amount}')

                def view():

                    proxy = random.choice(open('proxy.txt').read().splitlines())
                    proxies = {'https': f'socks4://{proxy}'}

                    options = webdriver.ChromeOptions()

                    options.add_argument('--proxy-server=%s' % proxy)
                    driver = webdriver.Chrome(options=options)

                    driver.get("https://www.twitch.tv/" + channel)
                    #os.system('pause')
                    time.sleep(900)
                    driver.close()

                for i in range(int(amount)):
                    threading.Thread(target=view).start()
            else:
                embed=discord.Embed(title="**Error**", description=f"This is a command for View Access users only.", color=0x00b8ff)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968364986919424070/968711852974546944/image.jpg")
                embed.add_field(name="Requested By:", value=f"{ctx.author.mention}", inline=True)
                await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            tview.reset_cooldown(ctx)

bot.run(token)