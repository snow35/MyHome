import discord
import interactions
import serial

intents = discord.Intents.default()
intents.message_content = True

ser = serial.Serial('COM10', 9600)
bot = interactions.Client(token="Yout_Bot_Token")

allowed_user_id = "User_ID"

def is_allowed_user(user_id):
    return str(user_id) == allowed_user_id

@bot.command(
    name="hello",
    description="봇이 인사를 해줘요!",  
    scope=Guild_ID,
)
async def hello(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        await ctx.send("안녕하세요!")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

@bot.command(
    name="room1_light_on",
    description="1번 방의 불을 켭니다",
    scope=Guild_ID,
)
async def Room_1_Light_ON(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        ser.write(b'1')
        await ctx.send("1번 방의 불이 켜졌습니다.")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

@bot.command(
    name="room1_light_off",
    description="1번 방의 불을 끕니다.",
    scope=Guild_ID,
)
async def Room_1_Light_OFF(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        ser.write(b'0')
        await ctx.send("1번 방의 불이 꺼졌습니다.")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

@bot.command(
    name="read_now_temperature",
    description="집 내부 온도를 측정합니다.",
    scope=Guild_ID,
)
async def read_temp(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        ser.write(b'T')
        now_temp = ser.readline().decode().strip()
        await ctx.send(f"현재 온도는 {now_temp}°C 입니다.")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

@bot.command(
    name="read_now_humidity",
    description="집 내부 습도를 측정합니다.",
    scope=Guild_ID,
)
async def read_humidity(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        ser.write(b'H')
        now_hum = ser.readline().decode().strip()
        await ctx.send(f"현재 습도는 {now_hum}% 입니다.")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

@bot.command(
    name="read_now_brightness",
    description="현재 집 내부 밝기를 측정합니다. 1부터 10까지 범위로 표현합니다.",
    scope=Guild_ID,
)
async def read_brightness(ctx: interactions.CommandContext):
    if is_allowed_user(ctx.user.id):
        ser.write(b'B')
        now_brightness = ser.readline().decode().strip()
        await ctx.send(f"현재 밝기는 {now_brightness} 입니다.")
    else:
        await ctx.send("죄송합니다. 등록된 사용자가 아닙니다.")

bot.start()