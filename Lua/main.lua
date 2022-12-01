local main_utils = require "main_utils"
local user, bool


local function main()
    while true do
        user, bool = main_utils.GetRPS(user)
        if bool then
            print('\n', main_utils.Game(user, ai), '\n')
        end
    end
end


main()