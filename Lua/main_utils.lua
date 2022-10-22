local utils = {}

function utils.GetRPS(user, array)
    io.write('Rock, Paper, Scissors?\n')
    user = io.read()
    for i=1, #array do
        if string.match(array[i][1], user[1]) then
            return array[i], true
        end
    return user, false
    end
end


return utils