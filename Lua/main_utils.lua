local utils = {}
local RPS = {'rock', 'paper', 'scissors'}
local ai

function utils.GetRPS(user)
    io.write('Rock, Paper, Scissors?\n')
    user = io.read()
    for i=1, #RPS do
        if user == RPS[i] then
            return RPS[i], true
        end
    end
    return user, false
end


function utils.Game(user)
    ai = RPS[math.random(#RPS)]
    if user == 'rock' then
        if ai == 'rock' then
            result = 'Draw'
        else if ai == 'paper' then
            result = 'Lose'
        else
            result = 'Win'
        end
        end

    else if user == 'paper' then
        if ai == 'rock' then
            result = 'Win'
        else if ai == 'paper' then
            result = 'Draw'
        else
            result = 'Lose'
        end
        end

    else
        if ai == 'rock' then
            result = 'Lose'
        else if ai == 'paper' then
            result = 'Win'
        else
            result = 'Draw'
        end
        end
    end
    end
    return result
end


return utils

