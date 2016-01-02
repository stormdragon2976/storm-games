-- Store operating system commands in a variable.
function os.capture(cmd, raw)
    local f = assert(io.popen(cmd, 'r'))
    local s = assert(f:read('*a'))
    f:close()
    if raw then
        return s
    end
    s = string.gsub(s, '^%s+', '')
    s = string.gsub(s, '%s+$', '')
    s = string.gsub(s, '[\n\r]+', ' ')
    return s
end

-- Speak with appropriate tool.
local function speak(text)
    if os.capture("uname") == "Linux" then
        os.execute('spd-say "' .. text .. '"')
    else
        os.execute('say "' .. text .. '"')
    end
end

-- Window related variables.
local gameName = "Bottle Blaster"

local SDL	= require "SDL"
local mixer = require "SDL.mixer"
local ret, err = SDL.init { SDL.flags.Video }
if not ret then
    error(err)
end

local function trySDL(func, ...)
    local t = { func(...) }

    if not t[1] then
        error(t[#t])
    end

    return table.unpack(t)
end

local function exit_game(SDL, mixer)
    SDL.quit()
    mixer.quit()
    return false
end

local win, err = SDL.createWindow {
    title	= gameName,	
    width	= 320,
    height	= 320
}

if not win then
    error(err)
end

trySDL(mixer.openAudio, 44100, SDL.audioFormat.S16, 2, 1024)
-- Load all game sounds here:
-- Format: local variableName = trySDL(mixer.loadWAV, "path/to/file")
-- Supported file types flac, ogg, wav
local bottle =
{
    trySDL(mixer.loadWAV, "sounds/glass1.ogg"),
    trySDL(mixer.loadWAV, "sounds/glass2.ogg"),
    trySDL(mixer.loadWAV, "sounds/glass3.ogg")
}
local gun =
{
    trySDL(mixer.loadWAV, "sounds/gun1.ogg"),
    trySDL(mixer.loadWAV, "sounds/gun2.ogg"),
    trySDL(mixer.loadWAV, "sounds/gun3.ogg"),
    trySDL(mixer.loadWAV, "sounds/gun4.ogg"),
    trySDL(mixer.loadWAV, "sounds/gun5.ogg")
}
local empty = trySDL(mixer.loadWAV, "sounds/empty.ogg")
local load = {}
load[3] = trySDL(mixer.loadWAV, "sounds/load3.ogg")
load[4] = trySDL(mixer.loadWAV, "sounds/load3.ogg")
load[5] = trySDL(mixer.loadWAV, "sounds/load5.ogg")

local function play_sound(sound, channel, loop)
    channel = channel or -1
    loop = loop or 0
    sound:playChannel(channel, loop)
end

local function play_at_location(sound, xPosition, yPosition)
    channel = channel or -1
    loop = loop or 0
    xPosition = xPosition or 0
    yPosition = yPosition or 0
    mixer.SetPanning(-1, 255, 127)
    sound:playChannel(-1, 0)
end

local function game_intro()
    local sound = trySDL(mixer.loadWAV, "sounds/game-intro.ogg")
sound:playChannel(-1, 0)
    while mixer.playing(-1) > 0 do
        SDL.delay(100)
    end
end

-- Game variables
local direction = ""
local holdKey = {}
local keyName = ""
local loaded = true
local playerPosition = math.random(0, 30)
local running = true
local weapon = 1

-- game functions.
local function player_move(position, direction)
    if direction == "Left" and position > 0 then
        position = position - 1
    end
    if direction == "Right" and position < 30 then
        position = position + 1
    end
    return position
end

game_intro()
-- Main game loop.
while running do
    -- Need a timer to make holding arrows move at a slower speed. for player_move()
    playerPosition = player_move(playerPosition, direction)
    -- Iterate over all events, this function does not block.
    for e in SDL.pollEvent() do
        if e.type == SDL.event.KeyUp then --chrys just recognice the keyup and free the loop
            keyName = SDL.getKeyName(e.keysym.sym)
            holdKey[keyName] = false
            direction = ""
            -- speak(playerPosition)
        end
        if e.type == SDL.event.Quit then
            running = false
        elseif e.type == SDL.event.KeyDown and not holdKey[keyName] then -- chrysif not already down ( see below)
            keyName = SDL.getKeyName(e.keysym.sym)
            holdKey[keyName] = true --chrys mark the remember the keydown
            if keyName == "Q" then
                running = exit_game(SDL, mixer)
            elseif keyName == "Left Shift" or keyName == "Right Shift" then
                if weapon >= 3 and loaded == false then
                    -- Need to not allow firing until loading is complete.
                    play_sound(load[weapon])
                end
                loaded = true
            elseif keyName == "Space" then
                if loaded == true then
                    play_sound(gun[weapon])
                    play_sound(bottle[math.random(1, #bottle)])
                else
                    play_sound(empty)
                end
                if weapon >= 3 then
                    loaded = false
                end
            elseif keyName == "Left" or keyName == "Right" then
                direction = keyName
            elseif tonumber(keyName) == nil then -- make sure keyName can be converted to a number for remaing if statements to avoid a crash.
                keyName = "0"
            elseif tonumber(keyName) >= 1 and tonumber(keyName) <= 5 then
                weapon = tonumber(keyName)
                if weapon >= 3 then
                    loaded = false
                else
                    loaded = true
                end
                if weapon == 1 then
                    speak("pistal")
                elseif weapon == 2 then
                    speak("beretta")
                elseif weapon == 3 then
                    speak("boomstick shotgun")
                elseif weapon == 4 then
                    speak("pump action shotgun")
                elseif weapon == 5 then
                    speak("bo and arrow")
                end
            end
        end
    end
end

