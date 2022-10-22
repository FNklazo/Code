local main_utils = require "main_utils"
local user, ai, bool
local RPS = {'rock', 'paper', 'scissors'}

local function main()
    while true do
        user, bool = main_utils.GetRPS(user, RPS)
        if bool then
            ai = RPS[math.random(#RPS)]
            
        end
    end
end


main()